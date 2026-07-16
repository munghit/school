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
    
    # 가독성을 위한 3단 카드 레이아웃
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div style="background:#1e293b; padding:15px; border-radius:10px; border-top: 5px solid #38bdf8; height: 100%;">
            <h4 style="color:#38bdf8;">🛡️ 보안 기술적 측면</h4>
            길이와 문자셋의 결합을 통한 <b>엔트로피 극대화</b>가 해킹 저항력 향상의 핵심임을 증명함.
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div style="background:#1e293b; padding:15px; border-radius:10px; border-top: 5px solid #fbbf24; height: 100%;">
            <h4 style="color:#fbbf24;">👤 사용자 측면</h4>
            무분별한 복잡성 요구는 오히려 보안 사고를 유발함. <b>12자리 이상의 적정 길이</b>가 사용성과 보안의 최적점.
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div style="background:#1e293b; padding:15px; border-radius:10px; border-top: 5px solid #22c55e; height: 100%;">
            <h4 style="color:#22c55e;">📈 최종 결과</h4>
            현대 컴퓨팅 환경에서 <b>[12자리 + 무작위 조합]</b>은 해독 불가능한 <b>'철통 보안'</b>의 표준임.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("💡 **결론 제언**: 향후 보안 시스템 설계는 사용자의 기억력을 저해하는 '복잡한 문자 강제' 정책에서 벗어나, '길이 기반의 엔트로피 확보' 정책으로 전환되어야 합니다.")
# --- 시뮬레이터 페이지 부분 ---
elif page == "🛡️ 보안성 시뮬레이터":
    st.title("🛡️ 실시간 보안 강도 분석기")
    st.markdown("---")

    password = st.text_input("비밀번호 입력", type="password", placeholder="분석할 비밀번호를 입력하세요")

    if password:
        # 엔트로피 계산
        charset_size = sum([26 if any(c.islower() for c in password) else 0,
                           26 if any(c.isupper() for c in password) else 0,
                           10 if any(c.isdigit() for c in password) else 0,
                           33 if any(not c.isalnum() for c in password) else 0])
        entropy = len(password) * math.log2(charset_size if charset_size > 0 else 1)
        score = min(int(entropy), 100)
        
        # 등급 판정
        if entropy < 40: level, color, icon = "매우 취약", "#ef4444", "🚨"
        elif entropy < 70: level, color, icon = "보통", "#f59e0b", "⚠️"
        elif entropy < 100: level, color, icon = "안전", "#3b82f6", "🔒"
        else: level, color, icon = "철통 보안", "#22c55e", "🛡️"

        # 대시보드
        st.subheader("🎯 종합 보안 등급")
        st.progress(score / 100)
        st.markdown(f'<div style="background:{color}; padding:15px; border-radius:10px; text-align:center; font-size:24px; color:white; font-weight:bold;">{icon} {level}</div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        col2.metric("비밀번호 길이", f"{len(password)} 자")
        col3.metric("최종 보안 점수", f"{score}/100")

        # 시뮬레이션
        st.markdown("### ⏱️ 공격자 대응 시뮬레이션")
        seconds = (2**entropy) / (10**10)
        time_str = f"{seconds:.2f} 초" if seconds < 60 else (f"{seconds/60:.2f} 분" if seconds < 3600 else (f"{seconds/3600:.2f} 시간" if seconds < 86400 else (f"{seconds/86400:.2f} 일" if seconds < 31536000 else f"{seconds/31536000:.2f} 년")))
        
        st.markdown(f"""
            <div style="background:#0f172a; padding:20px; border-radius:15px; border-left: 5px solid {color}; border-right: 5px solid {color}; text-align:center;">
                <p style="margin:0; color:#94a3b8;">현대적 GPU 브루트포스 공격 방어 시</p>
                <h2 style="margin:5px 0; color:white;">예상 해독 시간: <span style="color:{color};">{time_str}</span></h2>
            </div>
        """, unsafe_allow_html=True)

        # 상세 분석
        st.markdown("### 🔍 상세 구성 분석")
        c1, c2 = st.columns(2)
        
        with c1:
            st.markdown("#### ⚙️ 문자 구성 요소")
            elements = {"소문자 (a-z)": any(c.islower() for c in password), "대문자 (A-Z)": any(c.isupper() for c in password), "숫자 (0-9)": any(c.isdigit() for c in password), "특수문자 (!@#$%)": any(not c.isalnum() for c in password)}
            for name, ok in elements.items(): st.write(f"{'✅' if ok else '❌'} {name}")
        
        with c2:
            st.markdown("#### 🛡️ 보안 규정 준수 기준")
            standards = {"최소 권장 길이 (8자)": len(password) >= 8, "최적 보안 길이 (12자 이상)": len(password) >= 12, "복합 문자셋 (3종 이상)": sum([any(c.islower() for c in password), any(c.isupper() for c in password), any(c.isdigit() for c in password), any(not c.isalnum() for c in password)]) >= 3}
            for name, ok in standards.items(): st.write(f"{'✅' if ok else '❌'} {name}")

      # 위험도 강조 (소수점 2번째 자리까지)
        st.markdown("---")
        st.markdown("### 🕵️ 공격 성공 확률 (위험도)")
        
        attack_rate = max(0, 100 - score)
        
        st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <h1 style="font-size: 60px; color: {color}; margin: 0;">{attack_rate:.2f}%</h1>
                <p style="font-size: 20px; font-weight: bold; color: #94a3b8;">잠재적 해킹 침투 가능성</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.progress(attack_rate / 100)
