import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="보안 연구 대시보드", layout="wide")

# CSS: 직관적이고 전문적인 다크 테마 디자인
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .header-box { border-left: 5px solid #38bdf8; padding-left: 15px; margin-bottom: 20px; color: #f8fafc; }
    .card { background-color: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 20px; }
    h1 { color: #38bdf8 !important; }
    h2 { color: #ffffff !important; border-bottom: 2px solid #38bdf8; padding-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 대시보드 메뉴")
page = st.sidebar.radio("목차", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 연구 종합 보고서 ---
if page == "📂 연구 종합 보고서":
    st.title("📂 디지털 보안 연구: 비밀번호의 과학")
    
    # [서론]
    st.markdown("## 📝 1. 서론")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="header-box"><h3>🔍 탐구 동기</h3></div>', unsafe_allow_html=True)
        st.write("디지털 계정 탈취 사례의 대부분이 취약한 비밀번호 설정에서 비롯됨을 확인했습니다. 인간이 기억하기 쉬운 비밀번호가 컴퓨터에게는 얼마나 쉽게 뚫릴 수 있는지 정량적으로 확인하고자 본 연구를 시작했습니다.")
    with col2:
        st.markdown('<div class="header-box"><h3>❓ 탐구 문제</h3></div>', unsafe_allow_html=True)
        st.write("1. 비밀번호의 길이와 구성 요소가 보안 강도에 어떤 영향을 주는가?\n2. 현대적인 컴퓨팅 성능에서 '안전한 비밀번호'의 기준점은 어디인가?")

    # [본론]
    st.markdown("## ⚙️ 2. 본론 (탐구 과정)")
    col_a, col_b = st.columns([1, 1.5])
    with col_a:
        st.markdown('<div class="card"><b>Step 1. 표준 가이드라인 분석</b><br>NIST SP 800-63B 지침 연구</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><b>Step 2. 수학적 모델 설계</b><br>엔트로피 공식($E = L \\times \\log_2 N$) 수립</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><b>Step 3. 알고리즘 개발</b><br>Python 기반 해킹 소요 시간 산출 로직 구현</div>', unsafe_allow_html=True)
    with col_b:
        st.markdown('### 📉 길이 증가에 따른 해킹 난이도')
        chart_data = pd.DataFrame({'난이도(연산횟수)': [10**3, 10**6, 10**12, 10**24]}, index=['4자리', '6자리', '8자리', '12자리'])
        st.bar_chart(chart_data)

    # [결론]
    st.markdown("## 🎯 3. 결론 (탐구 결과)")
    c1, c2, c3 = st.columns(3)
    c1.metric("해킹 저항력", "12자리 이상 시 극대화")
    c2.metric("보안 핵심", "길이 > 단순조합")
    c3.metric("최종 결과", "안전 확보 가능")
    st.markdown('<div class="card"><b>탐구 결과 요약:</b> 비밀번호의 강도는 단순한 문자 조합보다 <b>"길이"</b>에서 비약적으로 상승합니다. 12자리 이상의 비밀번호는 현대 기술로도 해독에 수백 년이 소요되어 보안성이 매우 높음이 확인되었습니다.</div>', unsafe_allow_html=True)

# --- 시뮬레이터 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    pw = st.text_input("분석할 비밀번호 입력", type="password")
    if pw:
        entropy = len(pw) * math.log2(95)
        st.metric("분석된 강도", f"{entropy:.1f} bits")
        st.progress(min(entropy / 100, 1.0))
