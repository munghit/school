import streamlit as st
import plotly.graph_objects as go
import math

st.set_page_config(
    page_title="디지털 보안 연구 분석 시스템",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background:#f5f7f6;
    color:#263238;
}
h1{
    color:#17324d!important;
    font-size:40px!important;
    font-weight:800;
}
h2{
    color:#234e70!important;
    font-weight:750;
}
h3{
    color:#37474f!important;
}
p,li{
    color:#455a64;
    font-size:18px;
    line-height:1.7;
}
.content-box{
    background:#ffffff;
    padding:22px;
    border-radius:14px;
    border:1px solid #d9e2e3;
    box-shadow:0 3px 10px rgba(0,0,0,0.05);
    margin-bottom:12px;
}
.metric-card{
    background:#ffffff;
    padding:18px;
    border-radius:14px;
    border:1px solid #d9e2e3;
    text-align:center;
    box-shadow:0 3px 8px rgba(0,0,0,0.04);
}
.metric-number{
    font-size:36px;
    font-weight:800;
    color:#1565c0;
}
.report-card{
    background:#ffffff;
    padding:18px;
    border-radius:12px;
    border-left:5px solid #1976a8;
}
.safe{
    color:#2e7d32;
    font-weight:800;
}
.warning{
    color:#ef6c00;
    font-weight:800;
}
.danger{
    color:#c62828;
    font-weight:800;
}
section[data-testid="stSidebar"]{
    background:#ffffff;
    border-right:1px solid #d9e2e3;
}
section[data-testid="stSidebar"] label{
    color:#234e70!important;
    font-weight:700;
}
.stTextInput input{
    background:#ffffff!important;
    color:#263238!important;
    border:1px solid #b0bec5!important;
    border-radius:8px!important;
}
.stProgress>div>div>div{
    background:#1976a8;
}
</style>
""",unsafe_allow_html=True)


menu=st.sidebar.radio(
    "연구 분석 메뉴",
    [
        "📌 연구 개요",
        "📚 이론적 배경",
        "📈 보안 취약성 분석",
        "⚙️ 시스템 구현",
        "🧪 실험 및 결과",
        "🎯 결론 및 의의"
    ]
)


if menu=="📌 연구 개요":

    st.title("🛡️ 디지털 환경에서의 비밀번호 보안성 분석 연구")

    st.markdown("""
<div class="content-box">

<h2>연구 배경</h2>

<p>
디지털 서비스의 확산으로 개인정보 보호의 중요성이 증가하고 있습니다.
하지만 많은 사용자는 기억하기 쉬운 비밀번호를 사용하거나
동일한 비밀번호를 반복 사용하며 보안 위협에 노출되고 있습니다.
</p>

</div>
""",unsafe_allow_html=True)


    c1,c2,c3=st.columns(3)


    with c1:
        st.markdown("""
<div class="metric-card">
<h3>🔑 Password</h3>
<div class="metric-number">1st</div>
<p>디지털 보안의 첫 단계</p>
</div>
""",unsafe_allow_html=True)


    with c2:
        st.markdown("""
<div class="metric-card">
<h3>⚠️ Risk</h3>
<div class="metric-number">↑</div>
<p>사이버 위협 증가</p>
</div>
""",unsafe_allow_html=True)


    with c3:
        st.markdown("""
<div class="metric-card">
<h3>🛡 Analysis</h3>
<div class="metric-number">AI</div>
<p>데이터 기반 평가</p>
</div>
""",unsafe_allow_html=True)


    st.markdown("""
<div class="content-box">

<h2>연구 목적</h2>

<ul>
<li>비밀번호 보안성을 정량적으로 평가</li>
<li>사용자가 자신의 보안 수준을 직접 확인</li>
<li>데이터 기반 분석을 통한 보안 의식 향상</li>
</ul>

</div>
""",unsafe_allow_html=True)


    st.markdown("""
<div class="content-box">

<h2>연구 진행 과정</h2>

<p>
문제 정의 → 보안 이론 분석 → 평가 기준 설계 → 시스템 구현 → 결과 분석
</p>

</div>
""",unsafe_allow_html=True)

elif menu=="📚 이론적 배경":

    st.title("📚 이론적 배경")

    c1,c2=st.columns(2)

    with c1:
        st.markdown("""
<div class="content-box">

<h2>1. 정보보호와 비밀번호</h2>

<ul>
<li><b>인증:</b> 비밀번호는 사용자의 신원을 확인하는 기본 보안 수단입니다.</li>
<li><b>복잡도:</b> 문자 종류와 길이가 증가할수록 공격 가능성이 감소합니다.</li>
<li><b>관리:</b> 안전한 저장과 관리 방식이 중요합니다.</li>
</ul>

</div>
""",unsafe_allow_html=True)


    with c2:
        st.markdown("""
<div class="content-box">

<h2>2. 공격 원리와 보안성</h2>

<ul>
<li><b>Brute Force:</b> 가능한 모든 조합을 탐색하는 공격 방식입니다.</li>
<li><b>Dictionary Attack:</b> 자주 사용되는 단어와 패턴을 이용합니다.</li>
<li><b>조합 공간:</b> 문자 집합(N)과 길이(L)에 따라 N<sup>L</sup> 형태로 증가합니다.</li>
</ul>

</div>
""",unsafe_allow_html=True)


    st.markdown("""
<div class="content-box">

<h2>비밀번호 보안 평가 요소</h2>

</div>
""",unsafe_allow_html=True)



    a,b,c=st.columns(3)


    with a:
        st.markdown("""
<div class="metric-card">

<h3>Length</h3>

<div class="metric-number">
L
</div>

<p>비밀번호 길이</p>

</div>
""",unsafe_allow_html=True)



    with b:
        st.markdown("""
<div class="metric-card">

<h3>Character</h3>

<div class="metric-number">
N
</div>

<p>문자 종류</p>

</div>
""",unsafe_allow_html=True)



    with c:
        st.markdown("""
<div class="metric-card">

<h3>Entropy</h3>

<div class="metric-number">
H
</div>

<p>정보량</p>

</div>
""",unsafe_allow_html=True)



elif menu=="📈 보안 취약성 분석":

    st.title("📈 보안 취약성 분석")


    st.markdown("""
<div class="content-box">

<h2>사용자 보안 실태</h2>

<p>
디지털 서비스 이용 증가에도 불구하고 많은 사용자는
편의성을 우선하여 단순한 비밀번호를 선택합니다.
이는 비밀번호 재사용과 예측 가능성 증가로 이어집니다.
</p>

</div>
""",unsafe_allow_html=True)



    c1,c2=st.columns(2)



    with c1:

        st.markdown("""
<div class="content-box">

<h2>기술적 취약점</h2>

<ul>

<li>
<b>사전 공격</b><br>
자주 사용되는 단어나 패턴을 기반으로 공격
</li>

<li>
<b>무차별 대입 공격</b><br>
모든 가능한 조합을 반복 탐색
</li>

<li>
<b>비밀번호 재사용</b><br>
한 계정 유출이 다른 계정 위험으로 확대
</li>

</ul>

</div>
""",unsafe_allow_html=True)



    with c2:

        st.markdown("""
<div class="content-box">

<h2>사용자 측 취약점</h2>

<ul>

<li>
<b>판단 어려움</b><br>
자신의 비밀번호 안전성을 객관적으로 확인하기 어려움
</li>

<li>
<b>보안 피로</b><br>
복잡한 규칙 적용에 대한 부담 증가
</li>

<li>
<b>인식과 행동 차이</b><br>
중요성 인식에 비해 실천 부족
</li>

</ul>

</div>
""",unsafe_allow_html=True)

elif menu=="⚙️ 시스템 구현":

    st.title("⚙️ 시스템 구현")

    st.markdown("""
<div class="content-box">

<h2>구현 목표</h2>

<p>
사용자가 입력한 비밀번호를 기반으로
보안 요소를 분석하고, 정량적인 보안 점수와
시각화 결과를 제공하는 체험형 분석 시스템을 구현하였습니다.
</p>

</div>
""",unsafe_allow_html=True)



    c1,c2,c3=st.columns(3)


    with c1:
        st.markdown("""
<div class="metric-card">

<h3>Streamlit</h3>

<div class="metric-number">
UI
</div>

<p>웹 인터페이스 구축</p>

</div>
""",unsafe_allow_html=True)



    with c2:
        st.markdown("""
<div class="metric-card">

<h3>Python</h3>

<div class="metric-number">
⚙️
</div>

<p>보안 분석 알고리즘</p>

</div>
""",unsafe_allow_html=True)



    with c3:
        st.markdown("""
<div class="metric-card">

<h3>Plotly</h3>

<div class="metric-number">
📊
</div>

<p>데이터 시각화</p>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2>시스템 구성</h2>

<ul>

<li>
<b>입력 단계</b><br>
사용자가 비밀번호 입력
</li>

<li>
<b>분석 단계</b><br>
길이, 문자 종류, 엔트로피 분석
</li>

<li>
<b>출력 단계</b><br>
보안 점수와 위험도 시각화
</li>

</ul>

</div>
""",unsafe_allow_html=True)

elif menu=="🧪 실험 및 결과":

    st.title("🧪 Password Security Analyzer")

    st.markdown("""
<div class="content-box">

<h2>🔐 비밀번호 보안 분석 시스템</h2>

<p>
입력한 비밀번호를 기반으로 길이,
문자 구성, 엔트로피, 공격 가능성을 분석하여
보안 수준을 평가합니다.
</p>

</div>
""",unsafe_allow_html=True)

    pw=st.text_input(
        "🔑 분석할 비밀번호 입력",
        type="password",
        placeholder="비밀번호 입력"
    )

    if pw:
        # --- 수정된 계산 로직 (입력값에 맞게 실시간 반영) ---
        length = len(pw)
        has_upper = any(c.isupper() for c in pw)
        has_lower = any(c.islower() for c in pw)
        has_digit = any(c.isdigit() for c in pw)
        has_special = any(not c.isalnum() for c in pw)

        length_score = min(length * 8, 100)
        variety_score = (has_upper + has_lower + has_digit + has_special) * 25
        score = int(length_score * 0.4 + variety_score * 0.6)
        score = min(score, 100)
        # --------------------------------------------

        if score>=70:
            status="안전"
            color="#2e7d32"
        elif score>=40:
            status="주의"
            color="#ef6c00"
        else:
            status="위험"
            color="#c62828"

        left,right=st.columns([1,2])

        with left:
            st.markdown(f"""
<div class="content-box" style="text-align:center">

<h3>Security Score</h3>

<h1 style="font-size:75px;color:{color}">
{score}
</h1>

<h2 style="color:{color}">
{status}
</h2>

</div>
""",unsafe_allow_html=True)

        with right:
            missing=[]
            if not has_upper: missing.append("대문자")
            if not has_lower: missing.append("소문자")
            if not has_digit: missing.append("숫자")
            if not has_special: missing.append("특수문자")

            result=f"부족 요소: {', '.join(missing)}" if missing else "모든 보안 요소 충족"

            st.markdown(f"""
<div class="content-box">

<h2>🔍 분석 결과</h2>

<ul>

<li>
<b>비밀번호 길이:</b>
{length}자리
</li>

<li>
<b>문자 구성:</b>
{result}
</li>

<li>
<b>평가 결과:</b>
현재 비밀번호는
<b style="color:{color}">
{status}
</b>
수준입니다.
</li>

</ul>

</div>
""",unsafe_allow_html=True)

        st.progress(score/100)
        st.markdown("---")
        st.subheader("📊 보안 요소 분석")

        categories=["길이", "대문자", "소문자", "숫자", "특수문자"]
        # 점수 재정의
        values = [length_score, 100 if has_upper else 0, 100 if has_lower else 0, 100 if has_digit else 0, 100 if has_special else 0]

        fig=go.Figure()
        fig.add_trace(go.Scatterpolar(r=values, theta=categories, fill="toself", line=dict(color="#1976a8", width=3), fillcolor="rgba(25,118,168,0.18)"))
        fig.update_layout(polar=dict(bgcolor="#ffffff", radialaxis=dict(visible=True, range=[0,100], color="#37474f"), angularaxis=dict(color="#37474f")), showlegend=False, height=480, paper_bgcolor="#ffffff")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("---")
        st.subheader("🔐 엔트로피 분석")

        charset = (26 if has_lower else 0) + (26 if has_upper else 0) + (10 if has_digit else 0) + (32 if has_special else 0)
        entropy = length * math.log2(charset) if charset > 0 else 0

        if entropy<40: entropy_status, entropy_color = "낮음", "#c62828"
        elif entropy<70: entropy_status, entropy_color = "보통", "#ef6c00"
        else: entropy_status, entropy_color = "높음", "#2e7d32"

        st.markdown(f"""
<div class="content-box">
<h2>Password Entropy</h2>
<h1 style="color:{entropy_color}">{entropy:.2f} bits</h1>
<p>현재 엔트로피 수준: <b style="color:{entropy_color}">{entropy_status}</b></p>
</div>
""",unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("⚔️ 공격 유형별 위험도 분석")
        attack1,attack2,attack3=st.columns(3)
        dictionary = "🔴 높음" if length < 8 else "🟢 낮음"
        brute = "🔴 높음" if entropy < 50 else ("🟡 보통" if entropy < 80 else "🟢 낮음")
        pattern = "🔴 높음" if (pw.isdigit() or pw.lower()==pw) else "🟡 보통"

        for col, title, val in zip([attack1, attack2, attack3], ["Dictionary Attack", "Brute Force", "Pattern Attack"], [dictionary, brute, pattern]):
            with col:
                st.markdown(f'<div class="metric-card"><h3>{title}</h3><div class="metric-number">{val}</div></div>', unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("⏱️ 무차별 대입 공격 시뮬레이션")
        combinations = charset**length if charset > 0 else 0
        attack_seconds = combinations/1_000_000_000
        if attack_seconds < 60: attack_time = f"{attack_seconds:.2f}초"
        elif attack_seconds < 3600: attack_time = f"{attack_seconds/60:.2f}분"
        elif attack_seconds < 86400: attack_time = f"{attack_seconds/3600:.2f}시간"
        elif attack_seconds < 31536000: attack_time = f"{attack_seconds/86400:.2f}일"
        else: attack_time = f"{attack_seconds/31536000:.2f}년"

        st.markdown(f"""
<div class="content-box">
<h2>공격 시뮬레이션 결과</h2>
<ul><li>가능한 조합: <b>{combinations:,}</b></li></ul>
<h1 style="color:#1976a8">예상 공격 시간 : {attack_time}</h1>
</div>
""",unsafe_allow_html=True)

elif menu=="🎯 결론 및 의의":

    st.title("🎯 연구 결과 및 의의")


    c1,c2=st.columns(2)


    with c1:

        st.markdown("""
<div class="content-box">

<h2>기존 보안 방식</h2>

<ul>

<li>
비밀번호 규칙 암기 중심
</li>

<li>
사용자가 보안 수준을 직접 판단하기 어려움
</li>

<li>
위험성을 체감하기 어려움
</li>

</ul>

</div>
""",unsafe_allow_html=True)



    with c2:

        st.markdown("""
<div class="content-box">

<h2>제안 시스템</h2>

<ul>

<li>
비밀번호 보안성 정량 평가
</li>

<li>
엔트로피 기반 분석
</li>

<li>
공격 위험도 시각화
</li>

<li>
실시간 보안 피드백 제공
</li>

</ul>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2>연구 성과</h2>

<ul>

<li>
비밀번호 보안 요소를 기반으로 평가 알고리즘 구현
</li>

<li>
레이더 차트를 활용한 보안 수준 시각화
</li>

<li>
엔트로피와 공격 시뮬레이션을 통한 위험성 표현
</li>

<li>
사용자가 직접 체험할 수 있는 디지털 보안 분석 시스템 구축
</li>

</ul>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2 style="text-align:center;color:#234e70">
"보안은 단순한 규칙이 아니라,
데이터를 통해 이해하고 개선하는 과정이다."
</h2>


<p style="text-align:center">

본 연구는 사용자가 자신의 비밀번호 보안 수준을
직접 확인하고 데이터 기반 분석을 통해
안전한 디지털 환경을 구축할 수 있도록 지원하는
체험형 보안 분석 시스템 구현을 목표로 하였습니다.

</p>

</div>
""",unsafe_allow_html=True)
