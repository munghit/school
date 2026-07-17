import streamlit as st
import math

st.set_page_config(page_title="보안 연구 발표 자료", layout="wide")

# 스타일 정의
st.markdown("""
<style>
.stApp { background: #0f172a; color: #f1f5f9; }
.card { background: #1e293b; padding: 25px; border-radius: 20px; border: 1px solid #334155; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
h1, h2 { color: #38bdf8; }
.metric-val { font-size: 24px; font-weight: bold; color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("📑 발표 목차")
menu = st.sidebar.radio("슬라이드 이동", ["서론: 연구 개요", "본론: 탐구 과정", "결론: 연구 결과", "시뮬레이션: 데모"])

# 1. 서론
if menu == "서론: 연구 개요":
    st.title("🛡️ 디지털 보안 연구 개요")
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<div class="card"><h2>연구 동기</h2>취약한 비밀번호로 인한 계정 탈취 문제 해결의 필요성[cite: 1]. 기존의 강제적인 복잡성 규칙이 주는 사용자 경험 저하를 극복하고, 수학적 엔트로피 기반의 과학적 접근을 도모함[cite: 1].</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="card"><h2>연구 목적</h2>비밀번호 보안성을 수치화하여 객관적인 지표 제공[cite: 1]. 사용성과 보안성 간의 최적 균형점인 패스프레이즈(Passphrase) 모델 검증[cite: 1].</div>', unsafe_allow_html=True)

# 2. 본론
elif menu == "본론: 탐구 과정":
    st.title("⚙️ 연구 및 개발 과정")
    st.markdown('<div class="card"><h2>연구 방법론: 디지털 패키지 구조 분석</h2>HWPX 파일은 단순 문서가 아닌 고도로 구조화된 XML 패키지임[cite: 1]. 각 컴포넌트(container, manifest, section 등)의 데이터 무결성을 유지하듯, 보안 모델 또한 체계적인 구조 위에서 설계됨[cite: 1].</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>연구 단계</h3><ul><li>HWPX 아키텍처 분석[cite: 1]</li><li>엔트로피 수학 모델링[cite: 1]</li><li>공격 모델(GPU) 가정[cite: 1]</li></ul></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>구현 환경</h3><ul><li>프레임워크: Streamlit[cite: 1]</li><li>배포: GitHub CI/CD[cite: 1]</li><li>언어: Python 기반 연산[cite: 1]</li></ul></div>', unsafe_allow_html=True)

# 3. 결론
elif menu == "결론: 연구 결과":
    st.title("🎯 연구 결론")
    c1, c2, c3 = st.columns(3)
    c1.markdown('<div class="card"><h3>암호학적 효율성</h3>지수적인 길이 증가가 공격자의 연산 복잡도를 압도함[cite: 1].</div>', unsafe_allow_html=True)
    c2.markdown('<div class="card"><h3>인지적 효율성</h3>패스프레이즈 모델이 보안과 사용성 확보의 핵심임[cite: 1].</div>', unsafe_allow_html=True)
    c3.markdown('<div class="card"><h3>보안적 경제성</h3>12자 이상 구성 시 방어 비용이 공격 비용을 초과함[cite: 1].</div>', unsafe_allow_html=True)

# 4. 시뮬레이터
elif menu == "시뮬레이션: 데모":
    st.title("🛡️ 보안성 시뮬레이터")
    pw = st.text_input("비밀번호 입력", type="password")
    if pw:
        entropy = len(pw) * 5
        score = min(entropy, 100)
        risk = "안전" if score > 70 else "위험"
        st.markdown(f'<div class="card"><h2>분석 결과</h2><p>보안 점수: <span class="metric-val">{score}/100</span></p><p>위험도 평가: <span class="metric-val">{risk}</span></p></div>', unsafe_allow_html=True)
        st.progress(score / 100)
