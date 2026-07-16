import streamlit as st
import math

# 1. 페이지 설정
st.set_page_config(page_title="보안성 분석 연구", layout="wide")

# 2. 전문적인 스타일링 (CSS)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    [data-testid="stSidebar"] { background-color: #1e293b; }
    [data-testid="stSidebar"] * { color: #f8fafc !important; }
    .card { 
        background-color: white; 
        padding: 25px; 
        border-radius: 12px; 
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); 
        margin-bottom: 20px;
    }
    h1 { color: #1e293b; }
    </style>
""", unsafe_allow_html=True)

# 3. 사이드바 구성
st.sidebar.title("📌 연구 탐색")
page = st.sidebar.radio("목차", ["📂 연구 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 1. 연구 보고서 페이지 (내용 강화) ---
if page == "📂 연구 보고서":
    st.title("📂 디지털 보안 강화를 위한 비밀번호 엔트로피 분석")
    st.markdown("---")
    
    st.markdown('<div class="card"><h3>🔍 연구의 배경과 목적 (NIST 지침)</h3>'
                '본 연구는 <b>NIST SP 800-63B 디지털 신원 지침</b>을 기반으로 합니다. '
                '단순한 길이 제한을 넘어, 비밀번호의 <b>엔트로피(Entropy)</b>를 계산하여 무차별 대입 공격(Brute Force)에 '
                '대한 이론적 저항력을 정량화하고, 사용자가 스스로 보안 수준을 판단할 수 있는 가이드라인을 제시합니다.</div>', 
                unsafe_allow_html=True)
    
    st.subheader("🛠️ 연구 수행 체계")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown("**1. 이론 정립**\nNIST 보안 표준 분석 및 엔트로피 이론 연구")
    with col2: st.markdown("**2. 모델 구축**\nGPU 해싱 성능(10^10 H/s) 기반 공격 시나리오 설정")
    with col3: st.markdown("**3. 로직 개발**\nPython을 이용한 실시간 보안성 산출 알고리즘 구현")
    with col4: st.markdown("**4. 결과 도출**\n대시보드 시각화 및 사용자 보안 가이드 생성")

    st.subheader("📊 수학적 분석 모델")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown("**엔트로피 산출식**")
        st.latex("E = L \\times \\log_2(N)")
        st.write("($L$: 길이, $N$: 문자 조합 가짓수)")
    with c_b:
        st.markdown("**분석 의의**")
        st.write("지수 함수적 보안 강화 원리 이해를 통해 단순 암기가 아닌, **조합의 복잡성**이 보안의 핵심임을 증명함.")

# --- 2. 시뮬레이터 페이지 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        password = st.text_input("분석할 비밀번호 입력", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if password:
        # 보안 분석 로직
        n = 95 # 문자셋 크기
        entropy = len(password) * math.log2(n)
        seconds = (2**entropy) / (10**10)
        years = seconds / 31536000
        
        st.subheader("📈 실시간 분석 결과")
        m1, m2 = st.columns(2)
        m1.metric("엔트로피 강도(bits)", f"{entropy:.1f}")
        m2.metric("예상 해킹 소요 시간", f"{years:.2f}년" if years > 1 else f"{seconds:.1f}초")
        
        st.progress(min(entropy / 100, 1.0))
        
        if years > 100: 
            st.success("✅ **[안전]** 현대적 컴퓨팅 환경에서 매우 견고한 보안 수준입니다.")
        elif years > 1: 
            st.warning("⚠️ **[주의]** 최소 12자리 이상의 문자 조합으로 복잡도를 높이는 것을 권장합니다.")
        else: 
            st.error("🚨 **[위험]** 현재 비밀번호는 무차별 대입 공격에 즉시 노출될 가능성이 높습니다.")
            
        st.caption("※ 분석 기준: 최신 GPU 가속 기반(10^10 H/s) 무차별 대입 공격 시나리오 가정")
