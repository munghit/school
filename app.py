import streamlit as st
import math

# 페이지 설정
st.set_page_config(page_title="보안 연구 보고서", layout="wide")

# CSS 스타일 정의
st.markdown("""
<style>
    .stApp { background-color: #020617; color: #e2e8f0; font-family: 'Pretendard', sans-serif; }
    .main-card { background: #0f172a; padding: 30px; border-radius: 20px; border: 1px solid #1e293b; margin-bottom: 25px; }
    h1, h2, h3 { color: #38bdf8 !important; }
</style>
""", unsafe_allow_html=True)

# 사이드바 구성
st.sidebar.title("🧭 연구 목차")
menu = st.sidebar.radio("발표 섹션", [
    "서론: 연구 배경", 
    "본론 1: 이론적 배경", 
    "본론 2: 실태 및 문제점", 
    "본론 3: 해결 방안 및 구현", 
    "시뮬레이터: 보안 실증"
])

# 본문 내용 (삼중 따옴표 사용으로 SyntaxError 해결)
if menu == "서론: 연구 배경":
    st.title("🛡️ 디지털 보안 연구")
    st.markdown('''<div class="main-card">
        <h2>서론: 연구의 동기 및 목적</h2>
        <p>비밀번호는 인가된 사용자와 외부 침입자를 구분하는 가장 기본적인 방어선입니다. 
        본 연구는 KISA의 보안 가이드라인을 바탕으로, 데이터 기반 시뮬레이션을 통해 사용자가 
        보안성을 직접 체감하고 능동적인 보안 습관을 형성하도록 유도하는 데 목적이 있습니다.</p>
    </div>''', unsafe_allow_html=True)

elif menu == "본론 1: 이론적 배경":
    st.title("📖 이론적 배경")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('''<div class="main-card">
            <h3>1. 정보보호의 역할</h3>
            <p>비밀번호는 보안의 첫 번째 방어선입니다. 영문, 숫자, 특수문자의 혼합은 필수적인 보안 요구사항입니다.</p>
        </div>''', unsafe_allow_html=True)
    with c2:
        st.markdown('''<div class="main-card">
            <h3>2. 무차별 대입 공격</h3>
            <p>공격은 경우의 수에 좌우됩니다. 비밀번호의 길이(L)와 문자 집합(N)의 지수 함수적 관계(N^L)에 따라 해킹 난이도가 결정됩니다.</p>
        </div>''', unsafe_allow_html=True)

elif menu == "본론 2: 실태 및 문제점":
    st.title("⚠️ 관리 체계의 현황 및 문제점")
    st.markdown('''<div class="main-card">
        <h3>현황: 편리함과 보안 사이의 간극</h3>
        <p>KISA 실태조사에 따르면 다수의 사용자가 기억하기 쉬운 비밀번호를 여러 사이트에서 중복 사용하며, 보안 피로감을 느끼고 있습니다.</p>
    </div>''', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="main-card"><h3>기술적 취약성</h3>단순한 비밀번호는 무차별 대입 공격 및 사전 공격에 매우 취약합니다.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="main-card"><h3>사용자 인지 문제</h3>안전한 기준에 대한 체계적 정보 부족으로 인해 효과적인 비밀번호 수립에 어려움을 겪습니다.</div>', unsafe_allow_html=True)

elif menu == "본론 3: 해결 방안 및 구현":
    st.title("💡 혁신적 개선 방안 및 구현")
    st.markdown('''<div class="main-card">
        <h3>기술적 우수 사례</h3>
        <p>다중 인증(MFA), 비밀번호 관리자, 웹사이트별 강력한 정책 적용을 통해 보안성을 확보하고 있습니다.</p>
    </div>''', unsafe_allow_html=True)
    st.markdown('''<div class="main-card">
        <h3>개발 환경: Streamlit & GitHub</h3>
        <p>본 연구는 위 문제들을 해결하기 위해 <b>Streamlit</b>을 통해 <b>실시간 보안성 시뮬레이터</b>를 구축하였습니다.</p>
        <ul>
            <li><b>GitHub:</b> 코드 버전 관리 및 지속 가능한 프로젝트 개발 환경 구축</li>
            <li><b>Streamlit:</b> 사용자가 입력 즉시 수학적 엔트로피 기반 위험도를 직관적으로 확인</li>
            <li><b>교육적 효과:</b> '단순 암기'에서 '직접 체험'으로 보안 교육 패러다임 전환</li>
        </ul>
    </div>''', unsafe_allow_html=True)

elif menu == "시뮬레이션: 보안 실증":
    st.title("🛡️ 실시간 보안성 시뮬레이터")
    pw = st.text_input("🔑 비밀번호 입력", type="password")
    if pw:
        entropy = len(pw) * 5
        score = min(entropy, 100)
        st.markdown(f'<div class="main-card"><h3>분석 결과: {score}/100점</h3></div>', unsafe_allow_html=True)
        st.progress(score / 100)
