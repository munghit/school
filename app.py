import streamlit as st
import math
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import re


# =====================================================
# 페이지 설정
# =====================================================

st.set_page_config(
    page_title="AI 기반 패스워드 보안 분석 연구",
    page_icon="🛡️",
    layout="wide"
)


# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background:#020617;
    color:white;
}


.card{
    background:#0f172a;
    border:1px solid #334155;
    border-radius:18px;
    padding:25px;
    margin-bottom:20px;
}


.title-box{
    background:linear-gradient(
    135deg,#0f172a,#1e3a8a);
    padding:30px;
    border-radius:20px;
}


.metric-card{
    background:#111827;
    padding:20px;
    border-radius:15px;
    border:1px solid #334155;
}


.security-box{
    padding:25px;
    border-radius:20px;
    text-align:center;
    font-size:25px;
    font-weight:bold;
}


.analysis{
    background:#111827;
    border-left:5px solid #38bdf8;
    padding:18px;
    border-radius:10px;
}


</style>

""", unsafe_allow_html=True)



# =====================================================
# 함수 정의
# =====================================================


def calculate_entropy(password):

    charset = 0

    if re.search("[a-z]",password):
        charset +=26

    if re.search("[A-Z]",password):
        charset +=26

    if re.search("[0-9]",password):
        charset +=10

    if re.search("[^a-zA-Z0-9]",password):
        charset +=33


    if charset ==0:
        return 0,0


    entropy = len(password)*math.log2(charset)

    return entropy,charset



# -----------------------------------------------------


def attack_time(entropy):

    guesses = 2**entropy

    gpu_speed = 10**10

    seconds = guesses/gpu_speed


    if seconds <60:
        return f"{seconds:.2f} 초"

    elif seconds <3600:
        return f"{seconds/60:.2f} 분"

    elif seconds <86400:
        return f"{seconds/3600:.2f} 시간"

    elif seconds <31536000:
        return f"{seconds/86400:.2f} 일"

    else:
        return f"{seconds/31536000:.2f} 년"



# -----------------------------------------------------


def detect_pattern(password):

    risks=[]


    # 반복 문자

    if re.search(r"(.)\1\1",password):
        risks.append(
            "반복 문자 패턴 탐지"
        )


    # 연속 숫자

    if re.search(
        r"1234|2345|3456|4567|5678",
        password
    ):
        risks.append(
            "연속 숫자 패턴 탐지"
        )


    # 키보드 패턴

    keyboard=[
        "qwerty",
        "asdf",
        "zxcv"
    ]


    for k in keyboard:
        if k in password.lower():
            risks.append(
                "키보드 배열 패턴 탐지"
            )


    return risks



# -----------------------------------------------------


def security_score(entropy, risks):

    score=min(entropy,100)


    score -= len(risks)*8


    return max(0,int(score))



# =====================================================
# 사이드바
# =====================================================


st.sidebar.title("🛡️ Security Lab")

page=st.sidebar.radio(
    "분석 메뉴",
    [
        "📑 연구 보고서",
        "🔐 AI 패스워드 분석기"
    ]
)



# =====================================================
# 연구 보고서
# =====================================================

if page=="📂 연구 종합 보고서":

    st.title("📂 디지털 보안 연구 종합 보고서")
    st.markdown("---")

    st.header("📝 1. 서론")

    c1,c2=st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>🔍 탐구 동기</h3>
        최근 발생하는 개인정보 유출 및 계정 탈취 사고의 주요 원인 중 하나는 취약한 비밀번호 사용이다.<br><br>
        기존의 복잡성 중심 보안 정책은 사용자의 기억 부담을 증가시키지만 실제 공격 저항성을 정확히 반영하지 못한다.<br><br>
        본 연구에서는 정보이론 기반 정량 분석을 통해 비밀번호 보안성을 평가하고 최적의 보안 조건을 탐구한다.
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>❓ 탐구 문제</h3>
        1. 비밀번호 보안성을 결정하는 핵심 요소는 무엇인가?<br><br>
        2. 길이와 복잡성 중 어떤 요소가 공격 저항성에 더 큰 영향을 미치는가?<br><br>
        3. 보안성과 사용 편의성을 동시에 만족하는 방법은 무엇인가?
        </div>
        """,unsafe_allow_html=True)


    st.header("⚙️ 2. 본론 (연구 과정 및 분석 기준)")

    st.subheader("📚 이론적 배경")

    st.markdown("""
    <div class="card">
    <h3>Shannon Entropy 기반 보안성 평가</h3>
    엔트로피는 비밀번호가 가지는 정보량을 의미하며 값이 높을수록 가능한 조합 수가 증가하여 공격 난이도가 높아진다.<br><br>
    <b>공식</b><br>
    E = L × log₂(N)<br><br>
    L : 비밀번호 길이<br>
    N : 사용 가능한 문자 집합 크기
    </div>
    """,unsafe_allow_html=True)


    st.subheader("📊 보안성 평가 기준")

    criteria=pd.DataFrame({
        "평가 요소":[
            "길이(L)",
            "문자 집합(N)",
            "엔트로피(E)",
            "패턴 위험도",
            "예상 공격 시간"
        ],
        "분석 기준":[
            "비밀번호 길이가 증가할수록 조합 수 증가",
            "대문자·소문자·숫자·특수문자 사용 여부",
            "정보량(bit)을 이용한 수학적 보안성 평가",
            "반복 문자 및 예측 가능한 패턴 감점",
            "GPU Brute Force 공격 기준 계산"
        ]
    })

    st.dataframe(criteria,use_container_width=True)


    st.subheader("⚔️ 공격 시간 계산 모델")

    st.markdown("""
    <div class="card">
    공격자가 초당 R개의 조합을 검사한다고 가정할 때 예상 해독 시간은 다음과 같이 계산한다.<br><br>
    <b>T = 2ᴱ / R</b><br><br>
    E : 엔트로피(bit)<br>
    R : 초당 검사 가능한 조합 수<br><br>
    본 연구에서는 현대 GPU 기반 공격 환경을 고려하여 R = 10¹⁰ guesses/sec 기준으로 분석한다.
    </div>
    """,unsafe_allow_html=True)


    st.header("🎯 3. 결론 (종합 연구 결과)")

    c1,c2,c3=st.columns(3)

    with c1:
        st.markdown("""
        <div class="card">
        <h3>🔐 암호학적 효율성</h3>
        보안성 향상의 핵심은 단순한 규칙 증가가 아니라 높은 엔트로피 확보이다.
        </div>
        """,unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
        <h3>🧠 사용자 편의성</h3>
        복잡한 문자열보다 긴 Passphrase 방식이 기억성과 보안을 동시에 만족한다.
        </div>
        """,unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="card">
        <h3>🛡️ 최적 보안 전략</h3>
        12자 이상의 단어 조합형 패스프레이즈가 현실적인 보안 해결책이다.
        </div>
        """,unsafe_allow_html=True)


    st.success("""
💡 최종 결론

비밀번호 보안성은 단순히 특수문자를 추가하는 것이 아니라
충분한 길이와 높은 정보량을 확보하는 것이 핵심이다.

따라서 현대 인증 환경에서는
긴 패스프레이즈 기반 방식이 가장 효율적인 보안 전략이다.
""")


# =====================================================
# 여기까지 1/2
# =====================================================
# =====================================================
# AI 패스워드 분석기
# =====================================================


elif page=="🔐 AI 패스워드 분석기":


    st.markdown("""
    <div class="title-box">

    <h1>
    🔐 AI Password Security Analyzer
    </h1>

    <p>
    Information Theory + Threat Modeling 기반
    실시간 패스워드 취약점 분석 시스템
    </p>

    </div>

    """,
    unsafe_allow_html=True)



    password=st.text_input(
        "분석 대상 패스워드 입력",
        type="password",
        placeholder="예: 안전성을 평가할 패스워드를 입력하세요"
    )



    if password:


        # ================================
        # 기본 분석
        # ================================


        entropy,charset=calculate_entropy(password)


        risks=detect_pattern(password)


        score=security_score(
            entropy,
            risks
        )


        # 등급

        if score <30:

            level="Critical Risk"
            color="#ef4444"
            icon="🚨"

        elif score <60:

            level="High Risk"
            color="#f97316"
            icon="⚠️"


        elif score <85:

            level="Secure"
            color="#38bdf8"
            icon="🔒"


        else:

            level="Excellent Security"
            color="#22c55e"
            icon="🛡️"



        # ================================
        # 종합 결과
        # ================================


        st.subheader(
            "🎯 종합 보안 평가 결과"
        )


        st.markdown(
        f"""
        <div class="security-box"
        style="background:{color};">

        {icon}
        {level}

        <br>

        Security Score :
        {score}/100

        </div>

        """,
        unsafe_allow_html=True
        )



        st.progress(
            score/100
        )



        # ================================
        # 핵심 지표
        # ================================


        st.subheader(
            "📊 정량 분석 지표"
        )


        c1,c2,c3,c4=st.columns(4)


        c1.metric(
            "Entropy",
            f"{entropy:.2f} bits"
        )


        c2.metric(
            "Charset Space",
            f"{charset}"
        )


        c3.metric(
            "Length",
            f"{len(password)} chars"
        )


        c4.metric(
            "Risk Pattern",
            f"{len(risks)} 개"
        )




        # ================================
        # 엔트로피 시각화
        # ================================


        st.subheader(
            "📈 정보량 분석"
        )


        fig=go.Figure(
            go.Indicator(

                mode="gauge+number",

                value=entropy,

                title={
                    "text":
                    "Password Entropy(bits)"
                },

                gauge={

                    "axis":{
                        "range":[0,150]
                    }

                }

            )
        )


        st.plotly_chart(
            fig,
            use_container_width=True
        )



        # ================================
        # 공격 모델 분석
        # ================================


        st.subheader(
            "⚔️ 공격 유형별 취약성 분석"
        )


        attack_df=pd.DataFrame({

            "Attack Model":
            [
                "Brute Force",
                "Dictionary Attack",
                "Credential Stuffing",
                "Pattern Attack"
            ],


            "Risk Score":
            [
                max(0,100-entropy),
                70 if len(risks)>0 else 30,
                50,
                len(risks)*25
            ]

        })


        st.bar_chart(
            attack_df.set_index(
                "Attack Model"
            )
        )




        # ================================
        # 해킹 시간 시뮬레이션
        # ================================


        st.subheader(
            "⏳ GPU 기반 공격 시뮬레이션"
        )


        st.markdown(
        f"""

        <div class="analysis">

        현대 GPU 클러스터 공격 환경<br>

        가정:
        <br>
        • 초당 {10**10:,}회 연산 가능
        <br>
        • 완전 탐색(Brute Force)
        <br><br>


        예상 해독 시간:

        <h2>

        {attack_time(entropy)}

        </h2>

        </div>

        """,
        unsafe_allow_html=True
        )




        # ================================
        # 문자 구성 분석
        # ================================


        st.subheader(
            "🔎 문자 구성 분석"
        )


        features={

        "소문자":
        bool(re.search("[a-z]",password)),

        "대문자":
        bool(re.search("[A-Z]",password)),

        "숫자":
        bool(re.search("[0-9]",password)),

        "특수문자":
        bool(re.search("[^a-zA-Z0-9]",password))

        }



        f1,f2=st.columns(2)



        with f1:

            st.markdown(
            "### Character Set"
            )


            for k,v in features.items():

                if v:

                    st.success(
                        f"✅ {k} 포함"
                    )

                else:

                    st.error(
                        f"❌ {k} 부족"
                    )



        with f2:


            st.markdown(
            "### Pattern Detection"
            )


            if risks:


                for r in risks:

                    st.warning(
                        r
                    )


            else:

                st.success(
                    "탐지된 위험 패턴 없음"
                )



        # ================================
        # NIST 기준 평가
        # ================================


        st.subheader(
            "📋 NIST 기반 보안 정책 평가"
        )


        standards={

        "8자 이상":
        len(password)>=8,


        "12자 이상 권장":
        len(password)>=12,


        "문자 종류 3개 이상":
        sum(features.values())>=3,


        "반복 패턴 없음":
        len(risks)==0

        }



        result=[]


        for k,v in standards.items():

            result.append({

            "평가 기준":k,

            "결과":
            "PASS" if v else "FAIL"

            })


        st.table(
            pd.DataFrame(result)
        )



        # ================================
        # 개선 추천
        # ================================


        st.subheader(
            "💡 보안 강화 추천"
        )


        recommendations=[]


        if len(password)<12:

            recommendations.append(
            "길이를 12자 이상으로 증가시키세요."
            )


        if not features["특수문자"]:

            recommendations.append(
            "특수문자 추가를 고려하세요."
            )


        if risks:

            recommendations.append(
            "예측 가능한 패턴 제거가 필요합니다."
            )


        if entropy<70:

            recommendations.append(
            "단어 조합형 Passphrase 사용을 권장합니다."
            )



        if recommendations:


            for r in recommendations:

                st.info(
                    r
                )

        else:

            st.success(
            "현재 패스워드는 높은 보안 수준을 유지하고 있습니다."
            )



        st.markdown("---")


        st.caption(
        """
        본 분석기는 Shannon Entropy,
        Brute Force Threat Model,
        Pattern Detection 알고리즘을 기반으로
        패스워드 보안성을 정량 평가합니다.
        """
        )
