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
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 실시간 보안 강도 분석기")
    st.markdown("---")
    
    # 1. 입력 섹션
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        password = st.text_input("분석할 비밀번호를 입력하세요 (암호화 처리됨)", type="password")
        st.markdown('</div>', unsafe_allow_html=True)
    
    if password:
        # 분석 로직 (엔트로피 계산)
        # 문자 종류 계산 (대문자, 소문자, 숫자, 특수문자 고려)
        charset_size = 0
        if any(c.islower() for c in password): charset_size += 26
        if any(c.isupper() for c in password): charset_size += 26
        if any(c.isdigit() for c in password): charset_size += 10
        if any(not c.isalnum() for c in password): charset_size += 33
        
        entropy = len(password) * math.log2(charset_size if charset_size > 0 else 1)
        
        # 해킹 시간 추정 (10^10 H/s 가정)
        seconds = (2**entropy) / (10**10)
        
        # 2. 결과 시각화 (시각적 재미 요소)
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📊 보안 지표 상세")
            st.metric("엔트로피 강도", f"{entropy:.1f} bits")
            # 보안 등급에 따른 컬러 프로그레스바
            progress_val = min(entropy / 120, 1.0)
            st.write("보안 수준 게이지")
            st.progress(progress_val)
            
            if entropy < 50: st.error("🚨 등급: 매우 취약 (수초 이내 해독)")
            elif entropy < 80: st.warning("⚠️ 등급: 보통 (복잡도 향상 필요)")
            else: st.success("✅ 등급: 매우 안전 (해독 불가 수준)")
            
        with col2:
            st.markdown("### ⏱️ 공격 시뮬레이션 예상 시간")
            # 가독성을 위한 시간 변환
            if seconds < 60: time_str = f"{seconds:.2f} 초"
            elif seconds < 3600: time_str = f"{seconds/60:.2f} 분"
            elif seconds < 86400: time_str = f"{seconds/3600:.2f} 시간"
            else: time_str = f"{seconds/31536000:.2f} 년"
            
            st.metric("예상 해킹 소요 시간", time_str)
            st.info("※ 가정: 현대적인 GPU 클러스터 기반 무차별 대입 공격 (10^10 H/s)")

        # 3. 추가 조언 카드
        st.markdown("---")
        st.markdown('<div class="card"><h4>💡 보안 엔지니어의 조언</h4>'
                    '입력하신 비밀번호의 엔트로피가 80 bits를 넘지 못한다면, <b>길이를 12자 이상으로 늘리거나 특수문자를 추가</b>하여 '
                    '경우의 수를 2배 이상 확보하는 것을 강력히 권장합니다.</div>', unsafe_allow_html=True)
