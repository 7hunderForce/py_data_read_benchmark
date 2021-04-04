import dask.dataframe as dd
import modin.pandas as mpd
import pandas as pd
import psutil
import ray
import time

data = r'C:\GitHub\modin_benchmark\data.csv' 

print('Initializing Ray...')
ray.init(num_cpus=psutil.cpu_count())

print('\n[MODIN / RAY]')
mpd_start = time.time()
mpd_data = mpd.read_csv(data)
mpd_end = time.time()
ray.shutdown()
mpd_time_diff = mpd_end - mpd_start
print(f'Start: {mpd_start}')
print(f'End: {mpd_end}')
print(mpd_time_diff)

print('\n[PANDAS]')
pd_start = time.time()
pd_data = pd.read_csv(data)
pd_end = time.time()
pd_time_diff = pd_end - pd_start
print(f'Start: {pd_start}')
print(f'End: {pd_end}')
print(pd_time_diff)


print('\n[DASK]')
dd_start = time.time()
dd_data = dd.read_csv(data)
dd_end = time.time()
dd_time_diff = dd_end - dd_start
print(f'Start: {dd_start}')
print(f'End: {dd_end}')
print(dd_time_diff)