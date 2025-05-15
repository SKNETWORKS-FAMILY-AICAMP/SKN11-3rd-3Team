import json
import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer

# ✅ 데이터 로딩
with open("chunked_game_rules.json", "r", encoding="utf-8") as f:
    game_data = json.load(f)

# ✅ 임베딩 모델 로딩
embed_model = SentenceTransformer("BAAI/bge-m3", device="cuda")

# ✅ 저장할 루트 디렉토리 생성
os.makedirs("game_data", exist_ok=True)

# ✅ 각 게임별로 JSON + FAISS 저장
for game_name, info in game_data.items():
    chunks = info["chunks"]

    # 디렉토리 안전한 이름으로 파일명 변환 (공백, 특수문자 제거 등)
    safe_name = game_name.replace(" ", "_").replace("/", "_")

    # 파일 경로 설정
    json_path = os.path.join("game_data", f"{safe_name}.json")
    faiss_path = os.path.join("game_data", f"{safe_name}.faiss")

    # ✅ JSON 저장
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)

    # ✅ 벡터 임베딩 및 FAISS 저장
    embeddings = embed_model.encode(chunks, normalize_embeddings=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatIP(dim)
    index.add(np.array(embeddings))
    faiss.write_index(index, faiss_path)

    print(f"✅ 저장 완료: {game_name} → {safe_name}.json / {safe_name}.faiss")
