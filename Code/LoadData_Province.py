
import pandas as pd
import requests
import json
from pprint import pprint
import pandas as pd
import os
import errno

province_dict = {
    'Country': None,
    'City': None,
    'City (ASCII)': None,
    'Region': None,
    'Region (ASCII)': None,
    'Population': None,
    'Longitude': None,
    'Latitude': None,
    'Time Zone': None,
}

hourly_data = {
    'Year':None,
    'Month': None,
    'Day':None, 
    'UTC Hour':None,
    'PM2.5':None, 
    'PM10_mask':None,
    'Retrospective':None 
}


def read_dust_txt_file(file):  
    pv_detail = province_dict.copy()
    d = hourly_data.copy()
    dust_data = pd.DataFrame()
    #continue parameters or start
    if not os.path.exists(os.path.dirname("Data_Pravince/")):
        try:
            os.makedirs(os.path.dirname("Data_Pravince/"))
            print("Create : Data_Pravince/   (Done)")
        
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    line_list = file.split("\n")
    for line in line_list[0:9]:
        col,value = line.split(":")
        pv_detail[col[2:]] = value.strip()
        print(line)

    for line in line_list[10:-1]:
        d = hourly_data.copy()
        #print(line)
        (d['Year'],d['Month'],d['Day'],d['UTC Hour'],d['PM2.5'],  
        d['PM10_mask'],d['Retrospective']) = line.split("\t") 
        dust_data = dust_data.append(d,ignore_index=True)
   
    return pv_detail , dust_data



data_all_province = pd.DataFrame();
province_list = ['Chiang_Rai','Chiang_Mai','Lampang','Bangkok']
for province in province_list:
    p = province_dict.copy()
    url2 = f'http://berkeleyearth.lbl.gov/air-quality/maps/cities/Thailand/{province}/{province}.txt' #แสดงค่าที่ได้จากจุดตรวจวัดล่าสุด
    params = { }
    response = requests.request('GET', url2 ,params=params)
    in_txt = response.text.split("\n") 
    (p,hour_data) = read_dust_txt_file(response.text)
    
    hour_data.to_csv('Data_Pravince/'+province + '_data.csv')
    data_all_province = data_all_province.append(p, ignore_index=True)
    print('='*20)
data_all_province.to_csv('Data_Pravince/data_all_province.csv')


