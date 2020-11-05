import Tkinter as tkinter
#from Tkinter import messagebox
import tkMessageBox as messagebox
from eegloger import NeuroLog
from time import sleep
import csv
import threading
import pandas as pd
import numpy as np
import datetime
measureflag = False
thred_value = None

def button_click():
    global measureflag
    if measureflag:
        pass
    elif input_port.get() == '' or input_EEGKind.get() == '' or input_dir.get() == '' or input_file.get() == '':
        vali_msg = 'please fill in the values!\n'
        messagebox.showinfo('Note',vali_msg)
    else:
        global thred_value
        thred_value = threading.Thread(target=eeg_loger)
        thred_value.setDaemon(True)
        thred_value.start()

def eeg_loger():
    port = input_port.get()
    eegkind = input_EEGKind.get()
    directory = input_dir.get()
    filename = input_file.get()
    
    global measureflag
    measureflag = True
        
    eeg = NeuroLog(port)
    eeg.update(eegkind)
    try:
        eeg.headset.start()
        while measureflag == True:
            sleep(1)
        eeg.headset.stop()
        recodeFlag = True
    except Exception as e:
        recodeFlag = False
        print e
    finally:
        try:
            if recodeFlag:
                if eegkind == "eeg":
                    """
                    eeg_dataframe = pd.DataFrame({'lowAlphaTimeStamp':eeg.time_lowA,'lowAlpha':eeg.df_lowAlpha,
                                                  'highAlphaTimStamp':eeg.time_highA,'highAlpha':eeg.df_highAlpha,
                                                  'lowBetaTimeStamp':eeg.time_lowB,'lowBeta':eeg.df_lowBeta,
                                                  'highBetaTimeStamp':eeg.time_highB,'highBeta':eeg.df_highBeta,
                                                  'lowGammaTimeStamp':eeg.time_lowG,'lowGamma':eeg.df_lowGamma,
                                                  'midGammaTimeStamp':eeg.time_midG,'midGamma':eeg.df_midGamma,
                                                  'deltaTimeStamp':eeg.time_delta,'delta':eeg.df_delta,
                                                  'thetaTimeStamp':eeg.time_theta,'theta':eeg.df_theta})
                    """
                    eeg_dataframe = pd.DataFrame({'TimeStamp':eeg.time_midG,
                                                  'lowAlpha':eeg.df_lowAlpha,
                                                  'highAlpha':eeg.df_highAlpha,
                                                  'lowBeta':eeg.df_lowBeta,
                                                  'highBeta':eeg.df_highBeta,
                                                  'lowGamma':eeg.df_lowGamma,
                                                  'midGamma':eeg.df_midGamma,
                                                  'delta':eeg.df_delta,
                                                  'theta':eeg.df_theta})
                    eeg_dataframe.to_csv('{0}\\eeglog_{1}_{2}.csv'.format(directory,eegkind,filename))
                else:
                    with open('{0}\\eeglog_{1}_{2}.csv'.format(directory,eegkind,filename),'w') as f:
                        writer = csv.writer(f)
                        writer.writerow(eeg.df)
                recodeFlag = False
            else:
                pass
        except Exception as e:
            print("filesavederror|{}".format(e))
            print(eeg.df)
            

def stoping():
    global measureflag
    measureflag = False
    
    global thred_value
    thred_value.join()

root = tkinter.Tk()
root.title('EEG Measuring soft')
root.geometry("300x120")

input_port_label = tkinter.Label(text='PORT')
input_port_label.grid(row=1,column=1,padx=10,)
input_port = tkinter.Entry(width=30)
input_port.grid(row=1,column=2)

input_EEGKind_label = tkinter.Label(text='Data')
input_EEGKind_label.grid(row=2,column=1)
input_EEGKind = tkinter.Entry(width=30)
input_EEGKind.grid(row=2,column=2)

input_dir_label = tkinter.Label(text='directory')
input_dir_label.grid(row=3,column=1)
input_dir = tkinter.Entry(width=30)
input_dir.grid(row=3,column=2)

input_file_label = tkinter.Label(text='filename')
input_file_label.grid(row=4,column=1)
input_file = tkinter.Entry(width=30)
input_file.grid(row=4,column=2)

button = tkinter.Button(text='measure',command=button_click, width=10)
button.place(x=10,y=90)

stop = tkinter.Button(text='stop',command=stoping,width=10)
stop.place(x=150,y=90)

root.mainloop()