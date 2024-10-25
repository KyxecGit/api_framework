from services.movies.helpers.genre_helper import GenreHelper
from services.movies.helpers.movies_helper import MovieHelper
from services.movies.helpers.review_helper import ReviewHelper
from services.movies.models.genre_model.create_genre import CreateGenre
from services.movies.models.movie_model.create_movie import CreateMovie
from services.movies.models.genre_model.genre_response import GenreResponse, GenreListResponse
from services.movies.models.movie_model.movie_response import MovieResponse
from services.movies.models.review_model.movie_review import MovieReview
from services.movies.models.review_model.movie_review_response import MovieReviewResponse
from utils.config import UrlConfig


class MoviesService:
    """Сервис для работы с фильмами, жанрами и отзывами."""

    def __init__(self, url: UrlConfig):
        """Инициализация сервиса с URL конфигурацией."""
        self.url = url
        self.genre_helper = GenreHelper(self.url)  # Помощник для работы с жанрами
        self.movies_helper = MovieHelper(self.url)  # Помощник для работы с фильмами
        self.review_helper = ReviewHelper(self.url)  # Помощник для работы с отзывами

    def post_genre(self, create_genre: CreateGenre) -> GenreResponse:
        """Создает новый жанр."""
        response = self.genre_helper.post_genre(json=create_genre.model_dump(by_alias=True, exclude_defaults=True))
        return GenreResponse(**response.json())

    def get_genres(self) -> GenreListResponse:
        """Получает список всех жанров."""
        response = self.genre_helper.get_genres()
        return GenreListResponse(genres=response.json())

    def post_movie(self, create_movie: CreateMovie) -> MovieResponse:
        """Создает новый фильм."""
        response = self.movies_helper.post_movie(json=create_movie.model_dump(by_alias=True, exclude_defaults=True))
        return MovieResponse(**response.json())

    def post_movie_review(self, movie_id: int, movie_review: MovieReview) -> MovieReviewResponse:
        """Добавляет отзыв на фильм."""
        response = self.review_helper.post_movie_review(movie_id=movie_id, json=movie_review.model_dump(by_alias=True, exclude_defaults=True))
        return MovieReviewResponse(**response.json())

    def patch_movie_review(self, movie_id: int, user_id: str) -> MovieReviewResponse:
        """Обновляет отзыв на фильм."""
        response = self.review_helper.patch_movie_review(movie_id=movie_id, user_id=user_id)
        return MovieReviewResponse(**response.json())

    def delete_review(self, movie_id: int) -> MovieReviewResponse:
        """Удаляет отзыв на фильм."""
        response = self.review_helper.delete_review(movie_id=movie_id)
        return MovieReviewResponse(**response.json())
