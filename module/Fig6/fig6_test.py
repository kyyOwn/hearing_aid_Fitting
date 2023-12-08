'''
@FilePath: fig6_test.py
@Author: Kangyuyong
@Date: 2023-12-08
@LastEditTime: 2023-12-08
@Description: 
@Email: yuyongkang1024@gmail.com
'''

import os
import numpy as np
import argparse

from fig6_prescription import FIG6

def main():

    pta_num = 5
    pta = np.array([40, 50, 40, 40, 40])
    pta_freq = np.array([500, 1000, 2000, 4000, 8000])
    channel_num = 8
    channel_freq = np.array([250, 500, 1000, 1500, 2000, 3000, 4500, 6500])

    fig6 = FIG6(channel_num, pta_num, channel_freq, pta_freq)

    fig6.input_pta(pta)

    G40, G65, G95 = fig6.prescript()

    print("Freq.: " + str(channel_freq))
    print("G40: " + str(G40))
    print("G65: " + str(G65))
    print("G95: " + str(G95))

    return



if __name__ == "__main__":
    main()
