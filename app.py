import streamlit as st
import math

st.set_page_config(page_title="보안 연구 프로젝트", layout="wide")

# 사이드바 디자인 CSS
st.markdown("""
    <style>
    [data-testid="stSidebar"] { background-color: #2c3e50; }
    [data-testid="stSidebar"] * { color: white !important; }
    .card { background-color: #f8f9fa; padding: 20px; border-radius: 15px; border-left: 5px solid #3498db; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

# 3. 사이드바
st.sidebar.title("📌 연구 탐색")
page = st.sidebar.radio("목차", ["📂 연구 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 1. 연구 보고서 페이지 ---
if page == "📂 연구 보고서":
    st.title("📂 디지털 환경의 비밀번호 보안성 심층 분석")
    
    st.markdown('<div class="card"><h3>🔍 연구 목적</h3>본 연구는 비밀번호 보안의 핵심인 <b>엔트로피(Entropy)</b>를 정량화하여, 무차별 대입 공격에 대한 방어력을 시각적으로 확인하고 개인의 보안 의식을 고취하는 데 목적이 있습니다.</div>', unsafe_allow_html=True)

    st.subheader("🛠️ 연구 수행 과정")
    cols = st.columns(4)
    steps = [("① 이론적 조사", "NIST 가이드라인 기반 보안 지표 분석"), 
             ("② 모델 수립", "엔트로피 공식 및 공격 시나리오 설정"), 
             ("③ 알고리즘 구현", "Python 기반 실시간 강도 산출 로직 설계"), 
             ("④ 시각화 구현", "Streamlit을 통한 대시보드 구축")]
    
    for i, (title, desc) in enumerate(steps):
        cols[i].markdown(f"**{title}**\n\n{desc}")

    st.subheader("📊 수학적 분석 기반")
    c1, c2 = st.columns(2)
    c1.latex("E = L \\times \\log_2(N)")
    c1.caption("엔트로피 공식: 보안 강도의 핵심 지표")
    c2.write("**공격 시나리오:** 최신 GPU(10^10 H/s) 기반 무차별 대입 공격을 가정하여 객관적인 해킹 소요 시간을 도출함.")

# --- 2. 시뮬레이터 페이지 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    
    password = st.text_input("비밀번호를 입력하여 보안성을 확인하세요.", type="password")
    
    if password:
        # 보안 로직
        n = 95 # 대소문자+숫자+특수문자 총 95개 기준
        entropy = len(password) * math.log2(n)
        seconds = (2**entropy) / (10**10)
        years = seconds / (31536000)
        
        st.markdown("### 📈 실시간 분석 결과")
        m1, m2 = st.columns(2)
        m1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        m2.metric("예상 해킹 시간", f"{years:.2f}년" if years > 1 else f"{seconds:.1f}초")
        
        # 상태 표시
        if years > 100: st.success("✅ **보안 수준: 최고** (매우 안전한 비밀번호입니다)")
        elif years > 1: st.warning("⚠️ **보안 수준: 보통** (길이를 조금 더 늘리는 것을 권장합니다)")
        else: st.error("🚨 **보안 수준: 매우 취약** (즉시 변경이 시급합니다)")
