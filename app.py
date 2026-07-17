import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="디지털 보안 연구 보고서", layout="wide")

st.markdown("""
<style>
.stApp { background: #020617; color: #e2e8f0; font-family: 'Pretendard', sans-serif; }
.nav-header { background: #0f172a; padding: 25px; border-radius: 0 0 25px 25px; border-bottom: 3px solid #38bdf8; text-align: center; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.3); }
h1 { color: #38bdf8; font-weight: 900; margin: 0; }
.card { background: linear-gradient(145deg, #111827, #0f172a); padding: 30px; border-radius: 20px; border: 1px solid #334155; box-shadow: 0 10px 25px rgba(0,0,0,0.4); margin-bottom: 20px; }
.step-box { background: #172554; padding: 18px; border-radius: 15px; border-left: 6px solid #38bdf8; margin-bottom: 15px; font-weight: 700; }
[data-testid="metric-container"] { background: #111827; border-radius: 20px; padding: 25px; border: 1px solid #334155; text-align: center; }
[data-testid="stMetricValue"] { color: #38bdf8 !important; font-size: 35px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="nav-header"><h1>🛡️ Digital Security Intelligence</h1></div>', unsafe_allow_html=True)

st.sidebar.title("📌 연구 메뉴")
page = st.sidebar.radio("페이지 선택", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

if page == "📂 연구 종합 보고서":
    st.title("📂 디지털 보안 연구 종합 보고서")
    
    st.markdown("""
    <div class="card">
    <h3>🔐 비밀번호 보안성 정량 분석 연구</h3>
    <b>연구 분야</b>: 정보보안 · 암호학 · 데이터 기반 보안 분석<br>
    <b>개발 도구</b>: <b>Streamlit</b>(웹 프레임워크) & <b>GitHub</b>(버전 관리 및 배포)<br>
    <b>연구 목적</b>: 비밀번호 보안성을 수학적 정보량과 공격 저항성 기반으로 정량 평가.<br>
    <b>평가 방법</b>: 엔트로피 계산 · 무차별 대입 공격 모델 · 해독 시간 분석
    </div>
    """, unsafe_allow_html=True)

    st.subheader("⚙️ 2. 본론 (탐구 및 개발 과정)")
    col1, col2 = st.columns([1, 1.2])
    with col1:
        steps = [
            "1단계 : 보안 관련 문헌 조사", 
            "2단계 : 엔트로피 기반 수학 모델 설계", 
            "3단계 : GPU 무차별 대입 공격 환경 가정", 
            "4단계 : Streamlit 활용 웹 시스템 구축", 
            "5단계 : GitHub 기반 배포 및 보안성 분석"
        ]
        for step in steps:
            st.markdown(f'<div class="step-box">{step}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>📌 핵심 기술 스택</h3><ul><li><b>Streamlit:</b> 대화형 데이터 분석 웹 애플리케이션 프레임워크</li><li><b>GitHub:</b> 코드 버전 관리 및 지속적 통합/배포(CI/CD)</li><li><b>Python:</b> 암호학적 엔트로피 계산 로직 구현</li></ul></div>', unsafe_allow_html=True)

    # (결론 부분은 이전과 동일하게 유지)
    st.subheader("🎯 3. 결론 (종합 결과)")
    k1, k2, k3 = st.columns(3)
    k1.markdown('<div class="card" style="border-top:5px solid #38bdf8"><h4>암호학적 효율성</h4>지수적 길이 증가가 공격자의 계산 복잡도를 압도함. 12자 이상의 정보 밀도 높은 조합이 핵심.</div>', unsafe_allow_html=True)
    k2.markdown('<div class="card" style="border-top:5px solid #fbbf24"><h4>인지적 효율성</h4>복잡성 규칙은 인지적 마찰을 유발함. <b>패스프레이즈</b>가 사용성과 보안을 동시에 확보하는 최적점.</div>', unsafe_allow_html=True)
    k3.markdown('<div class="card" style="border-top:5px solid #22c55e"><h4>보안적 경제성</h4>12자 이상의 패스프레이즈는 해독 비용이 이득을 상회하게 만드는 <b>경제적 방어선</b>을 구축함.</div>', unsafe_allow_html=True)

elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 실시간 보안 강도 분석기")
    password = st.text_input("🔑 비밀번호를 입력하세요", type="password")
    
    if password:
        charset_size = sum([26 if any(c.islower() for c in password) else 0, 26 if any(c.isupper() for c in password) else 0, 10 if any(c.isdigit() for c in password) else 0, 33 if any(not c.isalnum() for c in password) else 0])
        entropy = len(password) * math.log2(charset_size if charset_size > 0 else 1)
        score = min(int(entropy), 100)
        
        # 위험도 텍스트 판정
        risk_val = max(0, 100 - score)
        if risk_val < 30: risk_text, risk_color = "안전 (낮음)", "#22c55e"
        elif risk_val < 70: risk_text, risk_color = "주의 (중간)", "#f59e0b"
        else: risk_text, risk_color = "위험 (높음)", "#ef4444"
        
        c1, c2, c3 = st.columns(3)
        c1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        c2.metric("비밀번호 길이", f"{len(password)} 자")
        c3.metric("최종 보안 점수", f"{score}/100")
        
        st.markdown(f"""
        <div class="card" style="text-align:center;">
            <h3>공격 성공 확률</h3>
            <h1 style="font-size:60px; color:{risk_color};">{risk_val:.2f}%</h1>
            <h2 style="color:{risk_color};">위험도: {risk_text}</h2>
        </div>
        """, unsafe_allow_html=True)
        st.progress(risk_val / 100)
