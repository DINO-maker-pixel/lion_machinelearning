# streamlit에 쓸 파일
# ml은 colab
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pickle

st.title("MachineLearning")
# git switch -c 브랜치명 (브랜치 생성하면서 바로 그 브랜치로 넘어간다)
st.header("캘리포니아 집값 예측 프로그램")
cols = [ 'MedInc','HouseAge','AveRooms','AveBedrms', 'Population','AveOccup','Latitude','Longitude']
datas = [0]*8
for idx, col in enumerate(cols):
    data[idx] = st.number_input(col)
x = np.array(datas).reshape(1, -1)
x.shape

with open("rf_housing.pickle", "rb") as f:
    rf_model = pickle.load(f)

y = rf_model.predict(x)

# https://github.com/likelionbe12/lion_machinelearning.git 포크
# 여러분의 깃허브로 가셔서 lion_machinelearning 레포를 확인
# 여러분의 레포를 클론

# git branch - 현재 브랜치 확인
# git branch feature_ml - feature_ml 이름의 브랜치 생성
# git checkout feature_ml - feature_ml로 전환
# 코드에 기업명을 넣을 수 있는 컴포넌트 하나 추가
# 확인
# git add .
# git commit -m "커밋메시지"
# git checkout main - main브랜치로 이동
# git merge feature_ml - feature_ml코드를 main에 병합
# git push