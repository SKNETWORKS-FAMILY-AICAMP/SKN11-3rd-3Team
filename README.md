# SKN11-3rd-3Team

**SK네트웍스 Family AI 캠프 11기 3차 프로젝트**

## Team 🐮🐶
    
- 팀원 소개


|  |  |  |  |
|---|---|---|---|   
|[김정원](https://github.com/Kimjeongwon12)|[이민정](https://github.com/minjung2266)|[정민호](https://github.com/Minor1862)|[Down황](https://github.com/junoaplus) |




## 프로젝트 개요
   - 프로젝트 명 : 
   - 프로젝트 소개 : 보드게임 룰 설명과 보드게임 추천을 해주는 LLM 챗봇
   - 프로젝트 필요성(배경) : 보드게임 카페에서 직원을 채용할 때 많은 보드게임 지식이 요구되는데, 조건에 부합하는 직원을 찾는데 많은 어려움이 있습니다.

   - 프로젝트 목표 : 
        - **사용자 시나리오**
            - 게임 이름 입력 → 게임에 대한 소개 및 구성품 설명 → 이해가 안 되는 부분 질문 → 추가 설명
            - 초반 진행 지원(플레이어 수 질문 → 세팅 안내 → 첫 라운드 진행 예시)
            - 게임 중 예외 상황 질문 → 룰 기반 답변 → 차례·행동 안내
        - **핵심 아이디어**
            - 룰 정보는 Vector DB에 저장 → 검색(Retrieval)
            - 대화 흐름, 말투, 예외 처리 로직은 파인튜닝된 LLM이 담당 → Generation
            - 두 시스템 결합으로 유연성과 일관성 동시 확보


## 기술 스택 & 사용한 모델 (임베딩 모델, LLM)

    python
    llama2 70b
    bge-m3
    faiss
    streamlit 

<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">



## 시스템 아키텍처

    graph TD
      A[사용자: Streamlit UI] --> B[백엔드: ]
      B --> C[LLM: LLaMA2 (70B) ]
      B --> D[임베딩 모델: ]
      D --> E[VectorDB: FAISS / Chroma]
      C --> F[챗봇 응답 / 학습 추천]


## WBS

| 일시 | 작업 항목 | 
| --- | --- | 
| 5월 12일 | 기능 구조 설계, 데이터 수집 | 
| 5월 13일 |  | 
| 5월 14일 |  | 
| 5월 15일 | streamlit, readme 작성 | 


## 요구사항 명세서

1. **게임 룰 문서 수집 및 청크화**
    - 각 보드게임별 원본 룰 문서(텍스트) 확보
    - 섹션별(구성품, 목적, 준비, 진행 순서, 행동, 예외 상황, 종료 조건, 확장팩 등)로 200~400 토큰 단위 분할
    - 메타데이터(`game_id`, `section`, `priority`) 부여


## 수집한 데이터 및 전처리 요약



## DB 연동 구현 코드



## 테스트 계획 및 결과 보고서


## 진행 과정 중 프로그램 개선 노력



## 수행결과(테스트/시연 페이지)



## 한 줄 회고

| 김정원 |  | 
| --- | --- | 
| **이민정** |  | 
| **정민호** |  | 
| **황준호** |  | 

