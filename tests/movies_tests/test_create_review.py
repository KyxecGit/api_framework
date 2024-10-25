import random
from faker import Faker
from utils.logger import Logger
from services.movies.models.genre_model.create_genre import CreateGenre
from services.movies.models.review_model.movie_review import MovieReview

# Инициализация Faker для генерации тестовых данных
faker = Faker()


class TestCreateReview:
    def test_create_genre_for_movie_and_make_review(self, movie_api_service, create_new_movie):
        """
        Тест на создание нового жанра для фильма и написание рецензии.
        """

        Logger.info(" !!! Step 1 - Create a new genre")
        # Создаем новый жанр
        genre = CreateGenre(name=faker.name())
        created_genre = movie_api_service.post_genre(genre)

        Logger.info(" !!! Step 2 - Create a new movie")
        # Создаем новый фильм с созданным жанром
        created_movie = create_new_movie(created_genre.id)

        Logger.info(" !!! Step 3 - Make a review")
        # Генерируем случайную рецензию на фильм
        movie_review = MovieReview(rating=random.randint(1, 5), text=faker.pystr())
        post_movie_review = movie_api_service.post_movie_review(movie_id=created_movie.id,
                                                                movie_review=movie_review)

        Logger.info(" !!! Step 4 - Check movie review")
        # Проверяем, что рецензия была правильно добавлена
        movie_review = movie_api_service.patch_movie_review(user_id=post_movie_review.user_id,
                                                            movie_id=created_movie.id)

        assert movie_review.text == post_movie_review.text, \
            f"Expected review text {post_movie_review.text} got {movie_review.text} instead"

        assert movie_review.rating == post_movie_review.rating, \
            f"Expected review rating: {post_movie_review.rating} got: {movie_review.rating} instead"

    def test_choose_genre_for_movie_and_make_review(self, movie_api_service, create_new_movie):
        """
        Тест на выбор жанра для фильма и написание рецензии.
        """

        Logger.info(" !!! Step 1 - Create a new movie")
        # Создаем новый фильм
        created_movie = create_new_movie()

        Logger.info(" !!! Step 2 - Make a review")
        # Генерируем случайную рецензию на фильм
        movie_review = MovieReview(rating=random.randint(1, 5), text=faker.pystr())
        post_movie_review = movie_api_service.post_movie_review(movie_id=created_movie.id,
                                                                movie_review=movie_review)

        Logger.info(" !!! Step 3 - Check a movie review")
        # Проверяем, что рецензия была правильно добавлена
        assert movie_review.text == post_movie_review.text, \
            f"Expected review text {post_movie_review.text} got {movie_review.text} instead"

        assert movie_review.rating == post_movie_review.rating, \
            f"Expected review rating: {post_movie_review.rating} got: {movie_review.rating} instead"
