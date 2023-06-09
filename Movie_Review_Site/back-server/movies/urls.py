from . import views
from django.urls import path

app_name = 'movies'
urlpatterns = [
    path('', views.movie_list), # 메인 영화 조회
    path('<int:movie_id>/', views.movie_detail), # 영화 상세 조회
    path('<int:movie_id>/reviews/', views.movie_review), # 영화별 리뷰 조회
    path('search/', views.movie_search), # 검색
    #http://127.0.0.1:8000/movies/search/?title=앤트맨&year=2018 (검색 예시)
    path('search/autocomplete/', views.movie_autocomplete),
    # http://127.0.0.1:8000/movies/search/autocomplete/?word=앤 (예시)
    path('<int:movie_id>/like/', views.movie_like), # 리뷰 좋아요
    path('<int:movie_id>/wishlist/', views.movie_wishlist), # 위시리스트 추가
    path('recommend/<str:username>/', views.movie_recommendation), # 위시리스트 기반 영화 추천
    path('recommend/', views.tfidf_recommend), # 입력 텍스트 기반 영화 추천
    # http://127.0.0.1:8000/movies/recommend/?keyword=키워드 
]
