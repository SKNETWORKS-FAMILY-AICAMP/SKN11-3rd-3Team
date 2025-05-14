# SKN11-3rd-3Team
- 주제 : LLM 기반 보드게임 룰 설명 & 맞춤형 추천 챗봇
- 개발기간 : 25.05.07~25.05.15

---
## 1. 팀 소개
- 팀명 : Battle of Minds | devil's plan | 타짜
- 서비스명 : 보디 |두봇 | 보봇


### 👤 팀원
<table>
  <thead>
    <td align="center">
      <a href="https://github.com/Kimjeongwon12">
        <img src=""/><br /><hr/>
        김정원
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/minjung2266">
        <img src=""/><br /><hr/>
        이민정
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/Minor1862">
        <img src=""/><br /><hr/>
        정민호
      </a><br />
    </td>
    <td align="center">
      <a href="https://github.com/junoaplus">
        <img src=""/><br /><hr/>
        황준호
      </a><br />
    </td>
  </thead>
</table>

<br/>


## 2. Overview

  #### 📖 프로젝트 소개 
"보디"는 보드게임 룰 설명과 추천 기능을 제공하는 LLM 기반 챗봇입니다. 챗봇은 사용자의 질문에 따라 게임 규칙을 설명하거나 취향에 맞는 게임을 추천해줍니다.

#### ⭐ 프로젝트 필요성
<table>
  <tr>
    <td>초보자들의 게임 선택 장애</td>
    <td>보드게임의 대중화로 다양한 게임이 출시되고 있지만, 초보 이용자들은 복잡한 룰을 이해하거나 자신의 취향에 맞는 게임을 고르는 데 어려움을 겪는다.</td>
  </tr>
  <tr>
    <td>보드게임 카페의 인력 문제</td>
    <td>보드게임 카페에서는 다양한 게임을 설명하고 추천할 수 있는 직원을 필요로 하지만, 폭넓은 게임 지식을 갖춘 인력을 채용하기란 쉽지 않다.</td>
  </tr>
</table>

#### 🎯 프로젝트 목표

<table>
  <tr>
    <td>보드게임 룰 설명 챗봇 구현</td>
    <td>사용자의 질문에 정확하고 간결한 게임 규칙을 제공</td>
  </tr>
  <tr>
    <td>보드게임 추천 기능 제공</td>
    <td>게임 방법, 인원 수, 테마 등을 기반으로 유사도 분석을 통해 최적의 보드게임을 추천</td>
  </tr>
  <tr>
    <td>도메인 특화 지식 반영</td>
    <td>벡터DB 구축과 LLM 파인튜닝을 통해 보드게임에 특화된 지식 기반 챗봇 구축</td>
  </tr>
</table>

<hr>

## 3. 기술 스택

| 항목                | 내용 |
|---------------------|------|
| **Language**        | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Development**     | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)<br>![Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)<br>![RunPod](https://img.shields.io/badge/RunPod-8A2BE2?style=for-the-badge) |
| **Embedding Model** | ![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black) |
| **Vector DB**       | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge) |
| **LLM Model**       | ![Qwen](https://img.shields.io/badge/OpenChat%20V3-4285F4?style=for-the-badge&logo=google&logoColor=white) |
| **Demo**            | ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) |
| **Collaboration Tool** | ![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)<br>![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)


## 4. 시스템 아키텍처

![diagram](https://github.com/user-attachments/assets/f3a87011-9285-41a3-9932-b20db7992b11)

1. 질문 입력
→ 원하는 서비스에 따라 user가 질문 입력 

2. 문서 검색
→ Retriver가 받은 질문을 임베딩 후, Vector DB에서 유사한 문장을 질의 

3. Prompt 구성 
→ 검색된 정보를 기반으로 LLM에게 전달할 Prompt 구성 

4. 모델 응답 생성
→ Prompt가 Fine-Tuning된 모델에게 전달되어 응답을 생성

5. 생성된 답변을 User에게 반환
→ LLM이 생성한 답변이 사용자에게 전달


## 5. WBS
![image](https://github.com/user-attachments/assets/edcfd623-1383-48dd-a661-5110a4a31204)


## 6. 요구사항 명세서
![image](https://github.com/user-attachments/assets/a5f797f5-77cf-4c94-99f2-51373c47e440)



## 7. 수집한 데이터 및 전처리 요약
[데이터 수집]

[데이터 전처리]




## 8. DB 연동 구현 코드



## 9. 테스트 계획 및 결과 보고서


## 10. 성능 개선 노력


## 11. 시연 페이지

## 12. 추후 개선점

## 13. 한 줄 회고

| 김정원 |  | 
| --- | --- | 
| **이민정** |  | 
| **정민호** |  | 
| **황준호** |  | 

