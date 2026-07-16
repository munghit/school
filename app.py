import streamlit as st
import math

# 1. 페이지 설정
st.set_page_config(page_title="비밀번호 보안 연구 프로젝트", layout="wide")

# 2. 사이드바
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("목차", ["프로젝트 개요", "보안성 시뮬레이터"])

# 3. 로직 함수
def analyze_security(password):
    length = len(password)
    n = 0
    if any(c.islower() for c in password): n += 26
    if any(c.isupper() for c in password): n += 26
    if any(c.isdigit() for c in password): n += 10
    if any(not c.isalnum() for c in password): n += 32
    entropy = length * math.log2(n) if n > 0 else 0
    seconds = (2**entropy) / (10**10) # 100억 H/s 기준
    return entropy, seconds

# 4. 페이지 전환 로직
if page == "프로젝트 개요":
    st.title("📂 디지털 환경의 비밀번호 보안성 심층 분석")
    st.markdown("---")

    with st.expander("🔍 연구 동기 및 목적", expanded=True):
        st.write("사용자가 자신의 비밀번호 취약성을 실시간으로 체감할 수 있는 도구를 개발하여, 보안 인식 개선 및 대응 방안을 제시하는 데 목적이 있습니다.")

    st.subheader("🛠️ 체계적인 연구 수행 과정")
    cols = st.columns(4)
    steps = [
        ("Step 1. 문헌 조사", "NIST 및 KISA 가이드라인 분석"),
        ("Step 2. 모델 설계", "엔트로피 공식 및 공격 시나리오 수립"),
        ("Step 3. 로직 구현", "Python 기반 알고리즘 개발"),
        ("Step 4. 시각화", "Streamlit을 활용한 대시보드 구축")
    ]
    for i, (title, desc) in enumerate(steps):
        cols[i].markdown(f"**{title}**\n\n{desc}")

    st.subheader("📊 수학적·기술적 분석 모델")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### **1. 엔트로피 공식**")
        st.latex("E = L \\times \\log_2(N)")
        st.write("- $L$: 비밀번호 길이, $N$: 문자셋 크기")
    with c2:
        st.markdown("#### **2. 공격 시나리오**")
        st.write("- **방식**: 무차별 대입 (Brute Force)")
        st.write("- **속도**: 10^10 H/s (현대적 GPU 기준)")
    st.success("연구 결론: 비밀번호는 단순 암기가 아닌, '지수적 연산 비용'의 방어 체계임.")

elif page == "보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    password = st.text_input("분석할 비밀번호를 입력하세요:", type="password")
    
    if password:
        entropy, seconds = analyze_security(password)
        years = seconds / (60 * 60 * 24 * 365)
        
        c1, c2 = st.columns(2)
        c1.metric("엔트로피 강도", f"{entropy:.2f} bits")
        c2.metric("예상 해킹 시간", f"{years:.2f} 년" if years > 0.01 else f"{seconds:.2f} 초")
        
        if years > 100: st.success("✅ 보안 수준: 매우 안전")
        elif years > 1: st.warning("⚠️ 보안 수준: 주의")
        else: st.error("🚨 보안 수준: 매우 취약")
        st.caption("※ 분석 기준: 현대 GPU(10^10 H/s) 무차별 대입 공격 기준")
