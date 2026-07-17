import streamlit as st
import math

st.set_page_config(page_title="보안 연구 발표", layout="wide")

st.markdown("""
<style>
.stApp { background: #020617; color: #e2e8f0; font-family: 'Pretendard', sans-serif; }
.card { background: #111827; padding: 20px; border-radius: 15px; border: 1px solid #334155; margin-bottom: 15px; }
h1 { color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

st.title("🛡️ 디지털 보안 연구 발표")
page = st.sidebar.radio("슬라이드", ["1. 연구 개요", "2. 탐구 과정", "3. 시뮬레이터"])

if page == "1. 연구 개요":
    st.subheader("🔐 비밀번호 보안성 정량 분석")
    st.markdown("""
    * **동기:** 복잡성 강제 방식의 한계를 극복하고 공격 저항성을 수학적으로 분석
    * **목적:** 엔트로피 기반 보안 평가 및 패스프레이즈 모델의 효율성 입증[cite: 1]
    * **도구:** Python(Streamlit)을 활용한 시뮬레이터 개발 및 GitHub 배포[cite: 1]
    """)

elif page == "2. 탐구 과정":
    st.subheader("⚙️ 연구 및 개발 단계")
    st.markdown("""
    * **분석:** HWPX 패키지 아키텍처(XML/메타데이터) 구조 분석[cite: 1]
    * **설계:** 암호학적 엔트로피 수학 모델링[cite: 1]
    * **환경:** GPU 기반 무차별 대입 공격 시뮬레이션 환경 가정[cite: 1]
    * **구현:** Streamlit 웹 인터페이스 구축 및 GitHub 형상 관리[cite: 1]
    """)
    st.info("※ 연구 대상 파일(HWPX)은 container.xml, manifest.xml 등 분산형 XML 구조로 보안성 연구의 데이터 모델로 활용[cite: 1]")

elif page == "3. 시뮬레이터":
    st.subheader("🛡️ 실시간 보안성 평가")
    password = st.text_input("🔑 테스트할 비밀번호 입력", type="password")
    if password:
        entropy = len(password) * math.log2(95) # 기본 예시
        score = min(int(entropy * 1.5), 100)
        risk = max(0, 100 - score)
        
        c1, c2 = st.columns(2)
        c1.metric("보안 점수", f"{score}/100")
        c2.metric("위험도", "높음" if risk > 70 else "안전")
        st.progress(risk / 100)
