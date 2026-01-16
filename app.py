# 배포를 할 때 가장 첫 번째로 실행되는 파일! 이름은 내가 원하는 대로 지어도 상관없음.
import streamlit as st
import pandas as pd # 그래프 그려주는 라이브러리
import matplotlib.pyplot as plt # 차트를 더 이쁘게 그려주는 라이브러리
import seaborn as sns # 차트를 더 이쁘게 그려주는 라이브러리
import numpy as np # 수학적 계산을 도와주는 라이브러리
import platform # 운영체제 확인 라이브러리

# -----------------------------------------------------------------------------------
# 한글 폰트 설정 (그래프에서 한글이 깨지지 않도록 설정)
# -----------------------------------------------------------------------------------
system_name = platform.system()
if system_name == 'Windows':
    plt.rc('font', family='Malgun Gothic') # 윈도우
elif system_name == 'Darwin':
    plt.rc('font', family='AppleGothic') # 맥
else:
    plt.rc('font', family='NanumGothic') # 리눅스(코랩 등)

plt.rc('axes', unicode_minus=False) # 마이너스 기호 깨짐 방지

# pip install streamlit pandas matplotlib seaborn numpy -> 터미널에 입력해서 여러 라이브러리 설치
# requirements.txt 파일 만들어서 라이브러리 관리 -> pip install -r requirements.txt

st.title('📊국세청 근로소득 데이터 분석기')

# 데이터 불러오기
file_path = '국세청_근로소득 백분위(천분위) 자료_20241231.csv' # 데이터 파일 경로! 변수명 = '파일 경로'
# file_path = './data(폴더명)/국세청_근로소득 백분위(천분위) 자료_20241231.csv' # 폴더로 관리할 때 './폴더명/파일명.csv' 로 관리
# file_path = '../국세청_근로소득 백분위(천분위) 자료_20241231.csv' # 하위 폴더에서 상위 폴더의 데이터 관리할 때 '../파일명.csv' 로 관리


# 혹시모를 오류에 대한 대비
try : 
    # 자료 읽기
    df = pd.read_csv(file_path, encoding='euc-kr') # 한글 깨짐 방지 인코딩, file_path를 csv로 판다스에서 읽기
    st.success('데이터가 성공적으로 불러와졌습니다!') # 데이서 읽어오는 것 성공했을 때.

    # 데이터 미리보기
    st.subheader('📈데이터 미리보기') # 서브 타이틀
    st.dataframe(df.head(10)) # 데이터프레임의 앞에서 10개 행 미리보기, 디폴트는 5개 행

    # 데이터 분석 그래프 그리기
    st.subheader('📈항목별 분포 그래프') # 서브 타이틀
    #분석하고 싶으 열 이름을 선택하도록 할게요
    # 급여나 인원 같은 숫자 데이터가 있는 칸을 고를 수 있도록 함.
    col_names = df.columns.tolist() # 데이터프레임의 열 이름들을 리스트로 변환
    selected_col = st.selectbox('분포를 보고 싶은 항목을 선택하세요', col_names) # 첫 번째 열(백분위)은 제외하고 선택박스 생성

    # 그래프 그리기(seaborn 활용)
    fig, ax = plt.subplots(figsize=(10, 5)) # figsize -> 차트의 가로 세로 비율. fig = 전체 도화지, ax = 그래프가 그려질 영역
    sns.histplot(df[selected_col],kde=True, ax=ax, color='#cc00ff') 
    # seaborn 히스토그램 그리기, ax영역은 위에서 지정한 ax, 바 색 '#16진법'. kde=True는 밀도추정선 그리기
    plt.title(f'[{selected_col}] 분포 확인') # 그래프 제목
    plt.xlabel(selected_col) # x축 라벨
    plt.ylabel('빈도수') # y축 라벨

    # 그래프를 스트림릿에 표시
    st.pyplot(fig) # 스트림릿에 fig(도화지)를 그리기

except FileNotFoundError:
    # 파일 불러오기 실패 시
    st.error(f'{file_path} 파일을 찾을 수 없습니다. 파일 경로를 확인해주세요.')
except Exception as e:
    # syntax 에러 
    st.error(f'데이터를 불러오는 중 오류가 발생했습니다: {e}')

