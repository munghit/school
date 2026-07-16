import streamlit as st
import math
import requests
from streamlit_lottie import st_lottie

# 1. 페이지 설정
st.set_page_config(page_title="비밀번호 보안 프로젝트", layout="wide")

# 2. 디자인 CSS (메모지 카드 스타일 & 사이드바 다크테마)
st.markdown("""
    <style>
    /* 사이드바 스타일 */
    [data-testid="stSidebar"] {
        background-color: #2c3e50;
    }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* 메모지 카드 스타일 */
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border-left: 5px solid #3498db;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Lottie 애니메이션 불러오기
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200: return None
    return r.json()

lottie_security = load_lottie("https://assets5.lottiefiles.com/packages/lf20_t3rzr5b6.json")

# 3. 사이드바
st.sidebar.title("📌 연구 탐색")
page = st.sidebar.radio("목차", ["📂 연구 보고서", "🛡️ 시뮬레이터"])

# --- 1. 연구 보고서 페이지 ---
if page == "📂 연구 보고서":
    st.title("📂 디지털 환경의 비밀번호 보안성 심층 분석")
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_security, height=300)
        
    with col2:
        st.markdown('<div class="card"><h3>🔍 연구 목적</h3>본 연구는 사용자 비밀번호의 취약점을 수학적으로 분석하고, 정량적 피드백을 제공함으로써 정보보안의 인식을 개선하고자 합니다.</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><h3>🛠️ 연구 과정</h3>1. 가이드라인 분석 → 2. 수학적 모델 수립 → 3. 알고리즘 구현 → 4. 인터페이스 시각화</div>', unsafe_allow_html=True)

    st.subheader("📊 핵심 성과")
    c1, c2, c3 = st.columns(3)
    c1.metric("이론적 근거", "NIST SP 800-63B")
    c2.metric("분석 핵심", "엔트로피(Entropy)")
    c3.metric("구현 도구", "Streamlit & Python")

# --- 2. 시뮬레이터 페이지 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        password = st.text_input("분석할 비밀번호 입력", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if password:
        # 분석 로직
        entropy = len(password) * math.log2(40) # 단순화된 엔트로피 계산
        seconds = (2**entropy) / (10**10)
        years = seconds / (31536000)
        
        st.markdown(f"### 📈 분석 리포트")
        m1, m2 = st.columns(2)
        m1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        m2.metric("예상 해킹 시간", f"{years:.2f}년" if years > 1 else f"{seconds:.1f}초")
        
        st.progress(min(entropy / 100, 1.0))
        
        if years > 100: st.success("✅ **보안 등급: 최고 (매우 안전)**")
        elif years > 1: st.warning("⚠️ **보안 등급: 보통 (복잡도 향상 권장)**")
        else: st.error("🚨 **보안 등급: 위험 (즉시 변경 필요)**")
