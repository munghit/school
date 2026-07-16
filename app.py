import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="보안 연구 대시보드", layout="wide")

# CSS: 디자인 요소 강화
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .section-header { color: #38bdf8; font-size: 1.5rem; font-weight: bold; margin-top: 20px; }
    .card { background-color: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 15px; }
    .white-text { color: #f8fafc; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 대시보드")
page = st.sidebar.radio("메뉴", ["📂 메인 분석 페이지", "🛡️ 시뮬레이터"])

if page == "📂 메인 분석 페이지":
    st.title("📂 디지털 보안 연구 분석")
    
    # --- 서론 ---
    st.markdown('<div class="section-header">📝 1. 서론 (연구 동기)</div>', unsafe_allow_html=True)
    st.markdown('<div class="card white-text">온라인 계정 탈취 사고의 80%는 단순한 비밀번호에서 발생합니다. 본 연구는 <b>엔트로피 이론</b>을 통해 비밀번호의 강도를 정량적으로 평가하고, 사용자에게 실질적인 보안 가이드를 제공하고자 합니다.</div>', unsafe_allow_html=True)
    
    # --- 본론 ---
    st.markdown('<div class="section-header">⚙️ 2. 본론 (핵심 분석)</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown('<div class="card white-text"><h3>📉 해킹 난이도의 변화</h3>'
                    '비밀번호가 4자리에서 12자리로 길어질 때, 해커가 뚫어야 할 경우의 수는 <b>지수적으로 급증</b>합니다. '
                    '옆의 그래프는 길이 증가에 따른 해킹 소요 시간의 폭발적인 증가를 보여줍니다.</div>', unsafe_allow_html=True)
    
    with col2:
        # 데이터프레임 형식 수정 (오류 방지)
        chart_df = pd.DataFrame({
            '난이도(연산횟수)': [1000, 1000000, 1000000000, 10000000000000]
        }, index=['4자리', '6자리', '8자리', '12자리'])
        st.bar_chart(chart_df)

    # --- 결론 ---
    st.markdown('<div class="section-header">🎯 3. 결론 (핵심 요약)</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("권장 길이", "12자 이상")
    c2.metric("문자 조합", "특수문자 필수")
    c3.metric("최종 보안성", "매우 높음")
    
    st.markdown('<div class="card white-text">결론적으로 비밀번호는 단순히 복잡하게 만드는 것이 아니라, <b>길이를 확보하는 것이 보안의 핵심</b>입니다.</div>', unsafe_allow_html=True)

elif page == "🛡️ 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    pw = st.text_input("비밀번호 입력", type="password")
    if pw:
        entropy = len(pw) * math.log2(95)
        st.metric("분석된 강도", f"{entropy:.1f} bits")
        st.progress(min(entropy / 100, 1.0))
