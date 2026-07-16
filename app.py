import streamlit as st
import math
import pandas as pd
import numpy as np

st.set_page_config(page_title="보안 연구 분석", layout="wide")

# CSS: 직관적인 카드 및 차트 색상 설정
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .main-card { background-color: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 20px; }
    h1, h2, h3 { color: #38bdf8 !important; }
    .metric-text { font-size: 1.2rem; color: #cbd5e1; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 대시보드 내비게이션")
page = st.sidebar.radio("목차", ["📊 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 연구 종합 보고서 ---
if page == "📊 연구 종합 보고서":
    st.title("📂 디지털 보안 강화를 위한 비밀번호 엔트로피 분석")
    st.markdown("---")

    # [서론]
    st.subheader("📝 1. 서론 (연구 동기)")
    st.markdown('<div class="main-card">디지털 계정 해킹 사고의 80% 이상은 취약한 비밀번호에서 기인합니다. '
                '단순한 길이 제한 가이드라인을 넘어, 실제 컴퓨팅 성능을 반영한 <b>"해킹 저항력(Entropy)"</b>을 정량적으로 평가하여 '
                '사용자의 능동적인 보안 습관을 형성하는 것이 본 연구의 핵심 목표입니다.</div>', unsafe_allow_html=True)

    # [본론]
    st.subheader("⚙️ 2. 본론 (연구 수행 및 분석)")
    c1, c2 = st.columns([1, 1.5])
    
    with c1:
        st.markdown('### 🛠️ 수행 단계')
        # 단계별 직관적 표시
        for step in ["✅ 1단계: 문헌 조사 (NIST 표준)", "✅ 2단계: 수학적 모델 정립", "✅ 3단계: 파이썬 시뮬레이터 개발", "🔄 4단계: 보안성 정량 분석"]:
            st.markdown(f"**{step}**")
            
    with c2:
        st.markdown('### 📉 보안 강도 vs 해킹 난이도 시각화')
        # 그래프 의미 명시
        data = pd.DataFrame({'해킹 소요 시간(로그)': np.logspace(1, 10, 20)})
        st.line_chart(data)
        st.caption("그래프 설명: 비밀번호 조합(엔트로피)이 증가함에 따라 해킹에 필요한 시간(연산 횟수)이 지수 함수적으로 급증함을 나타냅니다.")

    # [결론]
    st.subheader("🎯 3. 결론 (결과 요약)")
    st.markdown('<div class="main-card">'
                '<ul><li><b>보안 원리</b>: 비밀번호 길이를 1자 늘릴 때마다 해킹 난이도는 약 95배 증가합니다.</li>'
                '<li><b>실무 적용</b>: 12자리 이상의 복합 문자 비밀번호는 현대 GPU 연산 성능으로도 수백 년 이상 소요됩니다.</li>'
                '<li><b>의의</b>: 본 시뮬레이터는 정량적 수치를 제시하여 사용자에게 강력한 경각심과 실질적 가이드를 제공합니다.</li></ul>'
                '</div>', unsafe_allow_html=True)

# --- 시뮬레이터 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    password = st.text_input("비밀번호 입력", type="password")
    if password:
        entropy = len(password) * math.log2(95)
        st.metric("분석된 엔트로피(bits)", f"{entropy:.1f}")
        st.progress(min(entropy / 100, 1.0))
        st.write("※ 결과: 엔트로피가 80 bits 이상일 때 현대 공격 기술로 해독이 매우 어렵습니다.")
