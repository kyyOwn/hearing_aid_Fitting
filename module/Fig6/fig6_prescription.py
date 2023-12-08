'''
@FilePath: fig6_prescription.py
@Author: Kangyuyong
@Date: 2023-12-08
@LastEditTime: 2023-12-08
@Description: 
@Email: yuyongkang1024@gmail.com
'''

import os
import numpy as np

class FIG6():
    def __init__(self, channel_num, pta_num, channel_freq, pta_freq):
        self.channel_num = channel_num
        self.pat_num = pta_num
        self.pta_freq = pta_freq
        self.channel_freq = channel_freq
        self.pats = np.zeros(pta_num)
        self.G40 = np.zeros(channel_num)
        self.G65 = np.zeros(channel_num)
        self.G95 = np.zeros(channel_num)
        self.G40_pta = np.zeros(pta_num)
        self.G65_pta = np.zeros(pta_num)
        self.G95_pta = np.zeros(pta_num)
        return
    def input_pta(self, ptas):
        self.ptas = ptas

    def generate_G40(self, pta):
        IG = 0
        if pta < 20:
            IG = 0
        elif pta <=60:
            IG = pta - 20
        else:
            IG = 0.5 * pta + 10
        return IG
    
    def generate_G65(self, pta):
        IG = 0
        if pta < 20:
            IG = 0
        elif pta <= 60:
            IG = 0.6 * (pta - 20)
        else:
            IG = 0.8 * pta - 23
        return IG
        
    def generate_G95(self, pta):
        IG = 0
        if pta <= 40:
            IG = 0
        else:
            IG = 0.1 * (pta - 40)
        return IG
    
    def prescript(self):
        for id in range(self.pat_num):
            self.G40_pta[id] = self.generate_G40(self.ptas[id])
            self.G65_pta[id] = self.generate_G65(self.ptas[id])
            self.G95_pta[id] = self.generate_G95(self.ptas[id])
        for ch in range(self.channel_num):
            if self.channel_freq[ch] <= self.pta_freq[0]:
                self.G40[ch] = self.G40_pta[0]
                self.G65[ch] = self.G65_pta[0]
                self.G95[ch] = self.G95_pta[0]
            elif self.channel_freq[ch] >= self.pta_freq[-1]:
                self.G40[ch] = self.G40_pta[-1]
                self.G65[ch] = self.G65_pta[-1]
                self.G95[ch] = self.G95_pta[-1]
            else:
                cur_freq = self.channel_freq[ch]
                id1 = np.where(self.pta_freq > cur_freq )
                id2 = np.where(self.pta_freq <= cur_freq )
                low_id = np.reshape(id2, -1)
                low_id = low_id[-1]
                hig_id = np.reshape(id1, -1)
                hig_id = hig_id[0]
                low_freq = self.pta_freq[low_id]
                hig_freq = self.pta_freq[hig_id]
                self.G40[ch] = (cur_freq - low_freq) / (hig_freq -low_freq) * (self.G40_pta[hig_id] - self.G40_pta[low_id]) + self.G40_pta[low_id]
                self.G65[ch] = (cur_freq - low_freq) / (hig_freq -low_freq) * (self.G65_pta[hig_id] - self.G65_pta[low_id]) + self.G65_pta[low_id]
                self.G95[ch] = (cur_freq - low_freq) / (hig_freq -low_freq) * (self.G95_pta[hig_id] - self.G95_pta[low_id]) + self.G95_pta[low_id]

        return self.G40, self.G65, self.G95


