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


if page=="📑 연구 보고서":


    st.markdown("""
    <div class="title-box">

    <h1>
    🛡️ AI 기반 디지털 인증 보안 연구
    </h1>

    <p>
    Shannon Entropy와 공격 모델 기반
    패스워드 안전성 평가 시스템
    </p>

    </div>

    """,
    unsafe_allow_html=True)



    st.header("1. 연구 배경")


    c1,c2=st.columns(2)


    with c1:

        st.markdown("""
        <div class="card">

        <h3>🔍 연구 목적</h3>

        현대 인증 시스템에서 가장 빈번하게 발생하는
        계정 탈취 문제는 약한 패스워드 사용에서 발생한다.

        본 연구는 정보이론 기반 엔트로피 분석을 통해
        패스워드의 공격 저항성을 정량적으로 평가한다.

        </div>
        """,
        unsafe_allow_html=True)



    with c2:

        st.markdown("""
        <div class="card">

        <h3>⚠️ 주요 위협 모델</h3>

        • Brute Force Attack<br>
        • Dictionary Attack<br>
        • Credential Stuffing<br>
        • GPU Parallel Cracking

        </div>
        """,
        unsafe_allow_html=True)



    st.header("2. 평가 모델")


    df=pd.DataFrame({

        "평가 요소":
        [
            "Entropy",
            "Length",
            "Character Space",
            "Pattern Risk"
        ],

        "가중치":
        [
            40,
            25,
            20,
            15
        ]

    })


    st.dataframe(
        df,
        use_container_width=True
    )



    st.info(
    """
    핵심 연구 결론:

    단순한 복잡성 증가보다
    충분한 길이와 높은 정보량을 가진
    Passphrase 방식이 현대 인증 환경에서
    가장 효율적인 보안 전략이다.
    """
    )



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
