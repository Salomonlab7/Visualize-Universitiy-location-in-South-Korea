import folium

# 1. 지도 생성 (상명대학교가 잘 보이도록 서울 중심 근처로 설정)
map = folium.Map(location=[37.6026, 126.9552], zoom_start=9)

# 2. 상명대학교 서울캠퍼스 마커만 생성
marker = folium.Marker([37.6026315, 126.955252], 
                       popup='상명대학교 서울캠퍼스', 
                       icon=folium.Icon(color='red'))

# 3. 지도에 마커 등록
marker.add_to(map)

# 4. 파일 저장
map.save(r'C:\Users\Gyuhwang Choi\Desktop\전국 대학교 위치 시각화하기\uni_map.html')

print("상명대학교 마커만 포함된 지도가 저장되었습니다.")
