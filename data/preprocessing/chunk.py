import json
import re

def chunk_rule_text(text):
    """
    보드게임 룰 텍스트를 ':'을 기준으로 청킹하는 함수
    특정 패턴(인:, 일시: 등)이 포함된 문장은 제외
    """
    chunks = []
    current_chunk = ""
    
    # 문장 단위로 분리 (마침표, 느낌표, 물음표 기준)
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    for sentence in sentences:
        if not sentence.strip():
            continue
            
        # 제외할 패턴 확인
        exclude_patterns = [
            r'인\s*:', 
            r'일시\s*:', 
            r'이상\s*:',
            r'\d+\s*명\s*:',
            r'\d+\s*인일시\s*:',
            r'\d+\s*~\s*\d+\s*인일시\s*:'
        ]
        
        should_exclude = any(re.search(pattern, sentence) for pattern in exclude_patterns)
        
        # ":" 기준으로 청킹 (제외 패턴이 아닌 경우만)
        if ":" in sentence and not should_exclude:
            # 현재 청크가 있으면 저장
            if current_chunk:
                chunks.append(current_chunk.strip())
                current_chunk = ""
            # 새 청크 시작
            current_chunk = sentence
        else:
            # 현재 청크 계속 이어가기
            if current_chunk:
                current_chunk += " " + sentence
            else:
                current_chunk = sentence
    
    # 마지막 청크 추가
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

# 보드게임 룰 처리 함수
def process_game_rules(input_file, output_file):
    # JSON 파일 읽기
    with open(input_file, 'r', encoding='utf-8') as file:
        games_data = json.load(file)
    
    # 결과 저장할 딕셔너리
    result = {}
    
    # 각 게임 처리
    for game in games_data:
        game_id = game["id"]
        game_name = game["game_name"]
        rule_text = game["text"]
        
        # 룰 텍스트 청킹
        chunks = chunk_rule_text(rule_text)
        
        # 결과 저장
        result[game_id] = {
            "game_name": game_name,
            "chunks": chunks
        }
    
    # 결과를 JSON 파일로 저장
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=2)
    
    return result

# 실행 함수
def main():
    # 파일 경로
    input_file = "/Users/hwangjunho/Desktop/json데이터/game.json"
    output_file = "/Users/hwangjunho/Desktop/chunked.json"
    
    # 게임 룰 처리
    result = process_game_rules(input_file, output_file)
    
    # 결과 요약 출력
    print(f"청킹 완료: {output_file}에 저장되었습니다.")
    print(f"처리된 게임 수: {len(result)}")
    
    # 첫 번째 게임의 청크 예시 출력
    first_game_id = list(result.keys())[0]
    print(f"\n게임 이름: {result[first_game_id]['game_name']}")
    print(f"청크 수: {len(result[first_game_id]['chunks'])}")
    print("\n첫 번째 청크 예시:")
    print(result[first_game_id]['chunks'][0])

if __name__ == "__main__":
    main()
