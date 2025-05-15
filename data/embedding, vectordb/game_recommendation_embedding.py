# vectordb 생성 및 저장
import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ✅ game.json 로딩
with open("game.json", "r", encoding="utf-8") as f:
    data = json.load(f)

texts = [item["text"] for item in data]
game_names = [item["game_name"] for item in data]

# ✅ 임베딩 모델 로딩
embed_model = SentenceTransformer("BAAI/bge-m3", device="cuda")

embeddings = embed_model.encode(
    texts,
    normalize_embeddings=True,
    batch_size=8,
    show_progress_bar=True
)

# ✅ FAISS 인덱스 생성 및 저장
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)
index.add(np.array(embeddings))

# ✅ 벡터 DB 저장
faiss.write_index(index, "game_index.faiss")

# ✅ 부가 정보도 함께 저장
with open("texts.json", "w", encoding="utf-8") as f:
    json.dump(texts, f, ensure_ascii=False, indent=2)

with open("game_names.json", "w", encoding="utf-8") as f:
    json.dump(game_names, f, ensure_ascii=False, indent=2)
