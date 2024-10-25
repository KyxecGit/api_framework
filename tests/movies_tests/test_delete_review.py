import random
import requests.status_codes
from faker import Faker

from utils.logger import Logger
from services.movies.helpers.review_helper import ReviewHelper
from services.movies.models.review_model.movie_review import MovieReview

# Инициализация Faker для генерации тестовых данных
faker = Faker()


class TestDeleteReview:
    def test_create_movie_make_delete_review(self, movie_api_service, movie_api_utilities, create_new_movie):
        """
        Тест на создание фильма, написание рецензии и последующее её удаление.
        """
        
        Logger.info(" !!! Step 1 - Create a new movie")
        # Создаем новый фильм
        created_movie = create_new_movie()

        Logger.info(" !!! Step 2 - Make a review")
        # Генерируем случайную рецензию на фильм
        movie_review = MovieReview(rating=random.randint(1, 5), text=faker.pystr())
        post_movie_review = movie_api_service.post_movie_review(movie_id=created_movie.id,
                                                                movie_review=movie_review)

        Logger.info(" !!! Step 3 - Delete a movie review")
        # Удаляем рецензию на фильм
        movie_api_service.delete_review(created_movie.id)

        #review_helper = ReviewHelper(movie_api_utilities)
        # Пытаемся получить удалённую рецензию, ожидаем ошибку 404
        #response = review_helper.patch_movie_review(movie_id=created_movie.id, user_id=post_movie_review.user_id)

        # Проверяем, что статус код соответствует ожидаемому
        #actual_status_code = response.status_code
        #expected_status_code = requests.status_codes.codes.not_found

        #assert actual_status_code == expected_status_code, \
            #f"Expected status code: {expected_status_code}, got instead status code: {actual_status_code}"
