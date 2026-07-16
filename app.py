import streamlit as st
import math

st.set_page_config(page_title="보안 연구 프로젝트", layout="wide")

# 사이드바
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("목차", ["프로젝트 개요", "보안성 시뮬레이터"])

# --- 1. 프로젝트 개요 페이지 (상세 구성) ---
if page == "프로젝트 개요":
    st.title("📂 디지털 환경의 비밀번호 보안성 심층 분석")
    st.markdown("---")

    # [섹션 1] 연구 동기
    with st.expander("🔍 연구 동기 및 목적", expanded=True):
        st.write("""
        디지털 경제 전환으로 인해 온라인 계정의 중요성이 커졌으나, 다수의 사용자가 여전히 관리의 편리함을 위해 취약한 비밀번호를 사용하고 있습니다.
        본 연구는 무차별 대입 공격(Brute Force Attack)의 원리를 수학적으로 규명하고, **사용자가 자신의 비밀번호 취약성을 실시간으로 체감할 수 있는 도구를 개발**하여 보안 인식 개선 및 실질적인 대응 방안을 제시하는 데 목적이 있습니다.
        """)

    # [섹션 2] 상세 연구 과정 (타임라인 스타일)
    st.subheader("🛠️ 체계적인 연구 수행 과정")
    cols = st.columns(4)
    steps = [
        ("Step 1. 문헌 조사", "NIST(SP 800-63B) 및 KISA 가이드라인 분석"),
        ("Step 2. 모델 설계", "엔트로피 공식 및 공격 시나리오 수립"),
        ("Step 3. 로직 구현", "Python 기반의 암호 강도 산출 알고리즘 개발"),
        ("Step 4. 시각화", "Streamlit을 활용한 인터랙티브 대시보드 구축")
    ]
    for i, (title, desc) in enumerate(steps):
        cols[i].markdown(f"**{title}**\n\n{desc}")

    # [섹션 3] 전문적 분석 기준
    st.subheader("📊 수학적·기술적 분석 모델")
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown("""
        #### **1. 엔트로피 공식 (Entropy Formula)**
        비밀번호의 정보 이론적 강도는 다음을 통해 계산됩니다.
        $$E = L \\times \\log_2(N)$$
        - **$L$**: 비밀번호 길이
        - **$N$**: 사용된 문자셋의 크기 (대문자 26, 소문자 26, 숫자 10, 특수문자 32)
        """)
        
    with c2:
        st.markdown("""
        #### **2. 공격 시나리오 (Threat Model)**
        현대적 해킹 환경을 상정한 객관적 수치입니다.
        - **공격 방식**: 무차별 대입 (Brute Force)
        - **연산 속도**: $10^{10}$ H/s (최신 GPU 병렬 처리 기준)
        - **검증**: 공식적인 해시 연산 속도 기반의 이론적 소요 시간 도출
        """)

    st.success("연구 결론: 비밀번호는 단순히 '복잡한 조합'이 아니라, '지수적 연산 비용'을 통한 방어 체계임을 입증하였습니다.")

# --- 2. 시뮬레이터 페이지 (이전 코드 유지/개선) ---
elif page == "보안성 시뮬레이터":
    # ... (이전과 동일한 시뮬레이터 코드 사용)
