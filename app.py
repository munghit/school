import streamlit as st
import math

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
</style>
""",unsafe_allow_html=True)

menu=st.sidebar.radio(
"발표 섹션",
[
"서론: 연구 배경",
"본론 1: 이론적 배경",
"본론 2: 실태 및 문제점",
"본론 3: 해결 방안 및 구현",
"시뮬레이션: 보안 실증"
])

if menu=="서론: 연구 배경":
    st.title("🛡️ 디지털 보안 연구")
    st.markdown("""
<div class="content-box">
<h2>연구 동기 및 목적</h2>
<p>
본 연구는 현대 디지털 환경에서 개인정보 보호의 핵심인 비밀번호 보안성을 재조명합니다.
<b>KISA 및 국가정보원의 가이드라인</b>을 근거로,
단순 암기 위주의 구태의연한 보안 교육에서 벗어나고자 합니다.
</p>
<h3>연구 목표</h3>
<ul>
<li>비밀번호가 보안의 첫 번째 방어선임을 이론적으로 규명함</li>
<li>사용자의 보안 의식과 실제 행위 사이의 괴리를 데이터로 증명함</li>
<li>데이터 기반 실시간 시뮬레이션을 통해 <b>능동적인 보안 습관 형성</b>을 유도함</li>
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
<li><b>인증의 기본:</b> 비밀번호는 인가자와 침입자를 분리하는 필수 인증 수단임.</li>
<li><b>관리 가이드:</b> KISA는 영문, 숫자, 특수문자 혼합을 권고하며 이는 공격 표면을 줄이는 핵심 전략임.</li>
</ul>
</div>
""",unsafe_allow_html=True)
    with c2:
        st.markdown("""
<div class="content-box">
<h3>2. 공격 원리와 복잡도</h3>
<ul>
<li><b>무차별 대입(Brute Force):</b> 가능한 조합을 순차 대입하는 공격. 해킹 시간은 <b>N^L</b> 관계를 가짐.</li>
<li><b>보안 수학:</b> 문자 집합 크기와 길이 증가가 방어 비용을 기하급수적으로 증가시킴.</li>
</ul>
</div>
""",unsafe_allow_html=True)

elif menu=="본론 2: 실태 및 문제점":
    st.title("⚠️ 현황 및 문제점 분석")
    st.markdown("""
<div class="content-box">
<h3>사용자 보안 실태: 편리함의 역설</h3>
<p>
디지털 서비스 폭증에도 불구하고,
다수 사용자는 여전히 보안보다 편리함을 우선시합니다.
이는 단순 숫자 위주의 비밀번호 재사용 문제로 직결됩니다.
</p>
</div>
""",unsafe_allow_html=True)
    c1,c2=st.columns(2)


    with c1:
        st.markdown("""
<div class="content-box">
<h3>기술적 취약점</h3>
<ul>
<li><b>사전 공격(Dictionary Attack):</b> 통상적인 패턴을 이용한 해킹에 무방비함.</li>
<li><b>보안 피로감:</b> 복잡성 규칙 강요에 따른 사용자의 거부감.</li>
</ul>
</div>
""",unsafe_allow_html=True)

    with c2:
        st.markdown("""
<div class="content-box">
<h3>인지적 취약점</h3>
<ul>
<li><b>가이드라인 부재:</b> 무엇이 안전한지에 대한 구체적 기준을 체감할 기회 부족.</li>
<li><b>행위와 인식의 간극:</b> 보안의 중요성은 알지만, 실천 방법의 정교함이 결여됨.</li>
</ul>
</div>
""",unsafe_allow_html=True)

elif menu=="본론 3: 해결 방안 및 구현":
    st.title("💡 개선 방안 및 기술 스택")

    st.markdown("""
<div class="content-box">
<h3>제도적/기술적 대응</h3>
<ul>
<li><b>다중 인증(MFA/2FA):</b> 비밀번호 탈취 이후의 2차 방어선 구축.</li>
<li><b>비밀번호 관리자(Password Manager):</b> 복잡한 난수 생성을 자동화하여 인지적 부하 감소.</li>
</ul>
</div>
""",unsafe_allow_html=True)

    st.markdown("""
<div class="content-box">
<h3>구현 환경 및 혁신: "체험형 보안"</h3>
<ul>
<li><b>Streamlit:</b> 대화형 웹 인터페이스를 통해 사용자가 입력한 비밀번호의 엔트로피를 즉시 계산 및 시각화.</li>
<li><b>GitHub:</b> 오픈소스 기반 코드 형상 관리 및 프로젝트 지속성 확보.</li>
<li><b>패러다임 전환:</b> 단순 암기식 보안 교육을 실시간 피드백 중심의 <b>능동적 체험형 교육</b>으로 전환.</li>
</ul>
</div>
""",unsafe_allow_html=True)

elif menu=="시뮬레이션: 보안 실증":
    st.title("🛡️ 실시간 보안성 시뮬레이터")

    pw=st.text_input("🔑 테스트할 비밀번호를 입력하세요",type="password")

    if pw:
        score=min(
            len(pw)*5+
            sum([
                pw.islower(),
                pw.isupper(),
                any(c.isdigit() for c in pw),
                any(not c.isalnum() for c in pw)
            ])*10,
            100
        )

        status,color=(
            ("안전","#22c55e")
            if score>70
            else ("주의","#f59e0b")
            if score>40
            else ("위험","#ef4444")
        )

        c1,c2=st.columns([1,2])

        with c1:
            st.markdown(f"""
<div class="content-box score-card" style="text-align:center;">
<h3>🛡️ 보안 점수</h3>
<h1 style="color:{color};font-size:75px;">
{score}
</h1>
<p style="font-size:22px;">
평가:
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
<li><b>길이 요소:</b> 긴 비밀번호일수록 조합 공간이 지수적으로 확장됩니다.</li>
<li><b>조합 요소:</b> 특수문자, 대소문자, 숫자의 혼합은 사전 공격 저항력을 높입니다.</li>
<li><b>결론:</b> 현재 입력하신 비밀번호는 위 원칙을 바탕으로 분석되었습니다.</li>
</ul>
</div>
""",unsafe_allow_html=True)

            st.progress(score/100)
