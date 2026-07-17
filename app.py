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
    background:#f8fafc;
    color:#1e293b;
}
h1{
    color:#1d4ed8!important;
    font-size:42px!important;
    font-weight:900;
}
h2{
    color:#1e40af!important;
    font-weight:800;
}
h3{
    color:#334155!important;
}
p,li{
    color:#334155;
    font-size:17px;
    line-height:1.7;
}
.content-box{
    background:#ffffff;
    padding:25px;
    border-radius:16px;
    border:1px solid #dbeafe;
    box-shadow:0 5px 15px rgba(15,23,42,0.08);
    margin-bottom:15px;
}
.metric-card{
    background:#ffffff;
    padding:20px;
    border-radius:16px;
    border:1px solid #bfdbfe;
    text-align:center;
    box-shadow:0 4px 12px rgba(0,0,0,0.06);
}
.metric-number{
    font-size:40px;
    font-weight:900;
    color:#2563eb;
}
.report-card{
    background:#ffffff;
    padding:20px;
    border-radius:14px;
    border-left:6px solid #2563eb;
    box-shadow:0 4px 10px rgba(0,0,0,0.06);
}
.safe{
    color:#16a34a;
    font-weight:900;
}
.warning{
    color:#ca8a04;
    font-weight:900;
}
.danger{
    color:#dc2626;
    font-weight:900;
}
section[data-testid="stSidebar"]{
    background:white;
    border-right:1px solid #e2e8f0;
}
section[data-testid="stSidebar"] label{
    color:#1d4ed8!important;
    font-weight:700;
}
.stTextInput input{
    background:white!important;
    color:#111827!important;
    border:1px solid #94a3b8!important;
    border-radius:10px!important;
}
.stProgress>div>div>div{
    background:#2563eb;
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
디지털 서비스의 확대와 함께 개인정보 보호의 중요성이 증가하고 있습니다.
그러나 사용자는 편리성을 이유로 단순하거나 반복적인 비밀번호를 사용하는 경우가 많으며,
이는 개인정보 유출 위험을 증가시키는 주요 원인이 됩니다.
</p>

</div>
""",unsafe_allow_html=True)


    c1,c2,c3=st.columns(3)


    with c1:
        st.markdown("""
<div class="metric-card">
<h3>🔑 Password</h3>
<div class="metric-number">1st</div>
<p>첫 번째 보안 방어선</p>
</div>
""",unsafe_allow_html=True)


    with c2:
        st.markdown("""
<div class="metric-card">
<h3>⚠️ Risk</h3>
<div class="metric-number">↑</div>
<p>디지털 위협 증가</p>
</div>
""",unsafe_allow_html=True)


    with c3:
        st.markdown("""
<div class="metric-card">
<h3>🛡 Defense</h3>
<div class="metric-number">AI</div>
<p>데이터 기반 분석 필요</p>
</div>
""",unsafe_allow_html=True)


    st.markdown("""
<div class="content-box">

<h2>연구 목적</h2>

<ul>
<li>비밀번호가 디지털 보안의 핵심 방어 요소임을 분석</li>
<li>사용자의 보안 인식과 실제 사용 행태의 차이를 확인</li>
<li>데이터 기반 분석 시스템을 통해 보안 수준을 정량적으로 평가</li>
</ul>

</div>
""",unsafe_allow_html=True)


    st.markdown("""
<div class="content-box">

<h2>연구 진행 과정</h2>

<p>
문제 정의 → 이론 분석 → 알고리즘 설계 → 시스템 구현 → 결과 분석
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
<li><b>인증 과정:</b> 비밀번호는 사용자를 확인하는 가장 기본적인 인증 수단입니다.</li>
<li><b>보안 원칙:</b> 영문, 숫자, 특수문자 조합은 공격 가능성을 감소시키는 핵심 요소입니다.</li>
<li><b>관리 전략:</b> 비밀번호 관리자는 안전한 비밀번호 생성과 저장을 지원합니다.</li>
</ul>

</div>
""",unsafe_allow_html=True)


    with c2:
        st.markdown("""
<div class="content-box">

<h2>2. 공격 원리와 복잡도</h2>

<ul>
<li><b>무차별 대입 공격:</b> 가능한 모든 조합을 반복적으로 탐색하는 공격 방식입니다.</li>
<li><b>조합 공간:</b> 문자 집합 크기와 길이에 따라 경우의 수가 증가합니다.</li>
<li><b>수학적 관계:</b> 가능한 경우의 수는 N<sup>L</sup> 형태로 증가합니다.</li>
</ul>

</div>
""",unsafe_allow_html=True)


    st.markdown("""
<div class="content-box">

<h2>비밀번호 보안 핵심 변수</h2>

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

<p>사용 문자 종류</p>

</div>
""",unsafe_allow_html=True)


    with c:
        st.markdown("""
<div class="metric-card">

<h3>Entropy</h3>

<div class="metric-number">
↑
</div>

<p>정보량 증가</p>

</div>
""",unsafe_allow_html=True)



elif menu=="📈 보안 취약성 분석":

    st.title("📈 보안 취약성 분석")


    st.markdown("""
<div class="content-box">

<h2>사용자 보안 실태: 편리함과 보안의 충돌</h2>

<p>
많은 사용자는 기억하기 쉬운 비밀번호를 선택하며,
이는 비밀번호 재사용과 보안 취약성 증가로 이어집니다.
따라서 사용자가 자신의 보안 수준을 직접 확인할 수 있는
정량적 분석 시스템이 필요합니다.
</p>

</div>
""",unsafe_allow_html=True)



    c1,c2=st.columns(2)


    with c1:

        st.markdown("""
<div class="content-box">

<h2>기술적 취약점</h2>

<ul>
<li><b>사전 공격:</b> 자주 사용되는 단어나 패턴을 기반으로 공격</li>
<li><b>무차별 대입:</b> 모든 조합을 반복적으로 탐색</li>
<li><b>재사용 문제:</b> 하나의 유출이 여러 계정 위험으로 확산</li>
</ul>

</div>
""",unsafe_allow_html=True)



    with c2:

        st.markdown("""
<div class="content-box">

<h2>인지적 취약점</h2>

<ul>
<li><b>판단 어려움:</b> 사용자가 안전한 수준을 직접 평가하기 어려움</li>
<li><b>보안 피로:</b> 복잡한 규칙에 대한 사용자 부담 증가</li>
<li><b>인식과 행동 차이:</b> 중요성은 알지만 실천 부족</li>
</ul>

</div>
""",unsafe_allow_html=True)

elif menu=="⚙️ 시스템 구현":

    st.title("⚙️ 시스템 구현")


    st.markdown("""
<div class="content-box">

<h2>구현 목표</h2>

<p>
본 연구에서는 사용자가 입력한 비밀번호를 기반으로
보안 수준을 정량적으로 분석하고,
결과를 시각적으로 제공하는 체험형 보안 분석 시스템을 구현하였습니다.
</p>

</div>
""",unsafe_allow_html=True)



    c1,c2,c3=st.columns(3)


    with c1:
        st.markdown("""
<div class="metric-card">

<h3>Streamlit</h3>

<div class="metric-number">UI</div>

<p>웹 인터페이스 구현</p>

</div>
""",unsafe_allow_html=True)



    with c2:
        st.markdown("""
<div class="metric-card">

<h3>Python</h3>

<div class="metric-number">⚙️</div>

<p>분석 알고리즘 구현</p>

</div>
""",unsafe_allow_html=True)



    with c3:
        st.markdown("""
<div class="metric-card">

<h3>Plotly</h3>

<div class="metric-number">📊</div>

<p>데이터 시각화</p>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2>분석 알고리즘 구조</h2>

<ul>
<li><b>입력:</b> 사용자가 입력한 비밀번호</li>
<li><b>분석:</b> 길이, 문자 구성, 엔트로피 계산</li>
<li><b>평가:</b> 보안 점수와 위험 수준 산출</li>
<li><b>출력:</b> 그래프 및 개선 방향 제공</li>
</ul>

</div>
""",unsafe_allow_html=True)



elif menu=="🧪 실험 및 결과":

    st.title("🧪 Password Security Analyzer")


    st.markdown("""
<div class="content-box">

<h2>🔐 AI 기반 비밀번호 보안 분석</h2>

<p>
입력된 비밀번호를 기반으로 길이, 문자 다양성,
엔트로피, 공격 가능성을 분석하여 보안 수준을 평가합니다.
</p>

</div>
""",unsafe_allow_html=True)



    pw=st.text_input(
        "🔑 분석할 비밀번호 입력",
        type="password",
        placeholder="비밀번호를 입력하세요"
    )


    if pw:


        length_score=min(len(pw)*8,100)

        has_upper=any(c.isupper() for c in pw)

        has_lower=any(c.islower() for c in pw)

        has_digit=any(c.isdigit() for c in pw)

        has_special=any(not c.isalnum() for c in pw)


        upper_score=100 if has_upper else 0

        lower_score=100 if has_lower else 0

        digit_score=100 if has_digit else 0

        special_score=100 if has_special else 0



        score=int(
            length_score*0.35+
            upper_score*0.15+
            lower_score*0.15+
            digit_score*0.15+
            special_score*0.20
        )


        score=min(score,100)



        if score>=70:

            status="안전"

            color="#16a34a"


        elif score>=40:

            status="주의"

            color="#ca8a04"


        else:

            status="위험"

            color="#dc2626"




        c1,c2=st.columns([1,2])



        with c1:

            st.markdown(f"""
<div class="content-box" style="text-align:center">

<h3>Security Score</h3>

<h1 style="font-size:80px;color:{color}">
{score}
</h1>

<h2 style="color:{color}">
{status}
</h2>

</div>
""",unsafe_allow_html=True)



        with c2:

            missing=[]


            if not has_upper:
                missing.append("대문자")

            if not has_lower:
                missing.append("소문자")

            if not has_digit:
                missing.append("숫자")

            if not has_special:
                missing.append("특수문자")



            if len(missing)==0:

                recommend="현재 모든 보안 요소가 포함되어 있습니다."

            else:

                recommend=f"{', '.join(missing)} 요소 추가 필요"



            st.markdown(f"""
<div class="content-box">

<h2>🔍 Security Report</h2>

<ul>

<li>
<b>비밀번호 길이:</b> {len(pw)}자리
</li>

<li>
<b>문자 구성:</b>
{"균형적 구성" if len(missing)==0 else "일부 요소 부족"}
</li>

<li>
<b>개선 방향:</b>
{recommend}
</li>

</ul>

</div>
""",unsafe_allow_html=True)



        st.progress(score/100)

        st.markdown("---")

        st.subheader("📊 Security Factor Analysis")


        categories=[
            "길이",
            "대문자",
            "소문자",
            "숫자",
            "특수문자"
        ]


        values=[
            length_score,
            upper_score,
            lower_score,
            digit_score,
            special_score
        ]


        fig=go.Figure()


        fig.add_trace(
            go.Scatterpolar(
                r=values,
                theta=categories,
                fill="toself",
                name="Security Level",
                line=dict(
                    color="#2563eb",
                    width=4
                ),
                fillcolor="rgba(37,99,235,0.25)"
            )
        )


        fig.update_layout(
            polar=dict(
                bgcolor="#ffffff",
                radialaxis=dict(
                    visible=True,
                    range=[0,100],
                    color="#111827",
                    tickfont=dict(
                        size=13,
                        color="#111827"
                    )
                ),
                angularaxis=dict(
                    color="#111827",
                    tickfont=dict(
                        size=15,
                        color="#111827"
                    )
                )
            ),
            font=dict(
                color="#111827"
            ),
            showlegend=False,
            height=500,
            paper_bgcolor="#ffffff",
            plot_bgcolor="#ffffff"
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



        st.markdown("---")


        st.subheader("🔐 Password Entropy Analysis")


        charset=0


        if has_lower:
            charset+=26

        if has_upper:
            charset+=26

        if has_digit:
            charset+=10

        if has_special:
            charset+=32



        if charset>0:

            entropy=len(pw)*math.log2(charset)

        else:

            entropy=0



        if entropy<40:

            entropy_status="낮음"

            entropy_color="#dc2626"


        elif entropy<70:

            entropy_status="보통"

            entropy_color="#ca8a04"


        else:

            entropy_status="높음"

            entropy_color="#16a34a"



        st.markdown(f"""
<div class="content-box">

<h2>정보 엔트로피</h2>

<h1 style="color:{entropy_color}">
{entropy:.2f} bits
</h1>

<p>
현재 엔트로피 수준:
<b style="color:{entropy_color}">
{entropy_status}
</b>
</p>

<p>
엔트로피는 비밀번호가 가지는 예측 불가능성을 수치화한 값으로,
값이 높을수록 공격자가 추측하기 어렵습니다.
</p>

</div>
""",unsafe_allow_html=True)



        st.markdown("---")


        st.subheader("⚔️ Attack Risk Analysis")


        attack_col1,attack_col2,attack_col3=st.columns(3)



        if len(pw)<8:

            dictionary="🔴 높음"

        else:

            dictionary="🟢 낮음"



        if entropy<50:

            brute="🔴 높음"

        elif entropy<80:

            brute="🟡 보통"

        else:

            brute="🟢 낮음"



        if pw.lower()==pw or pw.isdigit():

            pattern="🔴 높음"

        else:

            pattern="🟡 보통"



        with attack_col1:

            st.markdown(f"""
<div class="metric-card">

<h3>Dictionary Attack</h3>

<div class="metric-number">
{dictionary}
</div>

<p>
사전 기반 공격 위험
</p>

</div>
""",unsafe_allow_html=True)



        with attack_col2:

            st.markdown(f"""
<div class="metric-card">

<h3>Brute Force</h3>

<div class="metric-number">
{brute}
</div>

<p>
무차별 대입 위험
</p>

</div>
""",unsafe_allow_html=True)



        with attack_col3:

            st.markdown(f"""
<div class="metric-card">

<h3>Pattern Attack</h3>

<div class="metric-number">
{pattern}
</div>

<p>
규칙 기반 공격 위험
</p>

</div>
""",unsafe_allow_html=True)



        st.markdown("---")


        st.subheader("⏱️ Brute Force Simulation")


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

<h2>공격 시뮬레이션 결과</h2>

<p>
가능한 조합 수:
<b>{combinations:,}</b>
</p>

<p>
가정:
초당 10억 회 대입 공격
</p>

<h1 style="color:#2563eb">
예상 공격 시간 : {attack_time}
</h1>

</div>
""",unsafe_allow_html=True)

        st.markdown("---")

        st.subheader("🆚 Security Improvement Simulation")


        st.markdown("""
<div class="content-box">

<h2>현재 비밀번호와 개선된 비밀번호 비교</h2>

<p>
현재 입력한 비밀번호의 취약점을 분석하고,
개선 방향을 적용했을 때 보안성이 어떻게 변화하는지 비교합니다.
</p>

</div>
""",unsafe_allow_html=True)



        improved_pw=pw


        if not has_upper:
            improved_pw+="A"

        if not has_lower:
            improved_pw+="a"

        if not has_digit:
            improved_pw+="1"

        if not has_special:
            improved_pw+="!"

        while len(improved_pw)<12:
            improved_pw+="X"



        improved_charset=0


        if any(c.islower() for c in improved_pw):
            improved_charset+=26

        if any(c.isupper() for c in improved_pw):
            improved_charset+=26

        if any(c.isdigit() for c in improved_pw):
            improved_charset+=10

        if any(not c.isalnum() for c in improved_pw):
            improved_charset+=32



        improved_score=int(
            min(len(improved_pw)*8,100)*0.35+
            (100 if any(c.isupper() for c in improved_pw) else 0)*0.15+
            (100 if any(c.islower() for c in improved_pw) else 0)*0.15+
            (100 if any(c.isdigit() for c in improved_pw) else 0)*0.15+
            (100 if any(not c.isalnum() for c in improved_pw) else 0)*0.20
        )


        improved_score=min(improved_score,100)



        compare1,compare2=st.columns(2)



        with compare1:

            st.markdown(f"""
<div class="metric-card">

<h3>현재 비밀번호</h3>

<div class="metric-number">
{score}
</div>

<p>
보안 점수
</p>

<p>
길이: {len(pw)}자리
</p>

</div>
""",unsafe_allow_html=True)



        with compare2:

            st.markdown(f"""
<div class="metric-card">

<h3>개선 시뮬레이션</h3>

<div class="metric-number">
{improved_score}
</div>

<p>
예상 보안 점수
</p>

<p>
길이: {len(improved_pw)}자리
</p>

</div>
""",unsafe_allow_html=True)



        st.markdown("""
<div class="content-box">

<h2>📌 연구 결과 해석</h2>

<ul>

<li>
비밀번호 길이와 문자 다양성이 증가할수록
가능한 조합 공간이 증가합니다.
</li>

<li>
엔트로피 증가를 통해 공격자의 예측 가능성이 감소합니다.
</li>

<li>
사용자가 자신의 취약 요소를 확인하고 개선 방향을 선택할 수 있습니다.
</li>

</ul>

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
<li>비밀번호 규칙 암기 중심</li>
<li>사용자가 위험성을 직접 판단하기 어려움</li>
<li>보안 수준을 체감하기 어려움</li>
</ul>

</div>
""",unsafe_allow_html=True)



    with c2:

        st.markdown("""
<div class="content-box">

<h2>제안 시스템</h2>

<ul>
<li>데이터 기반 보안 수준 분석</li>
<li>엔트로피 기반 정량 평가</li>
<li>공격 시뮬레이션 제공</li>
<li>개선 방향 자동 제시</li>
</ul>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2>연구 성과</h2>

<ul>

<li>비밀번호 보안성을 수치화하는 분석 알고리즘 구현</li>

<li>레이더 차트와 위험도 분석을 통한 시각화</li>

<li>엔트로피 기반 보안성 평가 적용</li>

<li>체험형 디지털 보안 교육 시스템 구축</li>

</ul>

</div>
""",unsafe_allow_html=True)



    st.markdown("""
<div class="content-box">

<h2 style="text-align:center;color:#2563eb">
"보안은 단순한 규칙이 아니라,
데이터를 통해 이해하고 개선하는 과정이다."
</h2>

<p style="text-align:center">

본 연구는 사용자가 자신의 비밀번호 보안 수준을 직접 확인하고,
데이터 기반 분석을 통해 안전한 디지털 환경을 구축할 수 있도록
지원하는 체험형 보안 분석 시스템을 구현하였습니다.

</p>

</div>
""",unsafe_allow_html=True)
