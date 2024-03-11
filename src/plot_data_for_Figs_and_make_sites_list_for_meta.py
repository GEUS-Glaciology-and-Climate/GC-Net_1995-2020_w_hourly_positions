#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:20:05 2024

@author: jason
"""

from glob import glob
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------- chdir
if os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/AWS/GCNET/GC-Net_1995-2020_w_hourly_positions/'

os.chdir(base_path)

files=glob('./data/*')


# print(files)

sites=[]
n_hours=[]

varnames=['longitude, deg', 'latitude, deg N', 'elevation above mean sea-level, m',
          'air-T ~1.5 m TA1, C', 'air-T ~3.7 m TA2, C', 'air-T ~1.5 m TA3, C', 'air-T ~3.7 m TA4, C',
          'rel.-humidity RH1 ~1.5 m, %', 'rel.-humidity RH2 ~3.7 m, %', 'wind-speed 1 VW1. m/s',
       'wind-speed 2 VW2, m/s', 'wind direction 1 DW1, deg true', 'wind direction 2 DW2.deg true', 'surface air pressure P, hPA']
for st,file in enumerate(files):
    # if st==0:
    if st>=0:
        fn=file.split(os.sep)[-1]
        df=pd.read_csv(file)
        df["time"] = pd.to_datetime(df['date'])
        df.index = pd.to_datetime(df.time)

        n_hours.append(len(df))
        site_name =fn.split('_')[0]
        sites.append(site_name)
        print(st,site_name)

        do_plot=1
        
        if do_plot:
            plt.close()
            plt.clf()
            N=len(df.columns[1:])
            fig, ax = plt.subplots(N-1,figsize=(9,20))
            for vv,var in enumerate(df.columns[1:-1]):
                # print(var)
                
                ax[vv].plot(df[var],label=var)
                ax[vv].legend()
                if vv==0:
                    ax[vv].set_title(fn.split('_')[0]+' '+str(len(df))+' hourly averages')
                ax[vv].set_ylabel(varnames[vv].replace(' ','\n'))
            # # ax.set_xlim(t0,t1+timedelta(hours=6))
            # plt.setp(ax[cc].xaxis.get_majorticklabels(), rotation=90,ha='center',fontsize=fs)
            # # ax.set_xlim()
            # ax[cc].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
            plt.subplots_adjust(wspace=0, hspace=0)
            ly='p'
            if ly == 'x':plt.show()
         
            if ly == 'p':
                figname='./Figs/'+site_name+'.png'
                plt.savefig(figname, bbox_inches='tight', dpi=200)
                
#%%
df=pd.DataFrame({
    'site':np.array(sites),
    'N_hours':np.array(n_hours),
    'N_years':np.array(n_hours)/8760,
                  })

df.to_csv('./meta/sites.csv')