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
from os import path
import nead


# -------------------------------- chdir
if os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/AWS/GCNET/GC-Net_1995-2020_w_hourly_positions/'

os.chdir(base_path)


base_dir = '/Users/jason/Dropbox/AWS/GCNET/GC-Net-level-1-data-processing/L1/hourly/'
files = sorted(glob(base_dir+'*'))
n_stations=len(files)

sites_original_convention=[
# "gits",
"HUM",
"PET",
"TUNU-N",
"Swiss Camp 10m",
# "swisscamp",
# "crawfordpoint",
"NAU",
"Summit",
"DYE2",
# "jar1",
# "saddle",
"SouthDome",
"NAE",
# "nasa_southeast",
"NEEM",
"E-GRIP"
]

th=1 ; fs=16
plt.rcParams["font.size"] = fs
plt.rcParams['axes.facecolor'] = 'w'
plt.rcParams['axes.edgecolor'] = 'k'
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
plt.rcParams["legend.facecolor"] ='w'
plt.rcParams["mathtext.default"]='regular'
plt.rcParams['grid.linewidth'] = th
plt.rcParams['axes.linewidth'] = th #set the value globally
plt.rcParams['figure.figsize'] = 17, 10
fg='k' ; bg='w'


name_alias = {'DY2': 'DYE2', 'CP1':'Crawford Point 1'}

site_list = pd.read_csv('/Users/jason/Dropbox/AWS/GCNET/GCN_albedo/metadata/GC-Net_location_w_nickname.csv',header=0)

fn='/Users/jason/Dropbox/AWS/GCNET/ancillary/varnames_all.txt'
info=pd.read_csv(fn, header=None, delim_whitespace=True)
info.columns=['id','varnam']
# print(info.columns)
# print(info.varnam)

# # ----------------------------------------------------------
# meta = pd.read_csv('/Users/jason/Dropbox/AWS/_merged/PROMICE_GC-Net_info.csv')
# meta = meta.rename({'stid': 'name'}, axis=1)
# meta.name_short
# names=meta.name_short

varsx=info.varnam[3:47]
varsx=info.varnam[3:29]
n_vars=len(varsx)


# print(files)

sites=[]
n_hours=[]

varnames=['longitude', 'latitude', 'elevation',
          'TA1', 'TA2', 'TA3', 'TA4','RH1',
                 'RH2', 'VW1', 'VW2', 'DW1', 'DW2', 'HW1', 'HW2', 'P']

varnames_out=['longitude', 'latitude', 'elevation',
          'T1', 'T2', 'RH1',
                 'RH2', 'VW1', 'VW2', 'DW1', 'DW2', 'HW1', 'HW2', 'P']

# Index(['timestamp', 'ISWR', 'OSWR', 'NR', 'TA1', 'TA2', 'TA3', 'TA4', 'RH1',
#        'RH2', 'VW1', 'VW2', 'DW1', 'DW2', 'P', 'HW1', 'HW2', 'V', 'TA5', 'TS1',
#        'TS2', 'TS3', 'TS4', 'TS5', 'TS6', 'TS7', 'TS8', 'TS9', 'TS10', 'IUVR',
#        'ILWR', 'Tsurf1', 'Tsurf2', 'HW1_adj_flag', 'HW2_adj_flag',
#        'OSWR_adj_flag', 'NR_cor', 'HS1', 'HS1_adj_flag', 'HS2', 'HS2_adj_flag',
#        'HS_combined', 'SHF', 'LHF', 'TA2m', 'RH2m', 'VW10m', 'SZA', 'SAA',
#        'Alb', 'RH1_cor', 'Q1', 'RH2_cor', 'Q2', 'latitude', 'longitude',
#        'elevation', 'DTS1', 'DTS2', 'DTS3', 'DTS4', 'DTS5', 'DTS6', 'DTS7',
#        'DTS8', 'DTS9', 'DTS10', 'TS_10m', 'year', 'month', 'day', 'doy'],

# varnames2=['longitude, °', 'latitude, ° N', 'elevation above mean sea-level, m',
#           'air-T ~1.5 m, °C', 'air-T ~3.7 m, °C', 'air-T ~1.5 m, °C', 'air-T ~3.7 m, °C',
#           'rel.-humidity ~1.5 m, %', 'rel.-humidity ~3.7 m, %', 'wind-speed 1, m/s',
#         'wind-speed 2, m/s', 'wind direction 1, deg true', 'wind direction 2, deg true', 'surface air pressure P, hPA']

# varnames3=['longitude °', 'latitude ° N', 'elevation above mean sea-level m',
#           'air-T 1 °C', 'air-T 2 °C',
#           'rel.-humidity 1 %', 'rel.-humidity 2 %', 'wind-speed 1 m/s',
#        'wind-speed 2 m/s', 'wind direction 1 deg true', 'wind direction 2 deg true', 'instrument heigh 1 m','instrument heigh 2 m','surface air pressure P hPA']

N=len(varnames)
# len(varnames3)

# for st,site in enumerate(sites):
for st,(site, ID )in enumerate(zip(site_list.Name,site_list.ID)):
    print(st)
    
    site=site.replace(' ','')
    # if site!='null':
    # if site=='NASA-E':
    # if site=='Summit':
    # if site=='Tunu-N':
    # if site=='SwissCamp':
    # if site=='SwissCamp10m':
    # if site=='DYE-2':
    # if site=='SouthDome':
    #     print(ID)
    if st>=0:
    # if ID==12:
        # # -------------------------------- loop years
        # for yy in range(n_years):
        #     yearx=yy+i_year
        #     print(site,yearx)
        #     n_days=365
        #     if calendar.isleap(yearx):
        #         n_days=366
    
        #     # if yearx==2012:
        #     # if yearx==2018:

        #     if yearx>=209:

        # site='swisscamp'
        # df=pd.read_csv('./output/swc_air_t_1990-2021.csv')
        # print(site)
        # fn=base_dir+str(info_all['Station Number'][st].astype(int)).zfill(2)+'-'+site+'.csv'
        # print(fn)
        # print('# '+str(ID)+ ' ' + site)
            filename = base_dir+site+'.csv'
            # filename = base_dir+site+'.csv'
            print(filename)
            if not path.exists(filename):
                print('Warning: No file for station '+str(ID)+' '+site)
                continue
            ds = nead.read(filename)
            df = ds.to_dataframe()
            df=df.reset_index(drop=True)
            df[df == -999] = np.nan
            df['T1'] = df[['TA1', 'TA3']].mean(axis=1).values
            df['T2'] = df[['TA2', 'TA4']].mean(axis=1).values
            df['time'] = pd.to_datetime(df.timestamp)
            # df['date'] = pd.strftime(df['time'],'%Y')
            df = df.set_index('time')
    
            # print(df.columns)
            df[df==999]=np.nan
            
            df['year'] = df.index.year
            df['month'] = df.index.month
            df['day'] = df.index.day
            
            # df.columns
            # df['doy'] = df.index.dayofyear



            # for oldName,newName in zip(varnames,varnames3):
            #     oldName,newName
            #     df = df.rename(columns={oldName: newName})
            
            vals=['T1','T2']
                  
            for val in vals:
                df[val] = df[val].map(lambda x: '%.2f' % x)

            df.to_csv(f'/Users/jason/Dropbox/AWS/GCNET/GC-Net_1995-2020_w_hourly_positions/data/GC-Net_historical_data_for_assimilation/{site}.csv',
                      columns=varnames_out)
            
            do_plot=0
            
            if do_plot:
                for yy in np.arange(np.min(df.year),np.max(df.year)+1):
                    dfx=df[df.year==yy]
                    print(site,yy)
                    n_hours.append(len(dfx))
                    # site_name =fn.split('_')[0]
                    # sites.append(site_name)
                    # print(st,site_name)
            
    
                    plt.close()
                    plt.clf()
                    fig, ax = plt.subplots(len(varnames),figsize=(12,20))
                    for vv,var in enumerate(varnames):
                        # print(yy,var,',',varnames3[vv])
                        # #%%
                        ax[vv].plot(dfx[var],label=var)
                        ax[vv].legend()
                        if vv==0:
                            ax[vv].set_title(site+' '+str(len(dfx))+' hourly averages, year '+str(yy))
                        ax[vv].set_ylabel(varnames[vv])
                        # ax[vv].set_ylabel(varnames[vv].replace(' ','\n'))
                    # # ax.set_xlim(t0,t1+timedelta(hours=6))
                    plt.setp(ax[vv].xaxis.get_majorticklabels(), rotation=90,ha='center',fontsize=fs)
                    # # ax.set_xlim()
                    # ax[cc].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
                    plt.subplots_adjust(wspace=0, hspace=0)
                    ly='p'
                    if ly == 'x':plt.show()
                 
                    if ly == 'p':
                        figname=f'./Figs/{site}_{yy}.png'
                        plt.savefig(figname, bbox_inches='tight', dpi=100)
# #%%
# df=pd.DataFrame({
#     'site':np.array(sites),
#     'N_hours':np.array(n_hours),
#     'N_years':np.array(n_hours)/8760,
#                   })

# df.to_csv('./meta/sites.csv')