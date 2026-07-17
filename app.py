import streamlit as st
import math
import plotly.graph_objects as go

st.set_page_config(page_title="보안 연구 상세 보고서",layout="wide")

st.markdown("""
<style>
.stApp{
background:
radial-gradient(circle at top left,#172554,transparent 35%),
radial-gradient(circle at bottom right,#312e81,transparent 35%),
#020617;
color:#e2e8f0;
}
p,li{
color:#dbeafe;
font-size:17px;
line-height:1.7;
}
h1{
color:#7dd3fc!important;
font-size:42px!important;
font-weight:900;
}
h2{
color:#a5b4fc!important;
font-weight:800;
}
h3{
color:#67e8f9!important;
}
.content-box{
background:
linear-gradient(
145deg,
rgba(30,41,59,.95),
rgba(15,23,42,.95)
);
padding:30px;
border-radius:20px;
border:1px solid #334155;
box-shadow:0 10px 25px rgba(0,0,0,.25);
margin-bottom:20px;
transition:.3s;
}
.content-box:hover{
transform:translateY(-3px);
border:1px solid #38bdf8;
box-shadow:0 15px 30px rgba(0,0,0,.35);
}
section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#020617,#111827);
}
section[data-testid="stSidebar"] label{
color:#7dd3fc!important;
font-weight:700;
}
.stTextInput input{
background:#0f172a!important;
color:white!important;
border-radius:15px!important;
border:1px solid #38bdf8!important;
font-size:18px;
}
.stProgress>div>div>div{
background:linear-gradient(90deg,#38bdf8,#818cf8);
}
li::marker{
color:#38bdf8;
}
.score-card{
border:1px solid #38bdf8;
}
.metric-card{
background:
linear-gradient(
145deg,
rgba(15,23,42,.95),
rgba(30,64,175,.35)
);
padding:25px;
border-radius:20px;
border:1px solid #334155;
text-align:center;
}
.metric-number{
font-size:35px;
font-weight:900;
color:#38bdf8;
}
</style>
""",unsafe_allow_html=True)

menu=st.sidebar.radio(
"발표 섹션",
[
"서론: 연구 배경",
"본론 1: 이론적 배경",
"본론 2: 실태 및 문제점",
"본론 3: 해결 방안 및 구현",
"시뮬레이션: 보안 실증",
"결론: 연구 결과"
])

if menu=="서론: 연구 배경":

    st.title("🛡️ 디지털 보안 연구")

    st.markdown("""
<div class="content-box">
<h2>연구 배경</h2>
<p>
디지털 서비스 증가와 함께 개인정보 보호의 중요성이 커지고 있습니다.
그러나 많은 사용자는 편리함을 위해 단순한 비밀번호를 사용하고 있으며,
이는 개인정보 유출 위험으로 이어지고 있습니다.
</p>
</div>
""",unsafe_allow_html=True)

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown("""
<div class="metric-card">
<h3>🔑 Password</h3>
<div class="metric-number">
1st
</div>
<p>
첫 번째 보안 방어선
</p>
</div>
""",unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="metric-card">
<h3>⚠️ Risk</h3>
<div class="metric-number">
↑
</div>
<p>
디지털 위협 증가
</p>
</div>
""",unsafe_allow_html=True)

    with c3:
        st.markdown("""
<div class="metric-card">
<h3>🛡 Defense</h3>
<div class="metric-number">
AI
</div>
<p>
데이터 기반 보안 필요
</p>
</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="content-box">

<h3>연구 목표</h3>

<ul>
<li>비밀번호가 보안의 첫 번째 방어선임을 이론적으로 분석</li>
<li>사용자의 보안 인식과 실제 행동 사이의 차이를 확인</li>
<li>데이터 기반 시뮬레이션을 통해 능동적인 보안 습관 형성 유도</li>
</ul>

</div>
""",unsafe_allow_html=True)


elif menu=="본론 1: 이론적 배경":

    st.title("📖 이론적 배경 상세")

    c1,c2=st.columns(2)

    with c1:
        st.markdown("""
<div class="content-box">
<h3>1. 정보보호와 비밀번호</h3>
<ul>
<li><b>인증의 기본:</b> 비밀번호는 인가자와 침입자를 구분하는 핵심 인증 수단입니다.</li>
<li><b>관리 가이드:</b> 영문, 숫자, 특수문자 조합은 공격 가능성을 낮추는 기본 전략입니다.</li>
</ul>
</div>
""",unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="content-box">
<h3>2. 공격 원리와 복잡도</h3>
<ul>
<li><b>무차별 대입 공격:</b> 가능한 모든 조합을 탐색하는 방식으로 비밀번호 길이에 따라 시간이 증가합니다.</li>
<li><b>보안 수학:</b> 문자 집합 크기와 길이 증가는 조합 공간을 지수적으로 증가시킵니다.</li>
</ul>
</div>
""",unsafe_allow_html=True)


elif menu=="본론 2: 실태 및 문제점":

    st.title("⚠️ 현황 및 문제점 분석")

    st.markdown("""
<div class="content-box">
<h3>사용자 보안 실태: 편리함의 역설</h3>
<p>
많은 사용자는 보안보다 기억하기 쉬운 비밀번호를 선호합니다.
이는 동일한 비밀번호 반복 사용과 개인정보 노출 위험 증가로 이어집니다.
</p>
</div>
""",unsafe_allow_html=True)

    c1,c2=st.columns(2)

    with c1:
        st.markdown("""
<div class="content-box">
<h3>기술적 취약점</h3>
<ul>
<li><b>사전 공격:</b> 자주 사용하는 단어나 패턴을 기반으로 공격합니다.</li>
<li><b>비밀번호 재사용:</b> 하나의 정보 유출이 여러 계정 위험으로 연결됩니다.</li>
</ul>
</div>
""",unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="content-box">
<h3>인지적 취약점</h3>
<ul>
<li><b>보안 기준 부족:</b> 사용자는 안전한 비밀번호 수준을 직접 판단하기 어렵습니다.</li>
<li><b>행동과 인식 차이:</b> 중요성은 알지만 실천으로 이어지지 않는 문제가 존재합니다.</li>
</ul>
</div>
""",unsafe_allow_html=True)


elif menu=="본론 3: 해결 방안 및 구현":

    st.title("💡 개선 방안 및 기술 스택")

    st.markdown("""
<div class="content-box">
<h3>제도적·기술적 대응</h3>
<ul>
<li><b>다중 인증(MFA/2FA):</b> 비밀번호 외 추가 인증을 통해 보안을 강화합니다.</li>
<li><b>비밀번호 관리자:</b> 복잡한 비밀번호 생성과 관리를 자동화합니다.</li>
</ul>
</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="content-box">
<h3>구현 환경 및 혁신</h3>
<ul>
<li><b>Streamlit:</b> 사용자의 입력 데이터를 기반으로 실시간 보안 분석 환경 구현</li>
<li><b>GitHub:</b> 코드 관리 및 프로젝트 공유 환경 구축</li>
<li><b>체험형 보안:</b> 단순 교육에서 벗어나 직접 경험하는 보안 분석 시스템 구축</li>
</ul>
</div>
""",unsafe_allow_html=True)


elif menu=="시뮬레이션: 보안 실증":

    st.title("🛡️ 실시간 보안성 시뮬레이터")

    pw=st.text_input(
        "🔑 테스트할 비밀번호를 입력하세요",
        type="password"
    )

    if pw:

        length_score=min(len(pw)*10,100)

        upper_score=100 if any(c.isupper() for c in pw) else 0
        lower_score=100 if any(c.islower() for c in pw) else 0
        digit_score=100 if any(c.isdigit() for c in pw) else 0
        special_score=100 if any(not c.isalnum() for c in pw) else 0

        score=int(
            length_score*0.35+
            upper_score*0.15+
            lower_score*0.15+
            digit_score*0.15+
            special_score*0.20
        )

        score=min(score,100)

        status,color=(
            ("안전","#22c55e")
            if score>=70
            else ("주의","#f59e0b")
            if score>=40
            else ("위험","#ef4444")
        )

        c1,c2=st.columns([1,2])

        with c1:

            st.markdown(f"""
<div class="content-box score-card">

<h3>🛡️ 보안 점수</h3>

<h1 style="color:{color};font-size:75px;">
{score}
</h1>

<p>
평가 :
<b style="color:{color}">
{status}
</b>
</p>

</div>
""",unsafe_allow_html=True)

        with c2:

            st.markdown("""
<div class="content-box">

<h3>🔍 분석 상세</h3>

<ul>
<li><b>길이:</b> 긴 비밀번호일수록 가능한 조합 수 증가</li>
<li><b>문자 조합:</b> 다양한 문자 사용은 공격 난이도 증가</li>
<li><b>결과:</b> 입력된 비밀번호의 보안 수준 분석</li>
</ul>

</div>
""",unsafe_allow_html=True)

        st.progress(score/100)


        st.markdown("---")

        st.subheader("📡 보안 요소 분석 레이더")

        radar_categories=[
            "길이",
            "대문자",
            "소문자",
            "숫자",
            "특수문자"
        ]

        radar_values=[
            length_score,
            upper_score,
            lower_score,
            digit_score,
            special_score
        ]

        radar_categories.append(radar_categories[0])
        radar_values.append(radar_values[0])

        fig=go.Figure(
            go.Scatterpolar(
                r=radar_values,
                theta=radar_categories,
                fill="toself",
                line=dict(
                    color="#38bdf8",
                    width=3
                )
            )
        )

        fig.update_layout(
            polar=dict(
                bgcolor="#0f172a",
                radialaxis=dict(
                    visible=True,
                    range=[0,100],
                    color="#cbd5e1"
                ),
                angularaxis=dict(
                    color="#cbd5e1"
                )
            ),
            height=450,
            showlegend=False,
            margin=dict(
                l=40,
                r=40,
                t=30,
                b=30
            ),
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(
                color="#e2e8f0"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


        st.markdown("---")

        st.subheader("⏱️ 예상 무차별 대입 공격 시간")


        charset=0

        if any(c.islower() for c in pw):
            charset+=26

        if any(c.isupper() for c in pw):
            charset+=26

        if any(c.isdigit() for c in pw):
            charset+=10

        if any(not c.isalnum() for c in pw):
            charset+=32


        combinations=charset**len(pw)

        attack_seconds=combinations/1_000_000_000


        if attack_seconds<60:
            attack_time=f"{attack_seconds:.2f}초"

        elif attack_seconds<3600:
            attack_time=f"{attack_seconds/60:.2f}분"

        elif attack_seconds<86400:
            attack_time=f"{attack_seconds/3600:.2f}시간"

        elif attack_seconds<31536000:
            attack_time=f"{attack_seconds/86400:.2f}일"

        else:
            attack_time=f"{attack_seconds/31536000:.2f}년"


        st.markdown(f"""
<div class="content-box">

<h3>🔓 공격 시뮬레이션 결과</h3>

<p>
가능한 비밀번호 조합 수:
<b>{combinations:,}</b>
</p>

<p>
기준:
초당 10억 번의 대입 공격
</p>

<h2 style="color:#38bdf8;">
예상 공격 시간 : {attack_time}
</h2>

</div>
""",unsafe_allow_html=True)



elif menu=="결론: 연구 결과":

    st.title("📌 연구 결과 및 의의")


    c1,c2=st.columns(2)


    with c1:

        st.markdown("""
<div class="content-box">

<h3>Before ❌</h3>

<ul>
<li>단순한 비밀번호 사용</li>
<li>보안 수준 판단 어려움</li>
<li>추상적인 보안 교육</li>
</ul>

</div>
""",unsafe_allow_html=True)


    with c2:

        st.markdown("""
<div class="content-box">

<h3>After ✅</h3>

<ul>
<li>데이터 기반 보안 분석</li>
<li>실시간 위험 수준 확인</li>
<li>체험형 보안 학습 가능</li>
</ul>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2>🛡️ 연구 의의</h2>

<p>
본 연구는 비밀번호 보안을 단순한 규칙 암기가 아닌,
데이터 기반 분석과 실시간 피드백을 통해
사용자가 직접 이해하고 개선할 수 있는
체험형 보안 시스템으로 확장하였습니다.
</p>

<h2 style="text-align:center;color:#38bdf8;">
"보안은 기술이 아니라 올바른 판단을 돕는 데이터입니다."
</h2>

</div>
""",unsafe_allow_html=True)
