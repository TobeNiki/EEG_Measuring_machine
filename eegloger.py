from NeuroPy import NeuroPy
import pandas as pd
from time import sleep

class NeuroLog(object):
    def __init__(self,PORT='COM3'):
        self.headset = NeuroPy(PORT)
        
    def update(self, EEG='attention'):
        def get_rawdata(raw_value):
            print raw_value
            self.df.append(raw_value)
            return None

        def attention_callback(attention_value):
            print attention_value
            self.df.append(attention_value)
            return None

        def meditation_callback(meditation_value):
            print meditation_value
            self.df.append(meditation_value)
            return None
        if(EEG == 'attention'):
            self.df = []
            self.headset.setCallBack('attention',attention_callback)
        elif(EEG == 'meditation'):
            self.df = []
            self.headset.setCallBack('meditation',meditation_callback)
        else:
            self.df = []
            self.headset.setCallBack('rawValue',get_rawdata)
