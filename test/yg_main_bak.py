#!/usr/bin/env python
# -*- coding:utf-8 -*-

#import sys
#from IRUtil import IRUtilities
from yg_utils import *

AC_KEYS = ["16_F_A_C", "17_F_A_C", "18_F_A_C", "19_F_A_C", "20_F_A_C", "21_F_A_C", "22_F_A_C", "23_F_A_C", "24_F_A_C", "25_F_A_C",
        "26_F_A_C", "27_F_A_C", "28_F_A_C", "29_F_A_C", "30_F_A_C", "16_F_1_C", "17_F_1_C", "18_F_1_C", "19_F_1_C", "20_F_1_C",
        "21_F_1_C", "22_F_1_C", "23_F_1_C", "24_F_1_C", "25_F_1_C", "26_F_1_C", "27_F_1_C", "28_F_1_C", "29_F_1_C",
        "30_F_1_C", "16_F_2_C", "17_F_2_C", "18_F_2_C", "19_F_2_C", "20_F_2_C", "21_F_2_C", "22_F_2_C", "23_F_2_C", "24_F_2_C",
        "25_F_2_C", "26_F_2_C", "27_F_2_C", "28_F_2_C", "29_F_2_C", "30_F_2_C", "16_F_3_C", "17_F_3_C", "18_F_3_C", "19_F_3_C",
        "20_F_3_C", "21_F_3_C", "22_F_3_C", "23_F_3_C", "24_F_3_C", "25_F_3_C", "26_F_3_C", "27_F_3_C", "28_F_3_C", "29_F_3_C",
        "30_F_3_C", "16_F_A_H", "17_F_A_H", "18_F_A_H", "19_F_A_H", "20_F_A_H", "21_F_A_H", "22_F_A_H", "23_F_A_H", "24_F_A_H",
        "25_F_A_H", "26_F_A_H", "27_F_A_H", "28_F_A_H", "29_F_A_H", "30_F_A_H", "16_F_1_H", "17_F_1_H", "18_F_1_H", "19_F_1_H",
        "20_F_1_H", "21_F_1_H", "22_F_1_H", "23_F_1_H", "24_F_1_H", "25_F_1_H", "26_F_1_H", "27_F_1_H", "28_F_1_H", "29_F_1_H",
        "30_F_1_H", "16_F_2_H", "17_F_2_H", "18_F_2_H", "19_F_2_H", "20_F_2_H", "21_F_2_H", "22_F_2_H", "23_F_2_H", "24_F_2_H",
        "25_F_2_H", "26_F_2_H", "27_F_2_H", "28_F_2_H", "29_F_2_H", "30_F_2_H", "16_F_3_H", "17_F_3_H", "18_F_3_H", "19_F_3_H",
        "20_F_3_H", "21_F_3_H", "22_F_3_H", "23_F_3_H", "24_F_3_H", "25_F_3_H", "26_F_3_H", "27_F_3_H", "28_F_3_H", "29_F_3_H",
        "30_F_3_H", "POWER", "POWER_OFF"]
TV_KEYS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Enter", "Mute", "Volume_Up", "Volume_Down",
        "Channel_Up", "Channel_Down", "Power", "Last", "Input", "Display", "Menu", "Select",
        "Navigate_Up", "Navigate_Down", "Navigate_Left", "Navigate_Right", "Exit", "---"]

DVD_KEYS = ["Power", "Rewind", "Play", "Fast_Forward", "Stop", "Pause", "Menu", "Select", "Navigate_Up", "Navigate_Down",
        "Navigate_Left", "Navigate_Right", "Exit", "Previous", "Next", "Audio_Channel", "Back", "Eject", "Volume_UP", "Volume_Down",
        "Mute", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

STB_KEYS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Enter", "Mute", "Channel_Up", 
            "Channel_Down", "Rewind", "Play", "Fast_Forward", "Record", "Stop", "Pause", 
            "Power", "Previous", "Menu", "Select", "Navigate_Up", "Navigate_Down", 
            "Navigate_Left", "Navigate_Right", "Exit", "DVR", "Back", "Last", 
            "Skip_Forward", "Skip_Back", "Info", "LiveTV", "OnDemand", 
            "Volume_Up", "Volume_Down", "Next", "Red", "Yellow", "Blue", "Green"]


if __name__ == "__main__":
    codes = []
    short_codes = []
    device_type_list = ["tv", "ac", "dvd", "stb"]
    drivce_type = None
    while not drivce_type in device_type_list:
        drivce_type = raw_input("Input the device type(tv, ac, dvd, stb):")
    
    print "press 'enter' to skip a key"
    print "press 'r' to recopy a key"
    print "press 'n' to copy next key"
    print
    print "================copy start================"
    
    codes.append("codesetid|frequency|type|key|uespulse|sys_code|data_code|format|full_code|")
    short_codes.append("codesetid|frequency|type|key|uespulse|")
    keys = None
    if drivce_type == "tv":
        keys = TV_KEYS
    elif drivce_type == "ac":
        keys = AC_KEYS
    elif drivce_type == "dvd":
        keys = DVD_KEYS
    elif drivce_type == "stb":
        keys = STB_KEYS
    t = threading.Thread(target=onFireEnter)
    t.setDaemon(True)  
    t.start()
    for key in keys:
        while True:
            Listener.input = 'XXXXXXXXX'
            irreader = Listener()
            print key
            irreader.run()
            
            if irreader.data_wave_len > 0:
                uespulse = ",".join(map(str,irreader.data_wave_buf))
                print irreader.data_wave_freq, '|', uespulse
                print
                
            while True:
                if Listener.input in ['n', 'r', '']:
                    break
                time.sleep(1)
            if Listener.input in ['n', '']:
                if irreader.data_wave_len > 0:
                    #codes.append("000000|%s|Full_Repeat|%s|%s|" % (data[0], key, data[1]))
                    uespulse = ",".join(map(str,irreader.data_wave_buf))
                    codes.append("000000|%d|Full_Repeat|%s|%s|%d|%d|%s|%s|" % (irreader.data_wave_freq, key, uespulse,
                        irreader.data_sys_code, irreader.data_data_code, irreader.data_format, irreader.data_full_code))
                    short_codes.append("000000|%d|Full_Repeat|%s|%s|" % (irreader.data_wave_freq, key, uespulse))
                break
    
    print "Input the filename:" 
    while True:
        if Listener.input:
            fp = open(Listener.input, "w")
            fp.write("\n".join(codes))
            fp.close()
            fp = open(Listener.input + "_short", "w")
            fp.write("\n".join(short_codes))
            fp.close()
            break
        time.sleep(1)
    print "================copy end================"

