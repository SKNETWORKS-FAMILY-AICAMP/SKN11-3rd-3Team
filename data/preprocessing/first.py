import os
import json
import re

def clean_text(text):
    """
    벡터 DB를 위한 고급 텍스트 정제 함수
    """
    # 줄바꿈을 공백으로 대체
    text = text.replace('\n', ' ')
    
    # 연속된 공백을 하나로 줄이기
    text = re.sub(r'\s+', ' ', text)
    
    # 특수 문자 처리
    text = text.replace('★', '')
    
    # 하이픈(-) 및 기타 부호 주변 공백 처리
    text = re.sub(r'(\-)([^\s])', r'\1 \2', text)
    text = re.sub(r'([^\s])(\-)', r'\1 \2', text)
    
    # 구분 기호 주변에 공백 추가 - 정규식 이스케이프 처리
    text = re.sub(r'(\,)([^\s])', r'\1 \2', text)  # 쉼표
    text = re.sub(r'(\.)([^\s])', r'\1 \2', text)  # 마침표
    text = re.sub(r'(\!)([^\s])', r'\1 \2', text)  # 느낌표
    text = re.sub(r'(\?)([^\s])', r'\1 \2', text)  # 물음표
    text = re.sub(r'(\:)([^\s])', r'\1 \2', text)  # 콜론
    text = re.sub(r'(\;)([^\s])', r'\1 \2', text)  # 세미콜론
    
    # 숫자와 글자 사이에 공백 추가
    text = re.sub(r'([0-9])([가-힣A-Za-z])', r'\1 \2', text)
    text = re.sub(r'([가-힣A-Za-z])([0-9])', r'\1 \2', text)
    
    # 괄호 주변 공백 처리
    text = re.sub(r'([^\s])([\(])', r'\1 \2', text)  # 여는 괄호
    text = re.sub(r'([\)])([^\s])', r'\1 \2', text)  # 닫는 괄호
    
    # 한글 조사 다음에 오는 단어 띄어쓰기 처리
    for particle in ['은', '는', '이', '가', '을', '를', '에', '의', '로', '와', '과', '도', '만', '에서', '으로']:
        text = re.sub(f'({particle})([가-힣])', f'\\1 \\2', text)
    
    # 문장 종결 후 새 문장 시작 시 공백 추가
    for ending in ['다', '요', '죠', '지만', '음', '함', '임', '봄', '됨', '암', '니다', '세요']:
        text = re.sub(f'({ending})([가-힣A-Za-z0-9])', f'\\1 \\2', text)
    
    # 영어 단어 사이에 공백 추가
    text = re.sub(r'([a-zA-Z])([가-힣])', r'\1 \2', text)
    text = re.sub(r'([가-힣])([a-zA-Z])', r'\1 \2', text)
    
    # 일반적인 띄어쓰기 오류 수정 (보드게임 특화)
    game_terms = {
        '카드를': '카드를 ',
        '카드는': '카드는 ',
        '카드가': '카드가 ',
        '게임은': '게임은 ',
        '플레이어는': '플레이어는 ',
        '사용합니다': '사용합니다 ',
        '가져갑니다': '가져갑니다 ',
        '버립니다': '버립니다 ',
        '확인합니다': '확인합니다 ',
        '제거합니다': '제거합니다 ',
        '시작합니다': '시작합니다 ',
        '진행합니다': '진행합니다 '
    }
    
    for term, replacement in game_terms.items():
        text = text.replace(term, replacement)
    
    # 연속된 공백을 다시 한 번 하나로 줄이기
    text = re.sub(r'\s+', ' ', text)
    
    # 앞뒤 공백 제거
    text = text.strip()
    
    return text

# 디렉토리 경로
directory_path = "/Users/hwangjunho/Desktop/fist_preprocessing_data"

# 결과를 저장할 리스트
json_data = []

# 디렉토리 내의 모든 파일 순회
for filename in os.listdir(directory_path):
    if filename.endswith(".txt") and not filename.startswith('.'):
        file_path = os.path.join(directory_path, filename)
        
        # 원본 파일명에서 게임 이름과 인원수 정보 추출 시도
        game_name_match = re.search(r'([가-힣a-zA-Z0-9\s]+)(?:\s+보드게임|\s+카드|\s+규칙|\s+하는\s*법|\s+룰)', filename)
        players_match = re.search(r'(\d+)(?:인|명|인용|~|\s*(?:-|–)\s*)(\d+)(?:인|명|인용)?', filename)
        
        # 게임 이름과 인원수 기본값 설정
        game_name = "알 수 없음"
        players = "정보 없음"
        
        # 게임 이름 추출 성공 시 저장
        if game_name_match:
            game_name = game_name_match.group(1).strip()
        else:
            # 게임 이름이 추출되지 않았다면 파일명에서 .txt 제거하여 저장
            game_name = filename.replace(".txt", "")
            
            # 네이버 블로그 부분과 기타 패턴 제거
            game_name = game_name.replace("  네이버 블로그", "")
            game_name = re.sub(r'\s*\([0-9~\-]+인.*?\)', '', game_name)
            game_name = game_name.strip()
        
        # 인원수 정보 추출 성공 시 저장
        if players_match:
            min_players = players_match.group(1)
            max_players = players_match.group(2)
            players = f"{min_players}~{max_players}인"
        
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 텍스트 정제
        clean_content = clean_text(content)
        
        # 파일명에서 TXT 확장자와 '네이버 블로그' 부분 제거
        clean_filename = filename.replace(".txt", "").replace("  네이버 블로그", "")
        
        # 게임 ID 생성 (한글, 영문, 숫자만 남기고 공백을 _로 대체)
        # 특수문자 제거 후 공백을 _로 변환
        game_id = re.sub(r'[^\w가-힣\s]', '', game_name).strip()
        game_id = re.sub(r'\s+', '_', game_id)
        
        # 중복된 ID가 있는지 확인
        existing_ids = [item["id"] for item in json_data]
        if game_id in existing_ids:
            # 중복된 ID가 있으면 번호 추가
            count = 1
            while f"{game_id}_{count}" in existing_ids:
                count += 1
            game_id = f"{game_id}_{count}"
        
        # JSON 객체 생성
        game_obj = {
            "id": game_id,
            "game_name": game_name,
            "section": "RULES",
            "text": clean_content,
            "players": players
        }
        
        # 리스트에 추가
        json_data.append(game_obj)

# JSON 파일로 저장
output_path = "/Users/hwangjunho/Desktop/boardgame_rules_final.json"
with open(output_path, 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f"변환 완료: {len(json_data)}개의 파일이 {output_path}에 저장되었습니다.")
