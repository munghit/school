import streamlit as st
import math

st.set_page_config(page_title="보안성 분석", layout="wide")

# 고대비 스타일링 (어두운 배경 + 밝은 텍스트)
st.markdown("""
    <style>
    /* 전체 배경을 어두운 네이비색으로 */
    .stApp { background-color: #0f172a; color: #f8fafc; }
    
    /* 사이드바 스타일 */
    [data-testid="stSidebar"] { background-color: #1e293b; }
    [data-testid="stSidebar"] * { color: #e2e8f0 !important; }
    
    /* 카드 스타일 (어두운 배경 위 밝은 회색 카드) */
    .card { 
        background-color: #1e293b; 
        padding: 25px; 
        border-radius: 12px; 
        border: 1px solid #334155;
        margin-bottom: 20px;
        color: #f1f5f9;
    }
    
    /* 글자색 강제 지정 */
    h1, h2, h3, p, label, .stMarkdown { color: #f8fafc !important; }
    </style>
""", unsafe_allow_html=True)

# 사이드바
st.sidebar.title("📌 연구 탐색")
page = st.sidebar.radio("목차", ["📂 연구 보고서", "🛡️ 보안성 시뮬레이터"])

# 1. 연구 보고서 페이지
if page == "📂 연구 보고서":
    st.title("📂 디지털 보안 연구 보고서")
    
    st.markdown('<div class="card"><h3>🔍 연구 목적</h3>NIST SP 800-63B 가이드라인에 따라, 비밀번호의 엔트로피를 분석하여 사용자의 보안 습관을 정량적으로 개선하는 것을 목표로 합니다.</div>', unsafe_allow_html=True)
    
    st.subheader("🛠️ 연구 수행 과정")
    cols = st.columns(4)
    steps = [("1. 이론조사", "보안 표준 분석"), ("2. 모델수립", "엔트로피 공식화"), ("3. 알고리즘", "파이썬 연산"), ("4. 시각화", "대시보드 구축")]
    for i, (t, d) in enumerate(steps):
        with cols[i]: st.markdown(f"**{t}**\n{d}")

    st.subheader("📊 수학적 모델")
    st.latex(r"\color{white}{E = L \times \log_2(N)}")

# 2. 시뮬레이터 페이지
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    
    password = st.text_input("비밀번호 입력", type="password")
    
    if password:
        entropy = len(password) * math.log2(95)
        seconds = (2**entropy) / (10**10)
        years = seconds / 31536000
        
        st.markdown(f"### 📈 결과 (엔트로피: {entropy:.1f} bits)")
        
        c1, c2 = st.columns(2)
        c1.metric("예상 해킹 소요 시간", f"{years:.2f}년" if years > 1 else f"{seconds:.1f}초")
        
        if years > 100: st.success("✅ 최고 보안 등급")
        elif years > 1: st.warning("⚠️ 주의 필요")
        else: st.error("🚨 즉시 변경 권장")
