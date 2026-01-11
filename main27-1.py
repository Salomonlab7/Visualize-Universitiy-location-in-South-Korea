import pandas as pd

# 엑셀 파일 경로
filePath = r'C:\Users\Gyuhwang Choi\Desktop\전국 대학교 위치 시각화하기\27. 전국의 대학교 위치 시각화하기\고등교육기관 하반기 주소록(2020).xlsx'

# 1. 엑셀 파일 읽기 (openpyxl 엔진 사용)
df_from_excel = pd.read_excel(filePath, engine='openpyxl')

# 2. 5번째 행(인덱스 4)을 가져와서 컬럼명으로 설정
df_from_excel.columns = df_from_excel.loc[4].tolist()

# 3. 데이터로 쓸 수 없는 상위 5개 행(0~4번 인덱스) 삭제
df_from_excel = df_from_excel.drop(index=list(range(0, 5)))

# 4. 결과 출력
print(df_from_excel.head())

print(df_from_excel['학교명'].values)

print(df_from_excel['주소'].values)
