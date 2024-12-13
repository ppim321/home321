# 설정 정보만 저장하는 파일.
# 프로그램에서 사용하는 고정 값들
# split 설정
chunk_size = 1000
chunk_overlap = 0

# model 설정
embedding_name = 'text-embedding-3-small'
model_name = 'gpt-4o-mini'

# Chroma DB 설정
collection_name = "korean_novel"
persist_directory = "vector_store/korean_novel_db"

