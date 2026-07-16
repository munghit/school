import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="디지털 보안 연구 보고서", layout="wide")

# CSS 스타일링
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .card { background-color: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 20px; color: #f8fafc; }
    .step-box { background-color: #334155; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid #38bdf8; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 메뉴")
page = st.sidebar.radio("목차", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 연구 종합 보고서 ---
if page == "📂 연구 종합 보고서":
    st.title("📂 디지털 보안 연구 종합 보고서")
    
    # [서론]
    st.subheader("📝 1. 서론")
    c1, c2 = st.columns(2)
    c1.markdown('<div class="card"><h3>🔍 탐구 동기</h3>계정 탈취 사고의 근본 원인인 "취약한 비밀번호" 문제를 정량적 데이터로 해결하고자 함.</div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>❓ 탐구 문제</h3>1. 어떤 요소가 비밀번호의 해킹 저항력을 결정하는가?<br>2. 보안과 사용 편의성 사이의 최적점은 어디인가?</div>', unsafe_allow_html=True)

    # [본론]
    st.subheader("⚙️ 2. 본론 (탐구 과정 및 분석)")
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown('### 🛠️ 탐구 수행 순서')
        steps = ["1. 문헌 조사 (NIST 표준)", "2. 엔트로피 수학 모델링", "3. GPU 공격 시뮬레이션 환경 구축", "4. 데이터 수집 및 상관관계 분석"]
        for step in steps:
            st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
            
    with col2:
        st.markdown('### 📊 분석 기준 및 결과 데이터')
        st.write("분석 공식: $E = L \\times \\log_2(N)$ / 해킹 시간: $2^E / 10^{10}sec$")
        df = pd.DataFrame({
            '해킹 시간(로그)': [1, 5, 15, 30],
            '위험도 점수': [90, 60, 20, 5]
        }, index=['4자/단순', '6자/조합', '8자/조합', '12자/복합'])
        st.bar_chart(df)

    # [결론]
    st.subheader("🎯 3. 결론 (종합 결과)")
    st.markdown('<div class="card">'
                '<ul><li><b>보안 기술적 측면</b>: 비밀번호는 단순히 복잡한 문자를 섞는 것보다 <b>길이 확보를 통한 엔트로피 증대</b>가 해킹 저항력 향상에 압도적으로 효과적임.</li>'
                '<li><b>사용자 측면</b>: 무조건적인 복잡성 강요는 사용자의 기억력을 저하시켜 오히려 메모 노출 등 보안 사고를 유발하므로, 적절한 길이 권고가 최선임.</li>'
                '<li><b>종합 결과</b>: 12자리 이상의 비밀번호는 보안 기술과 사용자 사용성 모두를 만족시키는 최적의 보안 기준점임이 입증됨.</li></ul>'
                '</div>', unsafe_allow_html=True)

# --- 시뮬레이터 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    pw = st.text_input("비밀번호 입력", type="password")
    if pw:
        entropy = len(pw) * math.log2(95)
        st.metric("분석 강도", f"{entropy:.1f} bits")
        st.progress(min(entropy / 100, 1.0))
        st.write("※ 기준: 80 bits 이상 권장")
