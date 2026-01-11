import requests

def request_geo(address):
    # 1. 주소 
    clean_address = address.split('(')[0].strip()
    
    # 2. API 키
    my_key = "8123CB17-C308-3459-AAD4-8ACACDC30F2B" 

    url = "https://api.vworld.kr/req/address?"
    
    # 3. 파라미터
    params = {
        "service": "address",
        "request": "getcoord",
        "version": "2.0",
        "crs": "epsg:4326",
        "address": clean_address,
        "format": "json",
        "type": "ROAD",
        "key": my_key
    }

    # 4. 요청 보내기
    response = requests.get(url, params=params)
    json_data = response.json()

    # 결과 확인
    if json_data.get('response', {}).get('status') == 'OK':
        x = json_data['response']['result']['point']['x']
        y = json_data['response']['result']['point']['y']
        return x, y
    else:
        # 에러 내용 출력
        print("API 응답 에러:", json_data.get('response', {}).get('error', {}).get('text'))
        return 0, 0

# 실행 테스트
x, y = request_geo("서울특별시 종로구 홍지문2길 20 ")
print(f"결과 좌표: x={x}, y={y}")
