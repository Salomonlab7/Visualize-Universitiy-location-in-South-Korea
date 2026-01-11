import pandas as pd
import requests
from openpyxl import load_workbook
from openpyxl import Workbook
import re

filePath = r'C:\Users\Gyuhwang Choi\Desktop\전국 대학교 위치 시각화하기\고등교육기관 하반기 주소록(2020).xlsx'
df_from_excel = pd.read_excel(filePath,engine='openpyxl')
df_from_excel.columns = df_from_excel.loc[4].tolist()
df_from_excel = df_from_excel.drop(index=list(range(0,5)))

def request_geo(address): #웹 보안키 
    clean_address = address.split('(')[0].strip()
    
    my_key = "8123CB17-C308-3459-AAD4-8ACACDC30F2B" #키 내용

    url = "https://api.vworld.kr/req/address?"
    

    params = {                            #좌표
        "service": "address",
        "request": "getcoord",
        "version": "2.0",
        "crs": "epsg:4326",
        "address": clean_address,
        "format": "json",
        "type": "ROAD",
        "key": my_key
    }

    response = requests.get(url, params=params) # 요청 보내삐
    json_data = response.json()

    
    if json_data.get('response', {}).get('status') == 'OK':  #결과 확인바리
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        # 에러 내용 출력
        print("API 응답 에러:", json_data.get('response', {}).get('error', {}).get('text'))
        return 0, 0

x, y = request_geo("서울특별시 종로구 홍지문2길 20 ") #실제 실행 코드
print(f"결과 좌표: x={x}, y={y}")

try:
    wb = load_workook(r"C:\Users\Gyuhwang Choi\Desktop\전국 대학교 위치 시각화하기\고등교육기관 하반기 주소록(2020).xlsx", data_only=True)
    sheet = wb.active
except:
    wb = Workbook()
    sheet = wb.active

university_list = df_from_excel['학교명'].to_list()
address_list = df_from_excel['주소'].to_list()

for num,value in enumerate(address_list):
    addr = re.sub(r'\(.*\)', '', str(value)).strip()
    print(addr)
    x,y = request_geo(addr)
    sheet.append([university_list[num],addr,x,y])

wb.save(r"C:\Users\Gyuhwang Choi\Desktop\전국 대학교 위치 시각화하기\고등교육기관 하반기 주소록(2020).xlsx")
