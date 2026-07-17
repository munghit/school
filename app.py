import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="Digital Security Lab", layout="wide")

st.markdown("""
<style>
/* 애니메이션 효과 */
@keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
.fade-in { animation: fadeIn 0.8s ease-out; }

/* 전체 스타일 */
.stApp { background:#020617; color:#e2e8f0; }
.nav-header { background: #0f172a; padding: 20px; border-radius: 0 0 20px 20px; border-bottom: 2px solid #38bdf8; text-align: center; margin-bottom: 30px; }

/* 카드 스타일 고도화 */
.card { background: linear-gradient(145deg, #111827, #1e293b); padding: 30px; border-radius: 20px; border: 1px solid #334155; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
.metric-card { background: #0f172a; padding: 20px; border-radius: 15px; border-left: 5px solid #38bdf8; }

/* 텍스트 스타일 */
h1 { color:#38bdf8; text-align: center; margin-bottom: 0; }
.sub-title { color:#94a3b8; text-align: center; margin-bottom: 30px; }
</style>
""", unsafe_allow_html=True)

# 헤더 영역
st.markdown('<div class="nav-header"><h1>🛡️ Digital Security Intelligence</h1><p class="sub-title">암호학적 분석 및 실시간 보안 강도 평가 시스템</p></div>', unsafe_allow_html=True)

st.sidebar.title("📌 연구 메뉴")
page = st.sidebar.radio("Navigate", ["📂 연구 종합 보고서", "🛡️ 보안성 시뮬레이터"])

if page == "📂 연구 종합 보고서":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("📂 종합 연구 보고서")
    
    # 3단 구조 결론을 최상단으로 올려 웹사이트 요약 느낌 강조
    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1: st.markdown('<div class="card"><h4>암호학적 효율성</h4>지수적인 길이 증가가 계산 복잡도를 압도함.</div>', unsafe_allow_html=True)
    with col_k2: st.markdown('<div class="card"><h4>인지적 효율성</h4>패스프레이즈 모델로 기억 부하와 보안성을 동시 확보.</div>', unsafe_allow_html=True)
    with col_k3: st.markdown('<div class="card"><h4>보안적 경제성</h4>연산 비용을 이득보다 높게 만드는 경제적 방어선.</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    # 이후 기존 내용 배치...
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🛡️ 보안성 시뮬레이터":
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.title("🛡️ 보안성 시뮬레이션")
    
    # 입력창 스타일 강화
    password = st.text_input("🔑 보안 점검을 위해 비밀번호를 입력하세요.", type="password", placeholder="비밀번호 입력...")
    
    if password:
        # (기존 로직 동일)
        charset_size = sum([26 if any(c.islower() for c in password) else 0, 26 if any(c.isupper() for c in password) else 0, 10 if any(c.isdigit() for c in password) else 0, 33 if any(not c.isalnum() for c in password) else 0])
        entropy = len(password) * math.log2(charset_size if charset_size > 0 else 1)
        score = min(int(entropy), 100)
        
        # 등급별 테마
        if entropy < 40: level, color, icon = "매우 위험", "#ef4444", "🚨"
        elif entropy < 70: level, color, icon = "보통", "#f59e0b", "⚠️"
        elif entropy < 100: level, color, icon = "안전", "#3b82f6", "🔒"
        else: level, color, icon = "매우 안전", "#22c55e", "🛡️"

        # 시각적 레이아웃 구성
        row1 = st.columns(3)
        row1[0].metric("엔트로피", f"{entropy:.2f} bits")
        row1[1].metric("비밀번호 길이", f"{len(password)}자")
        row1[2].metric("종합 점수", f"{score}/100")
        
        st.markdown(f'<div style="margin-top:20px; text-align:center; padding:20px; border: 2px solid {color}; border-radius:15px;"><h2>{icon} 보안 등급: {level}</h2></div>', unsafe_allow_html=True)
        
    st.markdown('</div>', unsafe_allow_html=True)
