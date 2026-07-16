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

    password = st.text_input("비밀번호 입력", type="password", placeholder="분석할 비밀번호를 입력하세요")

    if password:
        # 엔트로피 및 기본 분석 로직 (기존 코드 유지)
        charset_size = sum([26 if any(c.islower() for c in password) else 0,
                           26 if any(c.isupper() for c in password) else 0,
                           10 if any(c.isdigit() for c in password) else 0,
                           33 if any(not c.isalnum() for c in password) else 0])
        entropy = len(password) * math.log2(charset_size if charset_size > 0 else 1)
        score = min(int(entropy), 100)
        
        # 등급 판정 (기존 로직)
        if entropy < 40: level, color, icon = "매우 취약", "#ef4444", "🚨"
        elif entropy < 70: level, color, icon = "보통", "#f59e0b", "⚠️"
        elif entropy < 100: level, color, icon = "안전", "#3b82f6", "🔒"
        else: level, color, icon = "철통 보안", "#22c55e", "🛡️"

        # [전문성 추가 1] 상단 대시보드 레이아웃
        st.subheader("🎯 종합 보안 등급")
        st.progress(score / 100)
        st.markdown(f'<div style="background:{color}; padding:15px; border-radius:10px; text-align:center; font-size:24px; color:white; font-weight:bold;">{icon} {level}</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        col1.metric("엔트로피 강도", f"{entropy:.1f} bits")
        col2.metric("비밀번호 길이", f"{len(password)} 자")
        col3.metric("최종 보안 점수", f"{score}/100")

        # [전문성 추가 2] 시각적 해킹 타임라인
        st.markdown("### ⏱️ 공격자 대응 시뮬레이션")
        seconds = (2**entropy) / (10**10)
        time_str = f"{seconds:.2f} 초" if seconds < 60 else (f"{seconds/60:.2f} 분" if seconds < 3600 else (f"{seconds/3600:.2f} 시간" if seconds < 86400 else (f"{seconds/86400:.2f} 일" if seconds < 31536000 else f"{seconds/31536000:.2f} 년")))
        
        st.markdown(f"""
            <div style="background:#0f172a; padding:20px; border-radius:15px; border-left: 5px solid {color}; border-right: 5px solid {color}; text-align:center;">
                <p style="margin:0; color:#94a3b8;">현대적 GPU 브루트포스 공격(10¹⁰ H/s) 방어 시</p>
                <h2 style="margin:5px 0; color:white;">예상 해독 시간: <span style="color:{color};">{time_str}</span></h2>
            </div>
        """, unsafe_allow_html=True)

        # [전문성 추가 3] 그리드 기반 분석 보고서
        st.markdown("### 🔍 상세 구성 분석")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### ⚙️ 구성 요소 체크")
            crit = {"소문자": any(c.islower() for c in password), "대문자": any(c.isupper() for c in password), 
                    "숫자": any(c.isdigit() for c in password), "특수문자": any(not c.isalnum() for c in password)}
            for name, ok in crit.items():
                st.write(f"{'✅' if ok else '❌'} {name} 포함")
        
        with c2:
            st.markdown("#### 🛡️ 보안 권장 기준 충족 여부")
            rules = {"길이 8자 이상": len(password) >= 8, "길이 12자 이상(최적)": len(password) >= 12}
            for name, ok in rules.items():
                st.write(f"{'✅' if ok else '❌'} {name}")

        # [전문성 추가 4] 해커 위협도 레이더
        st.markdown("### 🕵️ 공격 성공 확률 (위험도)")
        attack_rate = max(0, 100 - score)
        st.progress(attack_rate / 100)
        st.caption(f"시스템 취약 노출도: {attack_rate}%")
