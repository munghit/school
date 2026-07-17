import streamlit as st

st.set_page_config(page_title="나침반 프로젝트 상세 연구 발표", layout="wide")

# 스타일 정의
st.markdown("""
<style>
.stApp { background: #0f172a; color: #f1f5f9; }
.card { background: #1e293b; padding: 25px; border-radius: 20px; border-left: 5px solid #38bdf8; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
h1, h2, h3 { color: #38bdf8; }
.content-text { font-size: 1.1em; line-height: 1.6; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📑 나침반 프로젝트 상세")
menu = st.sidebar.radio("슬라이드 이동", ["서론: 연구 동기 및 목적", "본론: HWPX 데이터 패키지 분석", "본론: 기술적 구조 상세", "결론: 연구 의의", "시뮬레이션: 보안 분석"])

# 1. 서론
if menu == "서론: 연구 동기 및 목적":
    st.title("🛡️ 서론: 연구의 출발점")
    st.markdown('<div class="card content-text"><h2>연구 동기</h2>디지털 환경에서 계정 탈취의 주요 원인인 취약한 비밀번호 문제의 심각성을 인식하고, 정보 보안의 기초를 탐구하고자 함.</div>', unsafe_allow_html=True)
    st.markdown('<div class="card content-text"><h2>연구 목적</h2>HWPX 파일과 같은 복잡한 디지털 문서 패키지의 구조를 분석하여, 정보 보안을 위한 체계적인 데이터 관리 모델과 보안성 평가의 필요성을 제시함[cite: 1].</div>', unsafe_allow_html=True)

# 2. 본론: HWPX 패키지 분석
elif menu == "본론: HWPX 데이터 패키지 분석":
    st.title("⚙️ 본론: 연구 대상 HWPX 패키지")
    st.markdown('<div class="card content-text"><h2>데이터 구조의 이해</h2>연구 대상인 HWPX 파일은 단일 파일이 아니라, 여러 XML 파일이 패키징된 복합적인 디지털 구조를 가짐[cite: 1]. 문서 내 데이터의 파편화와 통합 관리 방식은 정보 보안의 원리와 맞닿아 있음[cite: 1].</div>', unsafe_allow_html=True)
    st.markdown('<div class="card content-text"><h2>핵심 구성 요소</h2><ul><li><b>XML 기반 데이터:</b> 문서의 내용은 다수의 XML 파일로 분할되어 처리됨[cite: 1].</li><li><b>리소스 무결성:</b> container.rdf 및 container.xml을 통해 전체 문서의 리소스 종속성을 관리함[cite: 1].</li><li><b>동적 제어:</b> 스크립트(Scripts)와 설정 파일(settings.xml)이 문서의 동적 동작을 제어함[cite: 1].</li></ul></div>', unsafe_allow_html=True)

# 3. 본론: 기술적 상세
elif menu == "본론: 기술적 구조 상세":
    st.title("🔍 본론: 상세 구조 및 메타데이터")
    st.markdown('<div class="card content-text"><h2>상세 분석 데이터[cite: 1]</h2><ul><li><b>container.xml:</b> 전체 패키지의 메타데이터 정의 및 종속성 관리의 핵심[cite: 1].</li><li><b>manifest.xml:</b> 문서 내부의 콘텐츠 정보를 구체적으로 기술함[cite: 1].</li><li><b>section0.xml:</b> 실제 본문의 데이터가 담긴 영역으로 문서의 핵심 정보를 보유함[cite: 1].</li><li><b>header.xml & content.hpf:</b> 문서의 레이아웃 헤더 및 패키징 스키마를 정의하여 데이터 정합성을 확보함[cite: 1].</li></ul></div>', unsafe_allow_html=True)

# 4. 결론
elif menu == "결론: 연구 의의":
    st.title("🎯 결론: 연구의 의의")
    st.markdown('<div class="card content-text"><h2>문서 보안과 정보 시스템</h2>HWPX 파일의 XML 패키징 방식은 데이터의 구조적 안전성을 확보하는 중요한 사례임[cite: 1].</div>', unsafe_allow_html=True)
    st.markdown('<div class="card content-text"><h2>종합 요약</h2>정보 보안은 파편화된 리소스들을 체계적으로 통합하고, 각 메타데이터의 정합성을 유지하는 것에서 시작됨[cite: 1]. 본 연구는 데이터 패키지 구조 분석을 통해 정보 보안의 기술적 토대를 확인하였음[cite: 1].</div>', unsafe_allow_html=True)

# 5. 시뮬레이션
elif menu == "시뮬레이션: 보안 분석":
    st.title("🛡️ 보안성 시뮬레이터")
    pw = st.text_input("비밀번호 입력", type="password")
    if pw:
        score = min(len(pw) * 10, 100)
        st.markdown(f'<div class="card"><h2>분석 결과</h2><p>입력된 정보의 길이 기반 보안 점수: <b>{score}/100</b></p><p>파일 패키지 구조 분석의 원리에 따라 정보의 복잡도와 정합성을 평가합니다.</p></div>', unsafe_allow_html=True)
        st.progress(score / 100)
