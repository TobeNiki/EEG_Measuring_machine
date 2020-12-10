from NeuroPy import NeuroPy
from time import sleep
import threading
import datetime
import pandas as pd

class NeuroLog(object):
    def __init__(self,PORT='COM3'):
        self.headset = NeuroPy(PORT)
        
    def update(self, EEG):
        def raw_callback(raw_value):
            print("raw{}".format(raw_value))
            self.df.append(raw_value)
            return None

        def theta_callback(theta_value):
            print("theta{}".format(theta_value))
            #self.time_theta.append(str(datetime.datetime.now()))
            self.df_theta.append(theta_value)
            return None

        def delta_callback(delta_value):
            print("delta{}".format(delta_value))
            #self.time_delta.append(str(datetime.datetime.now()))
            self.df_delta.append(delta_value)
            return None

        def lowAlpha_callback(lowAlpha_value):
            print("lowAlpha{}".format(lowAlpha_value))
            #self.time_lowA.append(str(datetime.datetime.now()))
            self.df_lowAlpha.append(lowAlpha_value)
            return None

        def highAlpha_callback(highAlpha_value):
            print("highAlpha{}".format(highAlpha_value))
            #self.time_highA.append(str(datetime.datetime.now()))
            self.df_highAlpha.append(highAlpha_value)
            return None

        def lowBeta_callback(lowBeta_value):
            print("lowBeta{}".format(lowBeta_value))
            #self.time_lowB.append(str(datetime.datetime.now()))
            self.df_lowBeta.append(lowBeta_value)
            return None

        def highBeta_callback(highBeta_value):
            print("highBeta{}".format(highBeta_value))
            #self.time_highB.append(str(datetime.datetime.now()))
            self.df_highBeta.append(highBeta_value)
            return None

        def lowGamma_callback(lowGamma_value):
            print("lowGamma{}".format(lowGamma_value))
            #self.time_lowG.append(str(datetime.datetime.now()))
            self.df_lowGamma.append(lowGamma_value)
            return None

        def midGamma_callback(midGamma_value):
            print("midGamma{}".format(midGamma_value))
            self.time_midG.append(str(datetime.datetime.now()))
            self.df_midGamma.append(midGamma_value)
            return None

        def blinkStrength_callback(blinkStrength_value):
            print(blinkStrength_value)
            self.df.append(blinkStrength_value)
            return None

        def attention_callback(attention_value):
            print("attention{}".format(attention_value))
            self.df_attention.append(attention_value)
            return None

        def meditation_callback(meditation_value):
            print("meditation{}".format(meditation_value))
            self.df_meditation.append(meditation_value)
            return None

        if EEG == 'attention':
            self.df = []
            self.headset.setCallBack('attention',attention_callback)
        elif EEG == 'meditation':
            self.df = []
            self.headset.setCallBack('meditation',meditation_callback)
        elif EEG == "eeg":
            self.df = []
            self.df_delta,self.df_theta = [], []
            self.df_lowAlpha,self.df_highAlpha = [], []
            self.df_lowBeta,self.df_highBeta = [], []
            self.df_lowGamma,self.df_midGamma = [], []
            self.time_midG = []
            #self.time_delta,self.time_theta,self.time_lowA,self.time_highA = [],[],[],[]
            #self.time_lowB,self.time_highB,self.time_lowG,self.time_midG = [],[],[],[]
            self.headset.setCallBack('theta',theta_callback)
            self.headset.setCallBack("delta", delta_callback)
            self.headset.setCallBack("lowAlpha",lowAlpha_callback)
            self.headset.setCallBack("highAlpha",highAlpha_callback)
            self.headset.setCallBack("lowBeta",lowBeta_callback)
            self.headset.setCallBack("highBeta",highBeta_callback)
            self.headset.setCallBack("lowGamma",lowGamma_callback)
            self.headset.setCallBack("midGamma",midGamma_callback)
        elif EEG == "blink":
            self.df = []
            self.headset.setCallBack("blinkStrength",blinkStrength_callback)
        else:
            self.df = []
            self.headset.setCallBack('rawValue',raw_callback)


if __name__ == "__main__":
    headset = NeuroPy("COM3")
    def get_deltadata(delta_value): 
        print(delta_value)
    headset.setCallBack("delta",get_deltadata)
    headset.start()
    try:
        while True:
            sleep(1)
    except Exception as e:
        print(e)
    finally:
        headset.stop()
    