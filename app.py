import streamlit as st
import math

# 페이지 설정
st.set_page_config(page_title="비밀번호 보안 연구 프로젝트", layout="wide")

# 사이드바 메뉴 설정
st.sidebar.title("메뉴")
page = st.sidebar.radio("페이지 이동", ["프로젝트 개요", "보안성 시뮬레이터"])

# --- 1. 프로젝트 개요 페이지 ---
if page == "프로젝트 개요":
    st.title("📂 비밀번호 보안성 분석 연구")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("연구 동기 및 과정")
        st.write("""
        - **동기:** 디지털 전환 시대의 계정 보안 중요성 인식 및 단순 비밀번호의 위험성 체감.
        - **과정:** 이론적 배경 조사(NIST 가이드라인) → 파이썬 알고리즘 설계 → 스트림릿을 활용한 인터페이스 구현.
        """)
        
    with col2:
        st.subheader("분석 기준 (수학적 근거)")
        st.write("""
        - **엔트로피(Entropy) 이론:** $E = L \times \log_2(N)$
        - **공격 시나리오:** 현대 GPU 클러스터 기준, 초당 100억 회($10^{10}$ H/s) 해시 연산 가정.
        - **근거:** NIST(미국 국립표준기술연구소) SP 800-63B 디지털 신원 지침 준수.
        """)
    
    st.divider()
    st.subheader("연구 결과 및 의의")
    st.info("비밀번호의 복잡도가 해킹 소요 시간에 미치는 지수 함수적 관계를 시각화하여, 능동적인 보안 습관 형성을 유도함.")

# --- 2. 시뮬레이터 페이지 ---
elif page == "보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    password = st.text_input("분석할 비밀번호를 입력하세요", type="password")

    if password:
        # 보안 분석 로직
        length = len(password)
        n = 0
        if any(c.islower() for c in password): n += 26
        if any(c.isupper() for c in password): n += 26
        if any(c.isdigit() for c in password): n += 10
        if any(not c.isalnum() for c in password): n += 32
        
        entropy = length * math.log2(n) if n > 0 else 0
        seconds = (2**entropy) / (10**10)
        years = seconds / (60 * 60 * 24 * 365)
        
        # 결과 대시보드
        st.metric("엔트로피 강도", f"{entropy:.2f} bits")
        
        if years > 100:
            st.success(f"매우 안전: 해킹에 {years:.2f}년 이상 소요")
        elif years > 1:
            st.warning(f"보통: 해킹에 {years:.2f}년 소요")
        else:
            st.error(f"취약: 해킹에 {seconds:.2f}초 소요 (즉시 노출 위험)")
            
        st.write("---")
        st.caption("※ 분석 기준: 초당 100억 회 연산(10^10 H/s) 기반의 무차별 대입 공격 시나리오")
