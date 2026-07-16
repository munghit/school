import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="디지털 보안 연구 보고서", layout="wide")

# CSS 스타일링
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .card { background-color: #1e293b; padding: 25px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 20px; color: #f8fafc; }
    .step-box { background-color: #334155; padding: 15px; border-radius: 10px; margin-bottom: 10px; border-left: 4px solid #38bdf8; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 메뉴")
page = st.sidebar.radio("목차", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 연구 종합 보고서 ---
if page == "📂 연구 종합 보고서":
    st.title("📂 디지털 보안 연구 종합 보고서")
    
    # [서론]
    st.subheader("📝 1. 서론")
    c1, c2 = st.columns(2)
    c1.markdown('<div class="card"><h3>🔍 탐구 동기</h3>계정 탈취 사고의 근본 원인인 "취약한 비밀번호" 문제를 정량적 데이터로 해결하고자 함.</div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>❓ 탐구 문제</h3>1. 어떤 요소가 비밀번호의 해킹 저항력을 결정하는가?<br>2. 보안과 사용 편의성 사이의 최적점은 어디인가?</div>', unsafe_allow_html=True)

    # [본론]
    st.subheader("⚙️ 2. 본론 (탐구 과정 및 분석)")
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown('### 🛠️ 탐구 수행 순서')
        steps = ["1. 문헌 조사 (NIST 표준)", "2. 엔트로피 수학 모델링", "3. GPU 공격 시뮬레이션 환경 구축", "4. 데이터 수집 및 상관관계 분석"]
        for step in steps:
            st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
            
    with col2:
        st.markdown('### 📊 분석 기준 및 결과 데이터')
        st.write("분석 공식: $E = L \\times \\log_2(N)$ / 해킹 시간: $2^E / 10^{10}sec$")
        df = pd.DataFrame({
            '해킹 시간(로그)': [1, 5, 15, 30],
            '위험도 점수': [90, 60, 20, 5]
        }, index=['4자/단순', '6자/조합', '8자/조합', '12자/복합'])
        st.bar_chart(df)

   # [결론]
    st.subheader("🎯 3. 결론 (종합적 탐구 결과)")
    st.markdown('<div class="card">'
                '<ul><li><b>길이와 조합의 상호보완성</b>: 비밀번호 보안은 단순히 글자 수만 늘리는 것이 아니라, <b>"충분한 길이(12자리 이상)"</b>와 <b>"다양한 문자 집합(대/소문자, 숫자, 특수문자)"</b>이 결합될 때 비로소 완성됨.</li>'
                '<li><b>엔트로피(Entropy)의 극대화</b>: 다양한 문자 조합은 경우의 수를 기하급수적으로 늘려 무차별 대입 공격을 무력화하며, 12자리 이상의 길이는 이를 현실적으로 해독 불가능한 시간대(수백 년 이상)로 고착시킴.</li>'
                '<li><b>종합적 판단</b>: 따라서 최적의 보안 기준은 <b>[12자리 이상 + 무작위 문자 조합]</b>이며, 이는 현대 컴퓨팅 성능을 고려했을 때 해킹 비용을 이득보다 높게 만드는 가장 효율적인 방어 전략임.</li>'
                '<li><b>제언</b>: 보안 시스템 설계 시 사용자에게 단순 복잡성을 강요하기보다, 실효성 있는 <b>"최소 길이 가이드라인"</b>을 우선시하는 정책이 필요함.</li></ul>'
                '</div>', unsafe_allow_html=True)
# --- 시뮬레이터 페이지 부분 ---
import streamlit as st
import math

# 페이지 설정
# CSS: 입체적인 카드 효과, 빛나는 효과, 애니메이션
st.markdown("""
    <style>
    .glass-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
    }
    .neon-text { color: #38bdf8; text-shadow: 0 0 10px #38bdf8; }
    .gauge-container { width: 100%; height: 30px; background: #0f172a; border-radius: 15px; overflow: hidden; border: 1px solid #475569; }
    .gauge-fill { height: 100%; transition: width 1s ease-in-out, background-color 0.5s; }
    </style>
""", unsafe_allow_html=True)

# 시뮬레이터 페이지
st.title("🛡️ 실시간 보안 강도 분석기")

# 입력 섹션
with st.container():
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    password = st.text_input("비밀번호를 입력하세요:", type="password")
    
    if password:
        # 엔트로피 계산 로직
        charset = sum([26 if any(c.islower() for c in password) else 0,
                       26 if any(c.isupper() for c in password) else 0,
                       10 if any(c.isdigit() for c in password) else 0,
                       33 if any(not c.isalnum() for c in password) else 0])
        entropy = len(password) * math.log2(charset if charset > 0 else 1)
        
        # 등급 설정
        if entropy < 40: level, color, val = "취약", "#ef4444", 25
        elif entropy < 70: level, color, val = "보통", "#f59e0b", 50
        elif entropy < 100: level, color, val = "안전", "#3b82f6", 75
        else: level, color, val = "철통 보안", "#22c55e", 100

        # 결과 출력
        col1, col2 = st.columns(2)
        col1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        
        # [시각적 재미] CSS 게이지 바
        st.markdown(f"""
            <div style="margin: 20px 0;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>보안 등급: <b>{level}</b></span>
                </div>
                <div class="gauge-container">
                    <div class="gauge-fill" style="width: {val}%; background-color: {color};"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # 해킹 시간 계산
        seconds = (2**entropy) / (10**10)
        time_str = f"{seconds:.2f} 초" if seconds < 60 else (f"{seconds/60:.2f} 분" if seconds < 3600 else (f"{seconds/3600:.2f} 시간" if seconds < 86400 else f"{seconds/31536000:.2f} 년"))
        
        col2.metric("예상 해킹 소요 시간", time_str)
        
        st.markdown(f'</div>', unsafe_allow_html=True)
        
        # 하단 조언 섹션
        st.info("💡 보안 강화 팁: 12자리 이상 무작위 조합을 사용하면 해킹 시뮬레이션 시간이 '년' 단위로 급증합니다.")
    else:
        st.markdown('</div>', unsafe_allow_html=True)
