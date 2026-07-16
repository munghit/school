import streamlit as st
import math
import pandas as pd
import numpy as np

# 페이지 설정
st.set_page_config(page_title="보안 분석 대시보드", layout="wide")

# CSS: 단조로움을 깨는 입체감과 컬러 강조
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .metric-card { background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 15px; border: 1px solid #475569; }
    h1 { color: #38bdf8 !important; }
    h2, h3 { color: #e2e8f0 !important; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.markdown("### 🛠️ 대시보드 메뉴")
page = st.sidebar.radio("목차", ["📂 연구 프로젝트", "🛡️ 보안 분석 도구"])

if page == "📂 연구 프로젝트":
    st.title("📂 디지털 보안 엔트로피 분석")
    st.write("---")
    
    # [시각적 재미 1] 레이아웃을 이용한 3단 대시보드
    cols = st.columns(3)
    cols[0].metric("연구 대상", "비밀번호 보안", "NIST 준수")
    cols[1].metric("분석 핵심", "엔트로피(Entropy)", "무작위성")
    cols[2].metric("기반 공격", "Brute Force", "10^10 H/s")
    
    st.write("## 📜 연구의 흐름")
    # [시각적 재미 2] 시각적인 단계별 흐름도
    st.info("💡 1단계: 문헌 조사 ➔ 2단계: 수학적 모델 구축 ➔ 3단계: 파이썬 알고리즘 구현 ➔ 4단계: 실시간 시뮬레이션")
    
    # [시각적 재미 3] 데이터 시각화 차트 (가상 데이터)
    st.subheader("📊 복잡도에 따른 해킹 난이도 변화")
    chart_data = pd.DataFrame(np.random.randn(20, 1).cumsum(axis=0), columns=['Security Difficulty'])
    st.area_chart(chart_data)

elif page == "🛡️ 보안 분석 도구":
    st.title("🛡️ 실시간 보안 분석 엔진")
    
    # [시각적 재미 4] 입력 창 분할
    col_input, col_info = st.columns([2, 1])
    with col_input:
        password = st.text_input("분석할 비밀번호를 입력하세요:", type="password")
    
    if password:
        entropy = len(password) * math.log2(95)
        # 결과 대시보드
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        c1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        c2.metric("위험도 점수", "High" if entropy < 60 else "Low")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # [시각적 재미 5] 프로그레스 바를 활용한 직관적 피드백
        st.write("### 보안 수준")
        st.progress(min(entropy / 100, 1.0))
        
        if entropy > 80: st.success("✅ 최고 보안 등급: 해독 불가 수준")
        elif entropy > 50: st.warning("⚠️ 보통 보안 등급: 문자 조합 추가 권장")
        else: st.error("🚨 위험: 즉시 변경 권장")
