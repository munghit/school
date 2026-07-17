import streamlit as st

st.set_page_config(page_title="나침반 프로젝트 연구 발표", layout="wide")

# 스타일 정의
st.markdown("""
<style>
.stApp { background: #0f172a; color: #f1f5f9; }
.card { background: #1e293b; padding: 20px; border-radius: 15px; border-left: 5px solid #38bdf8; margin-bottom: 15px; }
h2 { color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📑 나침반 프로젝트 발표")
menu = st.sidebar.radio("슬라이드 이동", ["서론", "본론: 이론 및 실태", "본론: 문제점 및 해결", "본론: 개선 및 구현", "시뮬레이터"])

# 1. 서론
if menu == "서론":
    st.title("🛡️ 서론: 연구의 배경")
    st.markdown('<div class="card"><h2>연구 동기 및 목적</h2>비밀번호는 인가자와 침입자를 구분하는 첫 번째 방어선입니다. 본 연구는 KISA의 안전 가이드를 기반으로, 사용자가 보안성을 직관적으로 이해하고 실천할 수 있는 데이터 기반의 해결책을 제시하는 데 목적이 있습니다.</div>', unsafe_allow_html=True)

# 2. 본론 1: 이론 및 실태
elif menu == "본론: 이론 및 실태":
    st.title("📖 이론적 배경 및 실태 조사")
    st.markdown("""
    <div class="card">
    <h3>1. 이론적 배경</h3>
    * <b>공격 원리:</b> 무차별 대입 공격은 경우의 수에 의존하며, 문자 집합(N)과 길이(L)의 지수 관계($N^L$)에 따라 해킹 시간이 결정됩니다.
    * <b>수학적 지표:</b> 보안성은 문자 집합 크기와 길이의 함수로 표현되며, 이는 시뮬레이터의 핵심 논리입니다.
    </div>
    <div class="card">
    <h3>2. 관리 실태</h3>
    * 편리함을 위해 숫자 위주의 비밀번호를 여러 사이트에서 중복 사용하는 경향이 확인됨.
    * 보안 의식과 실제 설정 행위 사이에 큰 인지적 간극이 존재합니다.
    </div>
    """)

# 3. 본론 2: 문제점 및 해결사례
elif menu == "본론: 문제점 및 해결":
    st.title("⚠️ 문제점 및 우수 사례 분석")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>문제점 도출</h3><ul><li><b>기술적:</b> 단순 비밀번호는 사전 공격 등에 매우 취약함.</li><li><b>인지적:</b> 안전한 기준에 대한 체계적 정보 부족으로 사용자가 어려움을 겪음.</li></ul></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>우수 사례</h3><ul><li>다중 인증(MFA/2FA) 도입</li><li>비밀번호 관리자(Password Manager) 활용</li><li>웹사이트별 강력한 유효성 검증 정책</li></ul></div>', unsafe_allow_html=True)

# 4. 본론 3: 개선방안 및 구현 도구
elif menu == "본론: 개선 및 구현":
    st.title("💡 개선 방안 및 기술 스택")
    st.markdown("""
    <div class="card">
    <h3>데이터 기반 실시간 보안 시뮬레이션</h3>
    사용자가 비밀번호를 입력함과 동시에 보안성을 시각화하여 '단순 암기'가 아닌 '직접 체험'형 보안 교육을 수행합니다.
    </div>
    <div class="card">
    <h3>핵심 기술 스택 및 구현</h3>
    <ul>
    <li><b>Streamlit:</b> 파이썬 기반의 대화형 보안성 평가 인터페이스 구축.</li>
    <li><b>GitHub:</b> 코드 버전 관리 및 지속 가능한 프로젝트 개발 환경 구축.</li>
    <li><b>구현 효과:</b> 능동적인 보안 습관 형성을 유도하는 혁신적인 개선책 제시.</li>
    </ul>
    </div>
    """)

# 5. 시뮬레이터
elif menu == "시뮬레이터":
    st.title("🛡️ 보안성 시뮬레이터 데모")
    pw = st.text_input("비밀번호 입력", type="password")
    if pw:
        # 이론적 배경에 따른 간이 계산
        score = min(len(pw) * 10, 100) 
        st.write(f"현재 보안 점수: {score}/100")
        st.progress(score / 100)
