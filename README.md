# GC-Net_1995-2020_w_hourly_positions
'historical' GC-Net data 1995 to 2020 with (in certain cases*) variable elevation and/or lat lon

![map GC-Net sm](https://github.com/GEUS-Glaciology-and-Climate/GC-Net_1995-2020_w_hourly_positions/assets/32133350/3493e389-2868-44f9-894f-fd890c389492)

since-1990s Greenland automatic weather station (AWS) data for reanalysis assimilation.

Here implemented are estimates of the time-dependence of site elevation and horizontal position (lat, lon) for Greenland AWS.

Site displacements are up to 4 km in 33 years. 

Some sites high up on the ice sheet, several near the ice divide, here are given constant positions; a decent approximation for the time dependence of their position.

While the change in the lat, lon, elevation is not large from day to day, the position data are nonetheless provided hourly.

Code here merges a) horizontally-interpolated positions from certain AWS with b) time-variable elevations estimated from a variety of data sources and c) AWS meteorological data useful for e.g. atmospheric reanalysis data assimilation

building on data, sourced from [QC'd hourly AWS data](https://github.com/GEUS-Glaciology-and-Climate/GC-Net-level-1-data-processing/tree/main/L1/hourly) and [interpolated horizontal positions](https://github.com/GEUS-Glaciology-and-Climate/GCNet_positions/tree/main/output) using
[this code](https://github.com/GEUS-Glaciology-and-Climate/GCNet_positions/blob/main/analyze_AWS_elevs_including_ATM_v4.py)
