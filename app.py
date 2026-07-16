import streamlit as st
import math

# 페이지 설정
st.set_page_config(page_title="보안 연구 프로젝트", layout="wide")

# 사이드바 디자인
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #f0f2f6; }
    .css-1544g2n { font-size: 1.2rem; }
    h1 { color: #2c3e50; }
    h3 { font-size: 1.2rem !important; }
    .stMarkdown, .stWrite { font-size: 1.1rem !important; }
    </style>
""", unsafe_allow_html=True)

# 사이드바
st.sidebar.title("📌 연구 탐색")
page = st.sidebar.radio("목차", ["📂 연구 보고서", "🛡️ 시뮬레이터"])

# --- 1. 연구 보고서 페이지 ---
if page == "📂 연구 보고서":
    st.title("📂 디지털 환경의 비밀번호 보안성 심층 분석")
    
    tab1, tab2, tab3 = st.tabs(["📌 연구 개요", "🛠️ 수행 과정", "📈 연구 결과 및 성과"])
    
    with tab1:
        st.subheader("💡 연구 배경 및 목적")
        st.write("""
        오늘날 디지털 계정은 개인의 핵심 자산이나, 여전히 많은 사용자가 기억하기 쉬운 단순한 비밀번호를 사용하여 해킹 위험에 노출되어 있습니다.
        본 연구는 **엔트로피 기반 비밀번호 강도 측정 알고리즘**을 개발하여, 무차별 대입 공격(Brute Force)에 대한 방어력을 정량적으로 분석합니다.
        이를 통해 사용자에게 직관적인 보안 피드백을 제공하고, 안전한 디지털 습관 형성을 유도하는 것을 목적으로 합니다.
        """)
    
    with tab2:
        st.subheader("🛠️ 체계적인 연구 수행 과정")
        # 글자 크기를 적절히 유지하며 레이아웃 개선
        cols = st.columns(4)
        process = [
            ("① 문헌 조사", "국내외 보안 표준(NIST, KISA) 가이드라인 분석"),
            ("② 모델 설계", "비밀번호 경우의 수 및 엔트로피 수학적 모델 구축"),
            ("③ 로직 구현", "Python 기반의 실시간 보안 연산 알고리즘 개발"),
            ("④ 도구 개발", "Streamlit을 활용한 사용자 친화적 대시보드 배포")
        ]
        for i, (title, desc) in enumerate(process):
            with cols[i]:
                st.markdown(f"**{title}**")
                st.caption(desc)
            
    with tab3:
        st.subheader("📈 연구 성과 및 결과")
        st.info("비밀번호 복잡도와 해킹 소요 시간의 상관관계를 입증하고, 실용적 도구를 구현함")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### **연구의 의의**")
            st.write("- **학술적 가치**: 추상적인 보안 개념을 정량적 수치로 가시화함.")
            st.write("- **실용적 가치**: 사용자 스스로 자신의 보안 수준을 실시간 점검 가능.")
        with col2:
            st.markdown("#### **후속 연구 제안**")
            st.write("- **데이터 고도화**: 실제 유출된 비밀번호 데이터셋 대조 기능.")
            st.write("- **공격 다변화**: 사회공학적 기법 및 사전 공격 대응 로직 포함.")

# --- 2. 시뮬레이터 페이지 ---
elif page == "🛡️ 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    
    password = st.text_input("분석할 비밀번호 입력", type="password")
    
    if password:
        length = len(password)
        n = 0
        if any(c.islower() for c in password): n += 26
        if any(c.isupper() for c in password): n += 26
        if any(c.isdigit() for c in password): n += 10
        if any(not c.isalnum() for c in password): n += 32
        
        entropy = length * math.log2(n) if n > 0 else 0
        seconds = (2**entropy) / (10**10)
        years = seconds / (60 * 60 * 24 * 365)
        
        # 시각적 결과 구역
        st.markdown("### 📊 분석 결과")
        c1, c2, c3 = st.columns(3)
        c1.metric("엔트로피(bits)", f"{entropy:.1f}")
        c2.metric("예상 해킹 시간", f"{years:.2f}년" if years > 0.001 else f"{seconds:.1f}초")
        
        st.progress(min(entropy / 100, 1.0))
        
        if years > 100: st.success("✅ **보안 등급: 최고 (매우 안전)**")
        elif years > 1: st.warning("⚠️ **보안 등급: 주의 (개선 권장)**")
        else: st.error("🚨 **보안 등급: 위험 (즉시 변경 필요)**")
