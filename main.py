# streamlit에 쓸 파일
# ml은 colab
import streamlit as st

st.title("MachineLearning")
# git switch -c 브랜치명 (브랜치 생성하면서 바로 그 브랜치로 넘어간다)
st.header("네이버")

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