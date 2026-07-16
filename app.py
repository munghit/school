import streamlit as st
import math

# 1. 페이지 설정 및 디자인 CSS
st.set_page_config(page_title="비밀번호 보안 프로젝트", layout="wide")

# 사이드바 디자인을 위한 커스텀 CSS (사이드바 폭과 스타일 조정)
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-image: linear-gradient(180deg, #2c3e50 0%, #000000 100%);
        color: white;
    }
    .stRadio label { color: white !important; font-weight: bold; }
    .css-1d391kg { padding: 20px; }
    </style>
""", unsafe_allow_html=True)

# 2. 사이드바 구성
st.sidebar.title("🧭 연구 목차")
st.sidebar.markdown("---")
page = st.sidebar.radio("메뉴 선택", ["📂 프로젝트 개요", "🛡️ 보안성 시뮬레이터"])
st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip**: 비밀번호는 최소 12자리 이상, 다양한 문자 조합을 권장합니다.")

# 3. 로직 함수
def analyze_security(password):
    length = len(password)
    n = 0
    if any(c.islower() for c in password): n += 26
    if any(c.isupper() for c in password): n += 26
    if any(c.isdigit() for c in password): n += 10
    if any(not c.isalnum() for c in password): n += 32
    entropy = length * math.log2(n) if n > 0 else 0
    seconds = (2**entropy) / (10**10) 
    return entropy, seconds

# 4. 페이지 내용
if page == "📂 프로젝트 개요":
    st.title("📂 디지털 환경의 비밀번호 보안성 심층 분석")
    st.markdown("---")

    # 탭을 활용한 섹션 정리
    tab1, tab2, tab3 = st.tabs(["📌 연구 개요", "🛠️ 수행 과정", "📊 분석 모델"])
    
    with tab1:
        st.subheader("💡 연구 동기 및 목적")
        st.warning("온라인 계정 유출 사고의 80% 이상이 '취약한 비밀번호'에서 비롯됩니다.")
        st.write("본 프로젝트는 엔트로피 이론을 기반으로, 사용자의 비밀번호 보안성을 정량적으로 측정하고 능동적인 보안 습관 형성을 돕는 시스템을 설계하는 데 목적이 있습니다.")
        
    with tab2:
        st.subheader("🛠️ 연구 수행 과정")
        cols = st.columns(4)
        process = [("① 문헌 조사", "NIST 및 KISA 지침 분석"), ("② 모델 설계", "엔트로피 공식 수립"), 
                   ("③ 알고리즘", "파이썬 연산 로직 구현"), ("④ 결과 시각화", "웹 대시보드 구축")]
        for i, (title, desc) in enumerate(process):
            cols[i].metric(title, desc)
            
    with tab3:
        st.subheader("📊 수학적·기술적 분석 모델")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### **엔트로피 공식**")
            st.latex("E = L \\times \\log_2(N)")
        with col_b:
            st.markdown("### **해킹 시나리오**")
            st.info("최신 GPU 환경 기준 (10^10 H/s 연산)")

elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    st.markdown("비밀번호를 입력하여 실시간 보안 강도를 확인하세요.")
    
    password = st.text_input("비밀번호 입력", type="password")
    
    if password:
        entropy, seconds = analyze_security(password)
        years = seconds / (60 * 60 * 24 * 365)
        
        # 시각적 결과물
        col1, col2 = st.columns(2)
        col1.metric("엔트로피 강도", f"{entropy:.2f} bits", "High security" if entropy > 60 else "Low security")
        col2.metric("예상 해킹 시간", f"{years:.2f} 년" if years > 1 else f"{seconds:.1f} 초")
        
        st.progress(min(entropy / 100, 1.0)) # 보안성 프로그레스 바
        
        if years > 100: st.success("✅ 강력한 비밀번호입니다.")
        elif years > 1: st.warning("⚠️ 조금 더 복잡하게 만드는 것을 추천합니다.")
        else: st.error("🚨 매우 위험! 즉시 변경하세요.")
