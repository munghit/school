import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="디지털 보안 연구 보고서", layout="wide")

st.markdown("""
<style>
.stApp { background:#020617; color:#e2e8f0; }
h1 { color:#38bdf8; font-size:42px; font-weight:900; }
h2, h3 { color:#e0f2fe; }
.card { background:#111827; padding:25px; border-radius:18px; border:1px solid #334155; box-shadow: 0 8px 25px rgba(0,0,0,0.35); color:#f8fafc; line-height:1.8; }
.step-box { background:#172554; padding:16px; margin-bottom:12px; border-radius:12px; border-left:5px solid #38bdf8; color:#dbeafe; font-weight:700; }
[data-testid="metric-container"] { background:#111827; border-radius:15px; padding:18px; border:1px solid #334155; }
[data-testid="stMetricValue"] { color:#38bdf8; font-size:30px; font-weight:900; }
.stProgress > div > div { background:#38bdf8; }
.stTextInput input { background:#111827; color:white; border:1px solid #38bdf8; border-radius:10px; }
section[data-testid="stSidebar"] { background:#020617; border-right:1px solid #334155; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📌 연구 메뉴")
page = st.sidebar.radio("페이지 선택", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

if page == "📂 연구 종합 보고서":
    st.title("📂 디지털 보안 연구 종합 보고서")
    
    st.markdown("""
    <div class="card">
    <h3>🔐 비밀번호 보안성 정량 분석 연구</h3>
    <b>연구 분야</b>: 정보보안 · 암호학 · 데이터 기반 보안 분석<br>
    <b>연구 목적</b>: 비밀번호의 보안성을 수학적 정보량과 공격 저항성을 기반으로 정량 평가한다.<br>
    <b>평가 방법</b>: 엔트로피 계산 · 무차별 대입 공격 모델 · 예상 해독 시간 분석
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📝 1. 서론")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""<div class="card"><h3>🔍 탐구 동기</h3>취약한 비밀번호는 계정 탈취의 주원인입니다. 기존의 '복잡성 강제' 방식이 실제 공격 저항성을 충분히 설명하지 못한다는 문제의식에서 시작했습니다.</div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""<div class="card"><h3>❓ 탐구 문제</h3>1. 보안성의 핵심 결정 요소는 무엇인가?<br>2. 길이와 조합 중 무엇이 더 중요한가?<br>3. 보안성과 사용성의 최적 균형점은?</div>""", unsafe_allow_html=True)

    st.subheader("⚙️ 2. 본론 (탐구 과정)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.markdown("### 🛠️ 연구 진행 과정")
        for step in ["1단계 : 문헌 조사", "2단계 : 엔트로피 모델 설계", "3단계 : 공격 환경 가정", "4단계 : 데이터 비교 분석"]:
            st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown("### 📊 보안성 평가 모델")
        st.markdown("""<div class="card"><b>1. 엔트로피(Entropy):</b> E = L × log₂(N)<br><b>2. 공격 모델:</b> 초당 100억 회 연산(GPU 기반) 기준 해독 시간 산출</div>""", unsafe_allow_html=True)

    st.subheader("📈 비밀번호 조건별 보안성 비교")
    df = pd.DataFrame({"유형": ["4자리 단순", "6자리 조합", "8자리 조합", "12자리 복합"], "위험도": [90, 60, 20, 5], "저항성": [10, 40, 80, 95]})
    st.bar_chart(df.set_index("유형"))

    st.subheader("🎯 3. 결론 (종합적 탐구 결과)")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="card" style="border-top: 5px solid #38bdf8;"><h4>암호학적 효율성</h4>지수적인 길이 증가가 공격자의 계산 복잡도를 압도함. 12자 이상의 정보 밀도 높은 조합이 핵심임.</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card" style="border-top: 5px solid #fbbf24;"><h4>인지적 효율성</h4>복잡성 규칙은 인지적 마찰을 유발함. <b>패스프레이즈</b>가 보안과 사용성을 확보하는 최적의 모델임.</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="card" style="border-top: 5px solid #22c55e;"><h4>보안적 경제성</h4>최적 보안은 기술과 행동의 균형점임. 12자 이상 패스프레이즈는 연산 비용을 이득보다 높게 만듦.</div>', unsafe_allow_html=True)

elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 비밀번호 보안성 평가 시스템")
    password = st.text_input("🔑 분석할 비밀번호 입력", type="password")
    
    if password:
        charset_size = sum([26 if any(c.islower() for c in password) else 0, 26 if any(c.isupper() for c in password) else 0, 10 if any(c.isdigit() for c in password) else 0, 33 if any(not c.isalnum() for c in password) else 0])
        entropy = len(password) * math.log2(charset_size if charset_size > 0 else 1)
        score = min(int(entropy), 100)
        
        if entropy < 40: level, color, icon = "매우 위험", "#ef4444", "🚨"
        elif entropy < 70: level, color, icon = "보통", "#f59e0b", "⚠️"
        elif entropy < 100: level, color, icon = "안전", "#3b82f6", "🔒"
        else: level, color, icon = "매우 안전", "#22c55e", "🛡️"

        st.subheader("🎯 종합 보안 평가")
        st.progress(score / 100)
        st.markdown(f'<div style="background:#111827; padding:30px; border-radius:20px; border:1px solid {color}; text-align:center;"><h2>{icon} {level}</h2></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("정보량(bits)", f"{entropy:.2f}")
        col2.metric("길이", f"{len(password)}자")
        col3.metric("점수", f"{score}/100")

        seconds = (2**entropy) / (10**10)
        time_result = f"{seconds:.2f}초" if seconds < 60 else (f"{seconds/60:.2f}분" if seconds < 3600 else (f"{seconds/3600:.2f}시간" if seconds < 86400 else (f"{seconds/86400:.2f}일" if seconds < 31536000 else f"{seconds/31536000:.2f}년")))
        
        st.markdown(f'<div class="card"><h3>⚔️ 예상 해독 시간</h3><h1 style="text-align:center; color:{color};">{time_result}</h1></div>', unsafe_allow_html=True)
        
        st.subheader("🕵️ 예상 침투 위험도")
        risk = max(0, 100 - score)
        st.markdown(f'<h1 style="text-align:center; color:{color}; font-size:60px;">{risk:.2f}%</h1>', unsafe_allow_html=True)
        st.progress(risk / 100)
