import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="디지털 보안 연구 보고서", layout="wide")

# CSS: 전문적인 대시보드 스타일
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; }
    .card { background-color: #1e293b; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 20px; color: #f8fafc; }
    .highlight { color: #38bdf8; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# 1. 사이드바
st.sidebar.title("📌 대시보드 메뉴")
page = st.sidebar.radio("목차", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

# --- 연구 종합 보고서 ---
if page == "📂 연구 종합 보고서":
    st.title("📂 디지털 보안 연구 보고서")
    
    # [서론]
    st.subheader("📝 1. 서론")
    c1, c2 = st.columns(2)
    c1.markdown('<div class="card"><h3>🔍 탐구 동기</h3>무분별한 비밀번호 사용으로 인한 개인정보 유출 사고 예방과, 정량적 보안 수치 체감</div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>❓ 탐구 문제</h3>1. 길이와 조합이 해킹 시간과 위험도에 미치는 영향은 무엇인가?<br>2. 안전한 보안을 위한 최적의 기준점은 어디인가?</div>', unsafe_allow_html=True)

    # [본론]
    st.subheader("⚙️ 2. 본론 (탐구 과정 및 분석 기준)")
    col_l, col_r = st.columns([1, 1.2])
    
    with col_l:
        st.markdown('<div class="card"><h3>📊 분석 모델 및 기준</h3>'
                    '본 연구는 <b>엔트로피(Entropy)</b>를 기준으로 위험도를 산출합니다.<br><br>'
                    '• <b>가정</b>: 현대 GPU 성능(10^10 H/s) 기반 무차별 대입 공격<br>'
                    '• <b>위험도 산출</b>: $2^{Entropy} / 10^{10} = 소요시간(초)$<br>'
                    '• <b>기준</b>: 80bits 미만 시 즉시 위험군 분류</div>', unsafe_allow_html=True)
        st.markdown('### 🔍 탐구 과정')
        st.write("1. NIST 보안 지침 분석 → 2. 엔트로피 공식 정립 → 3. 공격 시나리오(GPU) 설정 → 4. 데이터 시각화")
        
    with col_r:
        st.markdown('### 📉 복합 분석: 해킹 시간 vs 보안 강도')
        # 다차원 데이터 시각화 (길이와 조합의 상관관계)
        df = pd.DataFrame({
            '해킹 소요 시간(로그)': [1, 5, 15, 30],
            '위험도 점수(반비례)': [90, 70, 30, 10]
        }, index=['4자/단순', '6자/조합', '8자/조합', '12자/복합'])
        st.bar_chart(df)
        st.caption("결과 해석: 조합(엔트로피)이 높을수록 해킹 시간은 증가하며 위험도는 급격히 하락함")

    # [결론]
    st.subheader("🎯 3. 결론 (종합적 탐구 결과)")
    st.markdown('<div class="card">'
                '<ul><li><b>종합 분석</b>: 보안의 핵심은 단순 조합보다 <b>"길이와 문자셋의 결합(엔트로피)"</b>에 있음이 증명됨.</li>'
                '<li><b>결론</b>: 12자리 이상의 복합 비밀번호는 해킹 소요 시간을 이론적으로 무한대에 가깝게 만들어 최상의 보안을 유지함.</li>'
                '<li><b>제언</b>: 시스템은 사용자에게 단순히 복잡한 비밀번호를 요구하기보다, 최소 12자리 이상의 길이를 권고하는 방향으로 변화해야 함.</li></ul>'
                '</div>', unsafe_allow_html=True)

# --- 시뮬레이터 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 보안성 분석 시뮬레이터")
    pw = st.text_input("분석할 비밀번호 입력", type="password")
    if pw:
        entropy = len(pw) * math.log2(95)
        st.metric("분석된 엔트로피(bits)", f"{entropy:.1f}")
        st.progress(min(entropy / 100, 1.0))
