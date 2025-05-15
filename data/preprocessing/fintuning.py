import json
import random
import os
import openai

# OpenAI API 키 설정
openai.api_key = ""

# 데이터 경로 설정
DATA_PATH = '/Users/hwangjunho/Desktop/json데이터/game.json'
OUTPUT_PATH = '/Users/hwangjunho/Desktop/model/fintuning_data.json'

# 질문 패턴 정의
QUESTION_PATTERNS = [
    "이 게임의 룰을 끝까지 상세히 설명해줘.",
    "이 게임을 끝까지 상세히 설명해줘.",
    "이 게임의 초기 세팅은 어떻게 되는지 끝까지 설명해줘.",
    "이 게임에서 각각의 역할은 어떻게 되는지 끝까지 설명해줘.",
    "이 게임의 규칙을 끝까지 설명해줘.",
    "게임에서 분쟁이 발생할 수 있는 부분이 있는지 끝까지 설명해줘.",
    "초보자도 이해할 수 있도록 쉽게 전체 룰을 끝까지 설명해줘.",
    "이 게임의 초기 세팅을 끝까지 도와줘.",
    "이 게임의 첫 번째 라운드 진행을 끝까지 설명해줘."
]

# JSON 형식으로 저장하는 함수
def write_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 이어서 생성하는 함수
def generate_completion(prompt, max_tokens=600):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "이 게임의 규칙에 대해 끝까지 상세히 설명해주는 AI입니다."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error generating completion: {e}")
        return ""

# 데이터셋 생성 함수
def generate_finetuning_data(data_path, num_samples=79):
    with open(data_path, 'r', encoding='utf-8') as f:
        games = json.load(f)

    selected_games = random.sample(games, num_samples)
    dataset = []
    total_requests = len(selected_games) * len(QUESTION_PATTERNS)
    current_request = 0

    for game in selected_games:
        game_name = game.get('game_name', "Unknown Game")
        rules = game.get('text', "No Rules Provided")

        for question in QUESTION_PATTERNS:
            current_request += 1
            prompt = f"게임명: {game_name}\n질문: {question}\nRULES: {rules}"
            
            print(f"[{current_request}/{total_requests}] 요청 중: {game_name} - {question}")

            # 첫 번째 요청
            completion = generate_completion(prompt)

            # 만약 답변이 중간에 끊겼다면 이어서 생성
            while len(completion.split()) >= 580:
                print("답변이 끊겼습니다. 이어서 생성 중...")
                additional_completion = generate_completion(f"{completion} ...")
                completion += " " + additional_completion

            # 데이터셋에 추가
            dataset.append({
                "prompt": prompt,
                "completion": completion.strip()
            })

            # 즉시 저장
            write_json(dataset, OUTPUT_PATH)

    print(f"데이터셋 생성 완료: {OUTPUT_PATH}")
    return dataset

if __name__ == "__main__":
    dataset = generate_finetuning_data(DATA_PATH, num_samples=79)
