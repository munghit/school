import streamlit as st
import math
import pandas as pd

st.set_page_config(
    page_title="디지털 보안 연구 보고서",
    layout="wide"
)

st.sidebar.title("📌 메뉴")

page = st.sidebar.radio(
    "목차",
    [
        "📂 연구 종합 보고서",
        "🛡️ 보안성 시뮬레이터"
    ]
)
if page == "📂 연구 종합 보고서":

    st.title("📂 디지털 보안 연구 종합 보고서")

    st.markdown("""
    <div class="card">

    <h3>🔐 Cyber Security Research Dashboard</h3>

    <b>Research Domain</b><br>
    Information Security / Password Cryptography

    <br><br>

    <b>Analysis Framework</b><br>
    Shannon Entropy Based Security Evaluation

    <br><br>

    <b>Simulation Environment</b><br>
    GPU Brute Force Attack Model

    <br><br>

    <b>Evaluation Metrics</b><br>
    Password Entropy · Search Space · Attack Resistance

    </div>
    """,unsafe_allow_html=True)


    st.subheader("📝 1. 서론")

    c1,c2=st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">

        <h3>🔍 탐구 동기</h3>

        계정 탈취 사고의 주요 원인인 취약한 비밀번호 문제를
        정량적 데이터 기반으로 분석하고 해결하고자 한다.

        기존의 단순 복잡성 중심 보안 정책은 사용자의 기억 부담을 증가시키지만,
        실제 공격 저항성을 정확하게 설명하지 못한다.

        따라서 정보이론 기반 분석을 통해 비밀번호 보안성을 평가하고
        최적의 보안 조건을 탐구한다.

        </div>
        """,unsafe_allow_html=True)


    with c2:
        st.markdown("""
        <div class="card">

        <h3>❓ 탐구 문제</h3>

        1. 어떤 요소가 비밀번호 공격 저항성을 결정하는가?

        <br><br>

        2. 길이와 복잡성 중 어떤 요소가 더 중요한가?

        <br><br>

        3. 보안성과 사용성을 동시에 만족하는 방식은 무엇인가?

        </div>
        """,unsafe_allow_html=True)



    st.subheader("⚙️ 2. 본론 (탐구 과정 및 분석)")


    col1,col2=st.columns([1,1.2])


    with col1:

        st.markdown("### 🛠️ Research Pipeline")

        steps=[
        "Literature Review (NIST Password Guideline)",
        "Entropy Mathematical Modeling",
        "GPU Brute Force Simulation",
        "Security Evaluation"
        ]

        for step in steps:
            st.markdown(
            f'<div class="step-box">{step}</div>',
            unsafe_allow_html=True
            )


    with col2:

        st.markdown("### 📊 Security Evaluation Model")

        st.markdown("""
        <div class="card">

        <b>Input Layer</b>

        <br>
        Password Length (L)
        <br>
        Character Set Size (N)

        <br><br>

        ↓

        <br><br>

        <b>Processing Layer</b>

        <br>
        Shannon Entropy Calculation

        <br><br>

        ↓

        <br><br>

        <b>Output Layer</b>

        <br>
        Attack Resistance Index
        <br>
        Estimated Brute Force Cost

        </div>
        """,unsafe_allow_html=True)



    st.markdown("""
    <div class="card">

    ### 🔢 Mathematical Model

    <br>

    Password Entropy

    <br>

    E = L × log₂(N)

    <br><br>

    Expected Attack Time

    <br>

    T = 2ᴱ / R

    <br><br>

    L : Password Length

    <br>

    N : Character Space

    <br>

    R : Attack Attempts Per Second

    </div>
    """,unsafe_allow_html=True)



    df=pd.DataFrame({

    "Password Type":
    [
    "4 Character Simple",
    "6 Character Combination",
    "8 Character Combination",
    "12 Character Complex"
    ],

    "Attack Resistance Index":
    [
    90,
    60,
    20,
    5
    ]

    })


    st.markdown("### 📈 Security Evaluation Result")

    st.bar_chart(
        df.set_index("Password Type")
    )



    st.subheader("🎯 3. 결론 (종합적 탐구 결과)")


    c1,c2,c3=st.columns(3)


    with c1:
        st.markdown("""
        <div class="card">

        <h3>🔐 Cryptographic Efficiency</h3>

        높은 보안성은 단순한 규칙 증가보다
        충분한 엔트로피 확보에서 결정된다.

        </div>
        """,unsafe_allow_html=True)


    with c2:
        st.markdown("""
        <div class="card">

        <h3>🧠 User Efficiency</h3>

        Passphrase 방식은 높은 정보량과
        기억 가능성을 동시에 확보한다.

        </div>
        """,unsafe_allow_html=True)


    with c3:
        st.markdown("""
        <div class="card">

        <h3>🛡️ Security Strategy</h3>

        12자 이상의 패스프레이즈는
        현실적인 보안 최적점이다.

        </div>
        """,unsafe_allow_html=True)


    st.info("""
💡 Final Research Conclusion

비밀번호 보안성은 단순한 문자 복잡성이 아니라
길이와 정보량을 기반으로 결정된다.

따라서 긴 패스프레이즈 기반 인증 방식이
보안성과 사용성을 동시에 만족하는 최적 전략이다.
""")


elif page == "🛡️ 보안성 시뮬레이터":

    st.title("🛡️ Password Security Assessment Engine")
    st.markdown("---")

    password=st.text_input(
        "분석 대상 비밀번호 입력",
        type="password",
        placeholder="보안 강도를 분석할 비밀번호 입력"
    )


    if password:

        charset_size=sum([
            26 if any(c.islower() for c in password) else 0,
            26 if any(c.isupper() for c in password) else 0,
            10 if any(c.isdigit() for c in password) else 0,
            33 if any(not c.isalnum() for c in password) else 0
        ])


        entropy=len(password)*math.log2(
            charset_size if charset_size>0 else 1
        )


        score=min(int(entropy),100)



        if entropy<40:
            level,color,icon="Critical Risk","#ef4444","🚨"

        elif entropy<70:
            level,color,icon="Moderate Security","#f59e0b","⚠️"

        elif entropy<100:
            level,color,icon="Strong Security","#3b82f6","🔒"

        else:
            level,color,icon="Enterprise Grade","#22c55e","🛡️"



        st.subheader("🎯 Security Classification")


        st.progress(score/100)


        st.markdown(f"""
<div style="
background:linear-gradient(135deg,{color},#020617);
padding:35px;
border-radius:25px;
text-align:center;
box-shadow:0 0 35px {color};
border:1px solid rgba(255,255,255,0.2);
">

<div style="
font-size:55px;
">
{icon}
</div>

<div style="
font-size:32px;
font-weight:900;
color:white;
">
{level}
</div>

<div style="
font-size:18px;
color:#cbd5e1;
margin-top:10px;
">
Password Security Classification Result
</div>

</div>
""",unsafe_allow_html=True)



        col1,col2,col3=st.columns(3)


        col1.metric(
            "Entropy Level",
            f"{entropy:.1f} bits"
        )


        col2.metric(
            "Password Length",
            f"{len(password)} characters"
        )


        col3.metric(
            "Security Score",
            f"{score}/100"
        )



        st.markdown("### ⏱️ Brute Force Attack Simulation")


        seconds=(2**entropy)/(10**10)


        if seconds<60:
            time_str=f"{seconds:.2f} seconds"

        elif seconds<3600:
            time_str=f"{seconds/60:.2f} minutes"

        elif seconds<86400:
            time_str=f"{seconds/3600:.2f} hours"

        elif seconds<31536000:
            time_str=f"{seconds/86400:.2f} days"

        else:
            time_str=f"{seconds/31536000:.2f} years"



        st.markdown(f"""
<div class="card">

<h3>⚔️ Estimated Cracking Time</h3>

<p style="
font-size:35px;
font-weight:900;
color:{color};
text-align:center;
">

{time_str}

</p>


<p style="
text-align:center;
color:#94a3b8;
">

GPU Based Brute Force Attack Model

</p>

</div>
""",unsafe_allow_html=True)




        st.markdown("### 🔍 Security Component Analysis")


        c1,c2=st.columns(2)



        with c1:

            st.markdown("""
            <div class="card">

            <h3>⚙️ Character Composition</h3>

            </div>
            """,unsafe_allow_html=True)


            elements={
            "Lowercase (a-z)":any(c.islower() for c in password),
            "Uppercase (A-Z)":any(c.isupper() for c in password),
            "Numbers (0-9)":any(c.isdigit() for c in password),
            "Special Characters":any(not c.isalnum() for c in password)
            }


            for name,value in elements.items():

                st.write(
                f"{'✅' if value else '❌'} {name}"
                )



        with c2:

            st.markdown("""
            <div class="card">

            <h3>🛡️ Security Compliance</h3>

            </div>
            """,unsafe_allow_html=True)



            standards={

            "Minimum Length (8+)":
            len(password)>=8,

            "Recommended Length (12+)":
            len(password)>=12,

            "Multi Character Set":
            sum([
            any(c.islower() for c in password),
            any(c.isupper() for c in password),
            any(c.isdigit() for c in password),
            any(not c.isalnum() for c in password)
            ])>=3

            }


            for name,value in standards.items():

                st.write(
                f"{'✅' if value else '❌'} {name}"
                )



        st.markdown("---")

        st.markdown("### 🕵️ Security Risk Assessment")


        risk=max(0,100-score)


        risk_level=(
            "LOW"
            if risk<30
            else
            "MEDIUM"
            if risk<70
            else
            "HIGH"
        )


        st.markdown(f"""
<div style="
background:linear-gradient(145deg,#020617,#111827);
padding:35px;
border-radius:25px;
border:1px solid rgba(56,189,248,0.3);
text-align:center;
">

<div style="
font-size:18px;
color:#94a3b8;
">
Estimated Compromise Risk
</div>


<div style="
font-size:65px;
font-weight:900;
color:{color};
">
{risk:.2f}%
</div>


<div style="
font-size:24px;
color:white;
font-weight:800;
">
{risk_level}
</div>


<p style="
color:#94a3b8;
">
Based on Entropy and Brute Force Resistance Model
</p>


</div>
""",unsafe_allow_html=True)


        st.progress(risk/100)
