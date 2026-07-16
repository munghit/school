import streamlit as st
import math
import pandas as pd

st.set_page_config(
    page_title="디지털 보안 연구 보고서",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
    background:#020617;
    color:#e2e8f0;
}


h1{
    color:#38bdf8;
    font-size:42px;
    font-weight:900;
}


h2,h3{
    color:#e0f2fe;
}


.card{

    background:#111827;

    padding:25px;

    border-radius:18px;

    border:1px solid #334155;

    box-shadow:
    0 8px 25px rgba(0,0,0,0.35);

    color:#f8fafc;

    line-height:1.8;

}


.step-box{

    background:#172554;

    padding:16px;

    margin-bottom:12px;

    border-radius:12px;

    border-left:5px solid #38bdf8;

    color:#dbeafe;

    font-weight:700;

}


[data-testid="metric-container"]{

    background:#111827;

    border-radius:15px;

    padding:18px;

    border:1px solid #334155;

}


[data-testid="stMetricValue"]{

    color:#38bdf8;

    font-size:30px;

    font-weight:900;

}


.stProgress > div > div{

    background:#38bdf8;

}


.stTextInput input{

    background:#111827;

    color:white;

    border:1px solid #38bdf8;

    border-radius:10px;

}


section[data-testid="stSidebar"]{

    background:#020617;

    border-right:1px solid #334155;

}


</style>
""",unsafe_allow_html=True)



st.sidebar.title("📌 연구 메뉴")

page=st.sidebar.radio(
    "페이지 선택",
    [
        "📂 연구 종합 보고서",
        "🛡️ 보안성 시뮬레이터"
    ]
)



if page=="📂 연구 종합 보고서":

    st.title("📂 디지털 보안 연구 종합 보고서")


    st.markdown("""
<div class="card">

<h3>🔐 비밀번호 보안성 정량 분석 연구</h3>


<b>연구 분야</b><br>
정보보안 · 암호학 · 데이터 기반 보안 분석


<br><br>


<b>연구 목적</b><br>
비밀번호의 보안성을 단순한 문자 조합이 아닌
수학적 정보량과 공격 저항성을 기반으로 평가한다.


<br><br>


<b>평가 방법</b><br>
엔트로피 계산 · 무차별 대입 공격 모델 · 예상 해독 시간 분석


</div>
""",
unsafe_allow_html=True)



    st.subheader("📝 1. 서론")


    c1,c2=st.columns(2)


    with c1:

        st.markdown("""
<div class="card">

<h3>🔍 탐구 동기</h3>


최근 계정 탈취와 개인정보 유출 사고의 주요 원인 중 하나는
취약한 비밀번호 사용이다.


그러나 기존 비밀번호 정책은 단순히
특수문자 추가와 복잡성 증가에 집중하여
실제 공격 저항성을 정확하게 설명하지 못한다.


따라서 본 연구에서는 비밀번호의 보안성을
정량적인 데이터로 분석하고 최적의 조건을 탐구한다.


</div>
""",
unsafe_allow_html=True)



    with c2:

        st.markdown("""
<div class="card">

<h3>❓ 탐구 문제</h3>


1. 비밀번호 보안성을 결정하는 핵심 요소는 무엇인가?


<br>


2. 길이와 문자 조합 중 어떤 요소가
공격 저항성에 더 큰 영향을 미치는가?


<br>


3. 보안성과 사용성을 동시에 만족하는
비밀번호 생성 방법은 무엇인가?


</div>
""",
unsafe_allow_html=True)



    st.subheader("⚙️ 2. 본론 (탐구 과정)")


    col1,col2=st.columns([1,1.2])


    with col1:

        st.markdown("### 🛠️ 연구 진행 과정")


        steps=[
            "1단계 : 보안 관련 문헌 조사",
            "2단계 : 엔트로피 기반 수학 모델 설계",
            "3단계 : GPU 무차별 대입 공격 환경 가정",
            "4단계 : 보안성 지표 계산 및 비교 분석"
        ]


        for step in steps:

            st.markdown(
                f'<div class="step-box">{step}</div>',
                unsafe_allow_html=True
            )



        with col2:

        st.markdown("### 📊 보안성 평가 모델")

        st.markdown("""
<div class="card">

<h3>📌 계산 기준</h3>


<b>1. 엔트로피(Entropy)</b>

<br>

비밀번호가 가질 수 있는 정보량을 측정하는 지표이다.

<br><br>

<b>계산식</b>

<br>

E = L × log₂(N)


<br><br>

L : 비밀번호 길이

<br>

N : 사용 가능한 문자 집합 크기


<br><br>


<b>2. 무차별 대입 공격 모델</b>

<br>

가능한 모든 조합을 하나씩 대입하는 공격 방식으로,
공격 속도를 초당 100억 회로 가정하여 예상 해독 시간을 계산한다.


</div>
""",
unsafe_allow_html=True)



    st.markdown("---")


    st.subheader("📈 비밀번호 조건별 보안성 비교")


    df=pd.DataFrame({

        "비밀번호 유형":
        [
            "4자리 단순",
            "6자리 조합",
            "8자리 조합",
            "12자리 복합"
        ],

        "위험도 점수":
        [
            90,
            60,
            20,
            5
        ],

        "공격 저항성 지수":
        [
            10,
            40,
            80,
            95
        ]

    })


    st.bar_chart(
        df.set_index("비밀번호 유형")
    )


    st.markdown("""
<div class="card">

<h3>📌 분석 결과</h3>


비밀번호 길이가 증가하고 사용 가능한 문자 종류가 많아질수록
검색 공간(Search Space)이 증가하여 공격자가 시도해야 하는 경우의 수가 증가한다.


특히 12자리 이상의 복합 비밀번호는
무차별 대입 공격에 필요한 계산 비용을 크게 증가시키므로
현실적인 보안 기준으로 활용할 수 있다.


</div>
""",
unsafe_allow_html=True)



    st.subheader("🎯 3. 결론 (종합 결과)")


    c1,c2,c3=st.columns(3)



    with c1:

        st.markdown("""
<div class="card">

<h3>🔐 암호학적 관점</h3>


보안성은 단순한 규칙 증가보다
충분한 정보량 확보가 핵심이다.


엔트로피가 높을수록 공격자가 탐색해야 하는
경우의 수가 증가한다.


</div>
""",
unsafe_allow_html=True)



    with c2:

        st.markdown("""
<div class="card">

<h3>🧠 사용자 관점</h3>


복잡한 문자열은 기억하기 어렵다는 문제가 있다.


따라서 여러 단어를 조합한 패스프레이즈 방식은
높은 보안성과 사용성을 동시에 확보할 수 있다.


</div>
""",
unsafe_allow_html=True)



    with c3:

        st.markdown("""
<div class="card">

<h3>🛡️ 보안 전략</h3>


최적의 비밀번호는 무조건 복잡한 문자열이 아니라
충분한 길이와 높은 정보량을 가진 형태이다.


12자리 이상의 패스프레이즈가
현실적인 보안 최적점이다.


</div>
""",
unsafe_allow_html=True)



    st.info("""
💡 최종 연구 결론

비밀번호 보안성은 길이, 문자 집합 크기,
그리고 엔트로피에 의해 결정된다.

따라서 단순한 복잡성 규칙보다
높은 정보량을 가지는 패스프레이즈 기반 방식이
보안성과 사용성을 모두 만족하는 방법이다.
""")
