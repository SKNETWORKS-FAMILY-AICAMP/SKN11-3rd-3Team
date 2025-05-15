import openai
import json
import time
import os

# === API 키 설정 ===
# 환경변수 OPENAI_API_KEY에 키를 설정하거나, 아래에 직접 입력하세요.
api_key = ""
openai.api_key = api_key


# === 데이터 경로 설정 ===
DATA_PATH = "/Users/hwangjunho/Desktop/model/fintuning_data.json"  # 변환 전 원본 JSON 파일

# === JSON → JSONL 변환 함수 ===
def convert_data_for_fine_tuning(input_file, output_file):
    """
    [{"prompt":..., "completion":...}, ...] 포맷의 JSON을
    {"messages":[{"role":"user",...}, {"role":"assistant",...}]} 형태의 JSONL로 변환
    """
    print(f"데이터 변환 중: {input_file} → {output_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    formatted = []
    for item in data:
        if 'prompt' not in item or 'completion' not in item:
            print(f"[경고] prompt/completion 누락: {item}")
            continue

        # User 메시지 + Assistant 응답 구성
        messages = [
            {"role": "user", "content": item['prompt'].strip()},
            {"role": "assistant", "content": item['completion'].strip()}
        ]
        formatted.append({"messages": messages})

    # JSONL로 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        for entry in formatted:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"변환 완료: 총 {len(formatted)}개 → {output_file}")
    return output_file

# === 파일 업로드 ===
def upload_training_file(file_path):
    print(f"파일 업로드 중: {file_path}")
    resp = openai.File.create(
        file=open(file_path, 'rb'),
        purpose="fine-tune"
    )
    file_id = resp["id"]
    print(f"업로드 완료. File ID: {file_id}")
    return file_id

# === 파인튜닝 작업 생성 ===
def create_fine_tuning_job(training_file_id, model="gpt-3.5-turbo"):
    print(f"파인튜닝 작업 생성: model={model}, file={training_file_id}")
    resp = openai.FineTuningJob.create(
        training_file=training_file_id,
        model=model
    )
    job_id = resp.id
    print(f"Job ID: {job_id}")
    return job_id

# === 상태 조회 ===
def check_fine_tuning_status(job_id):
    resp = openai.FineTuningJob.retrieve(job_id)
    status = resp.status
    print(f"[Status] {status}")
    if status == "succeeded":
        print(f"생성된 모델 ID: {resp.fine_tuned_model}")
    elif status == "failed":
        print(f"실패 사유: {resp.error}")
    return status, resp

# === 완료 대기 ===
def wait_for_fine_tuning_completion(job_id, check_interval=60, max_wait_time=3600):
    elapsed = 0
    while elapsed < max_wait_time:
        status, resp = check_fine_tuning_status(job_id)
        if status in ["succeeded", "failed", "cancelled"]:
            return resp.fine_tuned_model if status == "succeeded" else None
        print(f"{check_interval}초 대기 후 재조회…")
        time.sleep(check_interval)
        elapsed += check_interval

    print("[경고] 대기 시간 초과. 수동 확인 필요.")
    return None

# === 테스트 요청 ===
def test_fine_tuned_model(model_id, prompt):
    print(f"파인튜닝된 모델 테스트: {model_id}")
    resp = openai.ChatCompletion.create(
        model=model_id,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.7
    )
    answer = resp.choices[0].message.content
    print("=== 테스트 응답 ===")
    print(answer)
    return answer

# === 메인 실행 ===
def main():
    # 1) JSON → JSONL 변환
    jsonl_file = "formatted_training_data.jsonl"
    convert_data_for_fine_tuning(DATA_PATH, jsonl_file)

    # 2) 업로드
    file_id = upload_training_file(jsonl_file)

    # 3) 파인튜닝 Job 생성
    job_id = create_fine_tuning_job(file_id, model="gpt-3.5-turbo")

    # 4) 완료 대기
    model_id = wait_for_fine_tuning_completion(job_id)
    if not model_id:
        print("파인튜닝 실패 또는 중단됨.")
        return

    # 5) 테스트
    test_prompt = "이 게임 룰 전체를 처음부터 끝까지 간단히 알려주세요."
    test_fine_tuned_model(model_id, test_prompt)

    print(f"\n🎉 파인튜닝 완료! 새 모델 ID: {model_id}")

if __name__ == "__main__":
    main()
