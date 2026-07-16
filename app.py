import streamlit as st
import math
import pandas as pd

st.set_page_config(page_title="디지털 보안 연구 보고서", layout="wide")

# CSS 스타일링
st.markdown("""
<style>

.stApp{
background:
radial-gradient(circle at top,#1e3a8a 0%,transparent 35%),
linear-gradient(135deg,#020617,#0b1120);
color:#e2e8f0;
}


/* 전체 제목 */

h1{
font-size:42px;
font-weight:900;
color:#38bdf8;
text-shadow:0 0 20px rgba(56,189,248,0.5);
}

h2,h3{
color:#e0f2fe;
font-weight:800;
}


/* 연구 카드 */

.card{

background:
rgba(15,23,42,0.85);

backdrop-filter:blur(10px);

padding:28px;

border-radius:20px;

border:1px solid rgba(56,189,248,0.25);

box-shadow:
0 15px 35px rgba(0,0,0,0.45);

color:#f8fafc;

}


/* 탐구 과정 */

.step-box{

background:
linear-gradient(
90deg,
#172554,
#0f172a
);

padding:18px;

border-radius:14px;

margin-bottom:12px;

border-left:
5px solid #38bdf8;

font-weight:700;

color:#bae6fd;

}


/* Metric 카드 */

[data-testid="metric-container"]{

background:
linear-gradient(
145deg,
#111827,
#1e293b
);

border-radius:18px;

padding:22px;

border:

1px solid rgba(56,189,248,0.3);

box-shadow:
0 10px 25px rgba(0,0,0,0.4);

}


[data-testid="stMetricLabel"]{

color:#94a3b8;

font-size:15px;

}


[data-testid="stMetricValue"]{

color:#38bdf8;

font-size:32px;

font-weight:900;

}


/* 입력창 */

.stTextInput input{

background:#020617;

color:#f8fafc;

border:

1px solid #38bdf8;

border-radius:14px;

height:50px;

font-size:18px;

}


/* 버튼 및 진행바 */

.stProgress > div > div{

background:

linear-gradient(
90deg,
#2563eb,
#06b6d4,
#22c55e
);

}


/* 알림창 */

.stAlert{

background:#111827;

border-radius:15px;

border:1px solid #334155;

}


/* 사이드바 */

section[data-testid="stSidebar"]{

background:

linear-gradient(
180deg,
#020617,
#111827
);

border-right:

1px solid rgba(56,189,248,0.2);

}


/* 데이터프레임 */

[data-testid="stDataFrame"]{

border-radius:18px;

border:

1px solid #334155;

overflow:hidden;

}


</style>
""",unsafe_allow_html=True)
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

# [결론] - 핵심 요약 버전
    st.subheader("🎯 3. 결론 (종합적 탐구 결과)")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
          <div style="background:#1e293b; padding:15px; border-radius:10px; border-top: 5px solid #38bdf8; height: 100%;">
            <h4 style="color:#38bdf8;">암호학적 효율성</h4>
            무분별한 길이 연장은 인지 부하만 가중함. 핵심은 <b>단순 반복이 아닌, 높은 정보 밀도를 가진 문자 집합의 12자 이상 최적화</b>에 있음.
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div style="background:#1e293b; padding:15px; border-radius:10px; border-top: 5px solid #fbbf24; height: 100%;">
            <h4 style="color:#fbbf24;">인지적 효율성</h4>
            복잡성 규칙은 <b>인지적 마찰</b>을 유발함. <b>패스프레이즈(Passphrase)</b>는 암기 부하를 줄이면서도 정보량을 극대화하는 최적의 모델임.
        </div>
        """, unsafe_allow_html=True)
        
    with c3:
        st.markdown("""
        <div style="background:#1e293b; padding:15px; border-radius:10px; border-top: 5px solid #22c55e; height: 100%;">
            <h4 style="color:#22c55e;">보안적 경제성</h4>
            최적 보안은 기술과 행동의 <b>균형점</b>임. 12자 이상의 패스프레이즈는 연산 비용을 이득보다 높게 만드는 <b>경제적 방어선</b>임.
        </div>
        """, unsafe_allow_html=True)
  
    st.info("""
    💡 **핵심 결론**: 무작위 암기 불가능한 비밀번호는 보안 취약점을 만듭니다. 
    현실적인 해결책은 '패스프레이즈(Passphrase)'입니다. 
    단어 3~4개를 조합하여 12자리 이상의 문장을 만들면, 사용자는 기억하기 쉽고(길이 확보), 
    해커는 무차별 대입으로 뚫기 어려운 강력한 보안성을 가집니다.
    """)


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
        st.markdown("### 🕵️ 공격 성공 가능성 분석")

        st.markdown("### 🕵️ 보안 위험도 평가")

        attack_probability=max(0,100-score)

        risk_level="LOW" if attack_probability<30 else "MEDIUM" if attack_probability<70 else "HIGH"

        st.markdown(f"""
        <div style="
        background:linear-gradient(145deg,#020617,#111827);
        padding:35px;
        border-radius:25px;
        border:1px solid rgba(56,189,248,0.25);
        box-shadow:0 0 35px rgba(56,189,248,0.15);
        ">
        
        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        ">
        
        <div>
        
        <p style="
        color:#94a3b8;
        font-size:16px;
        margin:0;
        ">
        SECURITY RISK ASSESSMENT
        </p>
        
        <h1 style="
        font-size:60px;
        margin:10px 0;
        color:{color};
        ">
        {attack_probability:.2f}%
        </h1>
        
        <p style="
        color:#cbd5e1;
        font-size:18px;
        ">
        Estimated Password Compromise Risk
        </p>
        
        </div>
        
        
        <div style="
        background:{color};
        padding:18px 25px;
        border-radius:15px;
        color:white;
        font-size:24px;
        font-weight:900;
        ">
        {risk_level}
        </div>
        
        
        </div>
        
        
        <hr style="
        border:0;
        border-top:1px solid #334155;
        margin:25px 0;
        ">
        
        
        <div style="
        color:#94a3b8;
        font-size:15px;
        ">
        
        분석 모델 기준<br>
        • Shannon Entropy 기반 정보량 분석<br>
        • GPU Brute Force 공격 모델 적용<br>
        • 문자 집합 크기 및 길이 기반 평가<br>
        
        </div>
        
        
        </div>
        """,unsafe_allow_html=True)
        
                st.progress(attack_probability/100)
