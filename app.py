import streamlit as st
import math

# 페이지 설정
st.set_page_config(page_title="비밀번호 보안 연구", layout="wide")

# 사이드바 구성
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("목차", ["프로젝트 개요", "보안성 시뮬레이터"])

# 스타일 CSS (카드 형태 및 간격 조절)
st.markdown("""
    <style>
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #e9ecef; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. 프로젝트 개요 페이지 ---
if page == "프로젝트 개요":
    st.title("📂 비밀번호 보안성 분석 연구 프로젝트")
    st.markdown("---")
    
    # 상단 2분할
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💡 연구 동기 및 과정")
        with st.container():
            st.markdown("""
            - **연구 동기**: 디지털 계정 유출 사고 증가에 따른 보안 의식 고취 및 실효성 있는 대응책 마련.
            - **수행 과정**: 
                1. 국내외 보안 가이드라인(NIST, KISA) 분석.
                2. 무차별 대입 공격(Brute Force)의 수학적 원리 설계.
                3. 파이썬 및 스트림릿(Streamlit)을 활용한 시각화 도구 구현.
            """)
    with col2:
        st.subheader("📊 분석 기준 (Methodology)")
        st.info("""
        **수학적 공식: $E = L \\times \\log_2(N)$**
        - **$L$**: 비밀번호 길이
        - **$N$**: 문자 집합 크기 (영문 대소문자, 숫자, 특수문자 조합)
        - **공격 시나리오**: 현대 GPU 클러스터 기준, 초당 $10^{10}$ 회 해시 연산 가용성 가정.
        """)
        
    st.markdown("### 🏆 연구 성과 및 의의")
    st.success("""
    본 연구는 보안 이론의 직관적 시각화를 통해 사용자의 **능동적 행동 변화**를 유도하는 것에 목적이 있습니다. 
    단순 이론 학습을 넘어 실시간 정량적 피드백 시스템을 구축함으로써 정보보안 교육의 새로운 모델을 제시하였습니다.
    """)

# --- 2. 보안성 시뮬레이터 페이지 ---
elif page == "보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    
    # 시뮬레이터 카드
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        password = st.text_input("분석할 비밀번호를 입력하세요:", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if password:
        # 분석 로직
        length = len(password)
        n = 0
        if any(c.islower() for c in password): n += 26
        if any(c.isupper() for c in password): n += 26
        if any(c.isdigit() for c in password): n += 10
        if any(not c.isalnum() for c in password): n += 32
        
        entropy = length * math.log2(n) if n > 0 else 0
        seconds = (2**entropy) / (10**10)
        years = seconds / (60 * 60 * 24 * 365)
        
        # 결과 표시 (3분할)
        c1, c2, c3 = st.columns(3)
        c1.metric("엔트로피 강도", f"{entropy:.2f} bits")
        c2.metric("예상 해킹 시간", f"{years:.2f} 년" if years > 0.01 else f"{seconds:.2f} 초")
        
        # 상태에 따른 시각화
        if years > 100:
            st.success("✅ **보안 수준: 매우 안전** - 무차별 대입 공격에 견고한 암호입니다.")
        elif years > 1:
            st.warning("⚠️ **보안 수준: 주의** - 길이가 충분하지 않거나 복잡도가 낮습니다.")
        else:
            st.error("🚨 **보안 수준: 매우 취약** - 즉시 해킹 위험이 있습니다. 비밀번호 변경이 시급합니다!")
            
        st.caption("※ 본 시뮬레이션은 현대 GPU 연산 성능(10^10 H/s)을 기준으로 계산된 이론적 예측치입니다.")
