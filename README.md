![image](https://github.com/user-attachments/assets/bf50ee61-ab80-4d68-bfce-770ba0eff9f8)# SKN11-3rd-3Team
- 주제 : LLM 기반 보드게임 룰 설명 & 맞춤형 추천 챗봇
- 개발기간 : 25.05.07~25.05.15
---

## 1. 팀 소개
- 팀명 : Devil's plan
- 서비스명 : 🤖 보봇


### 👤 팀원
<table>
  <thead>
    <tr>
      <td align="center">
        <img src="이미지1_URL" width="100" /><br />
        <a href="https://github.com/Kimjeongwon12">김정원</a>
      </td>
      <td align="center">
        <img src="이미지2_URL" width="100" /><br />
        <a href="https://github.com/minjung2266">이민정</a>
      </td>
      <td align="center">
        <img src="이미지3_URL" width="100" /><br />
        <a href="https://github.com/Minor1862">정민호</a>
      </td>
      <td align="center">
        <img src="이미지4_URL" width="100" /><br />
        <a href="https://github.com/junoaplus">황준호</a>
      </td>
    </tr>
  </thead>
</table>

<br/>


## 2. Overview

  #### 📖 프로젝트 소개 
보드게임 봇 "보봇"은 보드게임 룰 설명과 추천 기능을 제공하는 LLM 기반 챗봇입니다. 챗봇은 사용자의 질문에 따라 게임 규칙을 설명하거나 취향에 맞는 게임을 추천해줍니다.

#### ⭐ 프로젝트 필요성
<table>
  <tr>
    <td>초보자들의 게임 선택 장애</td>
    <td>보드게임의 대중화로 다양한 게임이 출시되고 있지만, 초보 이용자들은 복잡한 룰을 이해하거나 자신의 취향에 맞는 게임을 고르는 데 어려움을 겪음</td>
  </tr>
  <tr>
    <td>보드게임 카페의 인력 문제</td>
    <td>보드게임 카페에서는 다양한 게임을 설명하고 추천할 수 있는 직원을 필요로 하지만, 폭넓은 게임 지식을 갖춘 인력을 채용하기란 쉽지 않음</td>
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
| **LLM Model**       | ![gpt-3.5-turbo](https://img.shields.io/badge/gpt--3.5-4B91FF?style=for-the-badge&logo=openai&logoColor=white) |
| **Demo**            | ![Gradio](https://img.shields.io/badge/Gradio-FF4B4B?style=for-the-badge&logo=gradio&logoColor=white) |
| **Collaboration Tool** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)


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
### 데이터 수집

  - BeautifulSoup 을 통해 225개의 게임 정보들이 적혀있는 보드게임 카페에서 데이터를 크롤링해왔다.

[보드게임 블로그 사이트](https://blog.naver.com/mukjjippa_boardgame)


### 데이터 전처리
✅ 원본 데이터 전처리
- 전처리 형식

| 원본 형태                             | 변환 방식                                          |
|----------------------------------|-------------------------------------------------|
| `@`, `☆`와 같은 특수문자                              | → 모두 제거                               |
| `- 2 인 -`, `- 4 인 -` 등               | → `2인일 시:`, `4인일 시:` 형태로 변환                    |
| 2~4인        | → `인`을 제거 / player 정보가 없을 시 ~로 처리 |
| 전체 문장 띄어쓰기 및 맞춤법               | → 맞춤법 교정, 불필요한 공백 제거, 문장부호 보정 적용              |


- 전처리 전 / 전처리 후

```
  [{
    "id": "블로커스_보드게임",
    "game_name": "블로커스 보드게임",
    "section": "RULES",
    "text": "게임 의 목적 - 하나라도 많은 블록을 놓으세요 게임 종료 시점 - 게임 플레이 어 모두가 더 이 상 블록을 놓지 못하는 상황이 되면 게임 종료이 며 남은 블록의 면적이 가 장 작은 플레이 어가 승리합니다 블록의 네모를 세서 면적을 계산하세요 게임 플레이 @자신의 차례가 되면 블록을 1 개 놓으면차례가 넘어갑니다@자신의 첫 블록은 모서리의 면을 채워야 합니다 @같은 색상의 블록은 꼭짓점이 닿아야 합니다 같은 색상의 블록은 면이 닿을 수 없습니다 게임 세팅 - 4 인 - 원하는 색상의 블록 조각을 21 개씩 1 가 지 색상으로 가 져갑니다 3 인 - 1 가 지 색상을 가 져가 고 남은 1 가 지 색상의 차례에 는 돌아가 면서 블록을 놓습니다 (4 인이 랑 같은 방식인데 1 명의 역할을 3 명이 합니다) 2 인 - 2 가 지 색상의 블록을 총 42 개 가 져옵니다 4 인 플레이 와 같은 방식으로 진행합니다 ☆블로 커스는 2 인용이 따로 있습니다 이 상 블로 커스 보드게임 규칙 (2~4 인) 이 었습니다",
    "source_file": "블로커스 보드게임 규칙(2~4인)",
    "players": "2~4인"
  },
...
```

```
[{
  "id": "블로커스_보드게임",
  "game_name": "블로커스 보드게임",
  "section": "RULES",
  "text": "게임의 목적: 하나라도 많은 블록을 놓는 것입니다. 게임 종료 시점: 모든 플레이어가 더 이상 블록을 놓지 못하는 상황이 되면 게임이 종료되며, 남은 블록의 면적이 가장 작은 플레이어가 승리합니다. 블록의 네모 칸 수를 세어 면적을 계산하세요. 게임 플레이: 자신의 차례가 되면 블록을 1개 놓고 차례를 넘깁니다. 첫 블록은 반드시 모서리에 닿도록 놓아야 합니다. 같은 색상의 블록은 꼭짓점만 닿아야 하며, 면이 닿으면 안 됩니다. 게임 세팅: 4인일 시: 원하는 색상의 블록 조각 21개를 하나씩 선택합니다. 3인일 시: 각자 1가지 색상의 블록을 가져가고, 남은 1가지 색상의 차례에는 돌아가면서 블록을 놓습니다. (4인 방식과 동일하나, 한 명의 역할을 3명이 번갈아 합니다) 2인일시: 두 가지 색상의 블록을 총 42개 가져와 4인 플레이 방식과 동일하게 진행합니다. 블로커스는 2인 전용 버전도 별도로 존재합니다.",
  "players": "2~4"
}]

```

✅ vectorDB 전처리
-  게임 추천 기능 : 원본 데이터 전처리와 동일하게 진행함. 


- 게임 룰 설명 기능 : 설명 단위로 청크하여 전처리 진행함.
  ```
  "블로커스": {
    "game_name": "블로커스",
    "chunks": [
      "게임의 목적: 하나라도 많은 블록을 놓는 것입니다.",
      "게임 종료 시점: 모든 플레이어가 더 이상 블록을 놓지 못하는 상황이 되면 게임이 종료되며, 남은 블록의 면적이 가장 작은 플레이어가 승리합니다. 블록의 네모 칸 수를 세어 면적을 계산하세요. 게임 플레이: 자신의 차례가 되면 블록을 1개 놓고 차례가 넘어갑니다. 첫 블록은 반드시 모서리에 닿도록 놓아야 합니다. 같은 색상의 블록은 꼭짓점이 닿아야 하며, 면이 닿으면 안 됩니다. 게임 세팅: 4인일 시: 원하는 색상의 블록 조각을 21개씩 하나씩 가져갑니다. 3인일 시: 각자 1가지 색상의 블록을 가져가고, 남은 1가지 색상의 차례에는 돌아가면서 블록을 놓습니다. (4인 방식과 동일하나,  한 명의 역할을 3명이 번갈아 합니다.) 2인일 시: 두 가지 색상의 블록을 총 42개 가져와 4인 플레이 방식과 동일하게 진행합니다. 블로커스는 2인 전용 버전도 별도로 존재합니다.."
    ]
  }
  ```


✅ 파인튜닝 전처리



## 8. DB 연동 구현 코드
```
```



## 9. 테스트 계획 및 결과 보고서
1. **LoRA 파라미터 조정** :

## 10. 성능 개선 노력
1. **목적에 따른 벡터DB 분리** : 추천 기능과 룰 설명 기능이 요구하는 정보가 달라 벡터DB를 별도로 구축함으로써, 검색 정확도를 높임

2. **RAG 모델 실험** :
다양한 LLM 모델 (OpenChat, TinyLlama, KoAlpaca)를 비교하여 응답 성능을 개선

3. **Finetunning 성능 개선을 위한 모델 변경** : KoAlpaca -> GPT-3.5-turbo


## 11. 시연 페이지

## 12. 추후 개선점
#### 1. 사용자 인터렉션 강화
- 꼬리질문 대응을 위해 세션 상태 유지
- 자주 선택한 게임 유형을 저장해 개인화 추천 강화

#### 2. 데이터 품질 개선
- 게임 정보 크롤링 자동화를 통해 최근 게임 업데이트


#### 3. 모델 성능 향상
- 비용 절감을 위해 다른 모델 적용 방법을 모색
- 꼬리질문 대응에 특화된 LoRA 개선

## 13. 한 줄 회고                                                                                                               
>  김정원 : LLM을 사용만 해보고 개발하는 것은 처음이라 관련 지식들을 처음 접하는 것이 많았습니다. 이번 프로젝트를 진행하면서 개발 프로세스를 어떻게 잡아야 하는지, 수많은 임베딩, RAG, LLM 모델 중에서 어떤 모델을 사용해야 우리의 프로젝트 결과물에 가장 우수한 성능을 낼 수 있는지 알 수 있었습니다. GPU 자원과 시간이 한정적이라 A-Z로 완벽히 구축하지 못한 것 같아 아쉽지만 이후에 어떻게 발전시킬 지 생각해 볼 수 있었던 시간이었습니다. 
>
> 이민정 : 여러 모델을 바꿔가며 RAG의 성능을 확인하는 과정에서 단순히 성능이 좋다는 모델보다는 내가 필요한 목적에 따라 알맞게 모델을 선택해야 함을 알게 되었습니다. 또 gpu 자원과 시간이 한정되어 있어 여러번 테스트 해보지 못한점이 아쉬움이 남습니다.
>
>  정민호 :                                                                                         
>
>  황준호 : 
