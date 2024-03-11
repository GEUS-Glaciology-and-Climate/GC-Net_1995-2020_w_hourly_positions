#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 11:17:34 2024

@author: jason

This code merges a) horizontally-interpolated positions from certain AWS with b) time-variable elevations estimated from a variety of data sources and c) AWS meteorological data useful for e.g. atmospheric reanalysis data assimilation

like the script name says:
    merge_positions_incl_elev_with_met_data
    
Baptiste had already created position_interpolated files that ./GCNet_positions/analyze_AWS_elevs_including_ATM_v4.py reads and outputs 

"""


import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
from glob import glob
# import datetime
import os
L1_path = '/Users/jason/Dropbox/AWS/GCNET/GC-Net-level-1-data-processing/L1/hourly/'
files = sorted(glob(L1_path+'*'))
from os import path
import nead

n_stations=len(files)

#%%
# two meta data files needed
meta0 = pd.read_csv('/Users/jason/Dropbox/AWS/GCNET/GC-Net-level-1-data-processing/L1/GC-Net_location.csv',header=0)
meta=pd.read_excel('/Users/jason/Dropbox/AWS/GCNET/GCNet_positions/data/GC-Net locations and numbers 2014 modified.xlsx')

sites=meta['Station Name']
nicknames=meta['nickname']
meta.columns
   
fn='/Users/jason/Dropbox/AWS/GCNET/ancillary/varnames_all.txt'
info=pd.read_csv(fn, header=None, delim_whitespace=True)
info.columns=['id','varnam']
#%%
# -------------------------------- chdir
if os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/AWS/GCNET/GC-Net_1995-2020_w_hourly_positions/'

os.chdir(base_path)

# monthly means 

# sites=meta.Name.values
# sites=info_all.name.values

# sites=['CP1']

# for st,site in enumerate(sites):
for site, ID,nickname in zip(meta['Station Name'],meta.Station,nicknames):
    # if site!='null':
    # if site=='NASA-E':
    # if site=='NASA-SE':
    # if site=='Summit':
    # if nickname=='JAR':

    # if site=='Saddle':
    # if site=='Swiss Camp':
    # if site=='South Dome':
        # print(ID)
    if ID>=24:
    # if ID>8:
    # if ID==9:
        # df=pd.read_csv('./output/swc_air_t_1990-2021.csv')
        # print(site)
        # fn=L1_path+str(info_all['Station Number'][st].astype(int)).zfill(2)+'-'+site+'.csv'
        # print(fn)
        # print('# '+str(ID)+ ' ' + site)
        filename = L1_path+site.replace(' ','')+'.csv'
        print(ID,site)
        print(filename)
        
        # filename = L1_path+str(ID).zfill(2)+'-'+site+'.csv'
        if not path.exists(filename):
            print('Warning: No file for station '+str(ID)+' '+site)
            continue

        if path.exists(filename):
        
            ds = nead.read(filename)
            df = ds.to_dataframe()
            df=df.reset_index(drop=True)
            df[df == -999] = np.nan
            df['time'] = pd.to_datetime(df.timestamp)
            df = df.set_index('time')
    
            print(df.columns)
            df[df==999]=np.nan
            
            df['year'] = df.index.year
            df['month'] = df.index.month
            df['doy'] = df.index.dayofyear
    
            df.columns
            
            fn=f'/Users/jason/Dropbox/AWS/GCNET/GCNet_positions/output/{site}_position_interpolated_with_elev.csv'
            if site=='SwissCamp10m':
                fn='/Users/jason/Dropbox/AWS/GCNET/GCNet_positions/output/Swiss Camp_position_interpolated_with_elev.csv'
            if site=='Crawford Point1':
                fn='/Users/jason/Dropbox/AWS/GCNET/GCNet_positions/output/Crawford Pt. 1_position_interpolated_with_elev.csv'

            if not path.exists(fn):
                df_pos=df.copy()
                if site!='EastGRIP':
                    df_pos=df[['timestamp','TS1']]
                else:
                    df_pos=df[['timestamp','SZA']]
                meta0.columns
                v=np.where(ID==meta0.ID)
                df_pos['lat']=np.nan
                df_pos['lat']=meta0['Latitude (°N)'][v[0][0]]
                df_pos['lon']=meta0['Longitude (°E)'][v[0][0]]
                xpos=pd.read_csv(f'/Users/jason/Dropbox/AWS/GCNET/GCNet_positions/output/{site}_position_info.csv')
                df_pos['elev']=np.mean(xpos.elev_approximation)
                df_pos['date']=df_pos['timestamp']

            if path.exists(fn):      
                df_pos=pd.read_csv(fn)
            
            df_pos['time'] = pd.to_datetime(df_pos.date)
            df_pos = df_pos.set_index('time')
            df_pos['year'] = df_pos.index.year
            # df_pos['month'] = df_pos.index.month
            df_pos['doy'] = df_pos.index.dayofyear
    
            df_pos.columns
            
            
            df_subset=df[['TA1', 'TA2', 'TA3', 'TA4', 'RH1',
                   'RH2', 'VW1', 'VW2', 'DW1', 'DW2', 'P']]
            tol = pd.Timedelta('5 minute')
            df_merged=pd.merge_asof(left=df_subset,right=df_pos,right_index=True,left_index=True,direction='nearest',tolerance=tol)
    
            ofile=f'./data/{site}_w_hourly_positions.csv'
            
            df_merged.columns
            df_merged.to_csv(ofile,columns=['date', 'lon', 'lat', 'elev','TA1', 'TA2', 'TA3', 'TA4', 'RH1',
                   'RH2', 'VW1', 'VW2', 'DW1', 'DW2', 'P'],index=None)


