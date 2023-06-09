import pandas as pd
import numpy as np
import warnings; warnings.filterwarnings('ignore')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from cachetools import LRUCache
import os
dir, file = os.path.split(os.path.abspath(__file__))

# movies = data  # JSON 데이터에서 영화 리스트 추출
# movie_data = []

# csv 생성
# for movie in movies:
#     movie_id = movie['pk']
#     title = movie['fields']['title']
#     release_date = movie['fields']['release_date']
#     popularity = movie['fields']['popularity']
#     score_average = movie['fields']['score_average']
#     overview = movie['fields']['overview']
#     poster_path = movie['fields']['poster_path']
#     genres = ', '.join(str(genre) for genre in movie['fields']['genres'])
#     director = movie['fields']['director']
#     actors = ', '.join(actor for actor in movie['fields']['actors'])
    
#     movie_data.append([movie_id, title, release_date, popularity, score_average, overview, poster_path, genres, director, actors])

# columns = ['movie_id', 'title', 'release_date', 'popularity', 'score_average', 'overview', 'poster_path', 'genres', 'director', 'actors']
# df = pd.DataFrame(movie_data, columns=columns)
# df.to_csv('movies.csv',encoding='utf-8', index=False)

movies=pd.read_csv(dir + "/movies.csv")

# 주요 칼럼 추출
movies_df=movies[['movie_id', 'title', 'genres', 'release_date', 'score_average', 'popularity', 'actors', 'director']]
movies_df.head(8)

# genre, actors, director, title기반으로 코사인 유사도 계산
movies_df['features'] = movies_df['genres'] + ' ' + movies_df['actors'] + ' ' + movies_df['title'] +  ' ' + movies_df['director']
movies_df['features'] = movies_df['features'].fillna('')  # NaN 값을 빈 문자열로 대체
count_vect = CountVectorizer(min_df=0, ngram_range=(1, 2))
features_mat = count_vect.fit_transform(movies_df['features'])
# print(features_mat.shape)

# 피처 백터화한 행렬로 계산
features_sim = cosine_similarity(features_mat, features_mat)
# print(features_sim.shape)

# 유사도 높은 순 정렬
features_sim_sorted_ind = features_sim.argsort()[:, ::-1]
print(features_sim_sorted_ind[:1])

# features_sim 열 추가
movies_df['features_sim'] = features_sim_sorted_ind.tolist()

# 캐시 생성
movie_cache = LRUCache(maxsize=128)

def find_sim_movies(movies_df, sorted_ind, movie_ids, top_n=10):
    similar_movies = []
    similar_indexes = []
    movie_index = []

    # 캐시 키
    movie_cache_key = f"movie_recommendation:{movie_ids}"

    # 추천영화 조회
    cached_movielist = movie_cache.get(movie_cache_key)
    # 해당 영화조합에 대한 추천 영화가 캐시에 있는 경우 그대로 반환
    if cached_movielist is not None:
        print('캐시', movie_cache[movie_cache_key])
        return movie_cache[movie_cache_key]
    
    for movie_id in movie_ids:
        # movie_id에 해당하는 인덱스 추출
        movie_index.append(movies_df[movies_df['movie_id'] == movie_id].index.values)
        # top_n에 해당하는 유사성이 높은 인덱스 추출
        similar_indexes.append(sorted_ind[movie_index, :(top_n)].flatten())
        print(f'5{similar_indexes}')

    # 비어있는 배열일 경우 바로 반환
    if not similar_indexes:
        return similar_movies
    
    # 유사한 영화 인덱스들을 병합
    similar_indexes = np.concatenate(similar_indexes)
    # # reshape(-1) 1차원 배열로 변환
    # similar_indexes = similar_indexes.reshape(-1)

    # 기준 영화 인덱스들을 제외하고 유사한 영화 인덱스 추출
    similar_indexes = np.setdiff1d(similar_indexes, movie_index)

    # 코사인 유사도를 기준으로 유사한 영화들을 정렬하여 similar_movies에 추가
    similar_movies = movies_df.iloc[similar_indexes].sort_values(by='features_sim', ascending=False)['movie_id'].tolist()
    # 캐시 저장
    movie_cache[movie_cache_key] = similar_movies
    print('캐시 값', movie_cache[movie_cache_key])


    return similar_movies


