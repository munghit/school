import streamlit as st
import math

st.set_page_config(page_title="나침반 프로젝트 연구 발표", layout="wide")

# 스타일 정의
st.markdown("""
<style>
.stApp { background: #0f172a; color: #f1f5f9; }
.card { background: #1e293b; padding: 25px; border-radius: 20px; border: 1px solid #334155; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
h1, h2, h3 { color: #38bdf8; }
.metric-val { font-size: 24px; font-weight: bold; color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📑 나침반 프로젝트 발표")
menu = st.sidebar.radio("슬라이드 이동", ["서론: 연구 개요", "본론: 연구 내용(HWPX 분석)", "결론: 연구 요약", "시뮬레이션: 보안 분석"])

# 1. 서론
if menu == "서론: 연구 개요":
    st.title("🛡️ 디지털 보안 연구 개요")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="card"><h2>연구 동기</h2>취약한 비밀번호로 인한 계정 보안 문제의 중요성을 인식함.</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h2>연구 목적</h2>디지털 문서 보안과 정보보안의 연관성을 탐구하고 보안성을 평가하는 체계적 방법론을 제시함[cite: 1].</div>', unsafe_allow_html=True)

# 2. 본론
elif menu == "본론: 연구 내용(HWPX 분석)":
    st.title("⚙️ 연구 내용: HWPX 데이터 패키지 분석")
    st.markdown('<div class="card"><h2>문서 구조와 정보보안의 상관관계</h2>연구 대상인 HWPX 파일은 단순 텍스트가 아닌 고도로 구조화된 XML 기반의 패키지임[cite: 1]. 문서의 무결성을 지키기 위해 여러 XML 요소가 결합된 구조를 분석함[cite: 1].</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>핵심 데이터 요소[cite: 1]</h3><ul><li><b>container.xml:</b> 리소스 메타데이터 정의</li><li><b>manifest.xml:</b> 콘텐츠 정보 기술</li><li><b>section0.xml:</b> 문서 본문 데이터</li></ul></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>연구 수행 과정[cite: 1]</h3><ul><li>문서 데이터 패키지의 구성 요소 분류</li><li>분산형 XML 구조에서의 데이터 관리 방식 탐구</li><li>정보 보안을 위한 체계적 설계 모델 분석</li></ul></div>', unsafe_allow_html=True)

# 3. 결론
elif menu == "결론: 연구 요약":
    st.title("🎯 연구 결론")
    c1, c2 = st.columns(2)
    c1.markdown('<div class="card"><h3>문서 보안의 체계성</h3>HWPX의 XML 패키지 구조와 같이 정보 보안 또한 체계적이고 파편화된 리소스의 통합 관리가 중요함[cite: 1].</div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>연구 의의</h3>문서 내 스크립트와 메타데이터의 안전한 처리가 정보 보안의 기초임을 확인[cite: 1].</div>', unsafe_allow_html=True)

# 4. 시뮬레이터
elif menu == "시뮬레이션: 보안 분석":
    st.title("🛡️ 보안성 시뮬레이터")
    st.info("보고서의 정보 보안 원리를 적용한 분석 시뮬레이터입니다.")
    pw = st.text_input("비밀번호 입력", type="password")
    if pw:
        # 파일 내의 논리에 기반하여 길이에 따른 단순 보안 강도 평가
        score = min(len(pw) * 10, 100)
        risk = "안전" if score > 70 else "주의/위험"
        st.markdown(f'<div class="card"><h2>분석 결과</h2><p>보안 점수: <span class="metric-val">{score}/100</span></p><p>보안 수준: <span class="metric-val">{risk}</span></p></div>', unsafe_allow_html=True)
        st.progress(score / 100)
