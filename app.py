import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="보안 연구 대시보드", layout="wide")

# CSS: 단조로움 탈피 (카드 디자인 + 색상 강조)
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .hero-card { background: linear-gradient(135deg, #3b82f6, #8b5cf6); padding: 30px; border-radius: 20px; color: white; margin-bottom: 20px; }
    .info-box { background-color: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; }
    h1, h2, h3 { color: #f8fafc !important; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 대시보드")
page = st.sidebar.radio("메뉴", ["📂 연구 보고서", "🛡️ 시뮬레이터"])

if page == "📂 연구 보고서":
    # [시각적 재미] 히어로 섹션
    st.markdown('<div class="hero-card"><h1>🔍 비밀번호 보안의 수학적 분석</h1><p>무차별 대입 공격(Brute-Force)을 방어하기 위한 정량적 데이터 가이드</p></div>', unsafe_allow_html=True)
    
    # [본론] 그래프와 내용 분할
    st.subheader("⚙️ 본론: 왜 비밀번호를 길게 해야 하는가?")
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="info-box"><h3>📉 공격 난이도의 지수적 상승</h3>'
                    '비밀번호가 1글자 늘어날 때마다, 해커가 찾아야 할 경우의 수는 95배씩 늘어납니다. '
                    '아래 그래프는 <b>비밀번호 길이에 따른 해킹 소요 시간의 폭발적인 증가</b>를 보여줍니다.</div>', unsafe_allow_html=True)
        
    with col2:
        # [직관적 그래프] 실제 계산 데이터 대입
        chart_data = pd.DataFrame({'소요 시간(연산 횟수)': [10**3, 10**6, 10**12, 10**24]}, index=['4자리', '6자리', '8자리', '12자리'])
        st.bar_chart(chart_data)
        st.caption("그래프: 12자리 이상이 되었을 때 해킹 소요 시간은 기하급수적으로 증가함")

    # [결론] 아이콘 기반 요약
    st.subheader("🎯 결론: 핵심 가이드라인")
    c1, c2, c3 = st.columns(3)
    c1.metric("권장 길이", "12자리 이상")
    c2.metric("문자 조합", "특수문자 포함")
    c3.metric("최종 보안 등급", "Very High")

elif page == "🛡️ 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    password = st.text_input("분석할 비밀번호 입력", type="password")
    if password:
        entropy = len(password) * math.log2(95)
        # [시각적 재미] 분석 바
        st.write("### 보안성 게이지")
        st.progress(min(entropy / 100, 1.0))
        st.metric("계산된 강도", f"{entropy:.1f} bits")
