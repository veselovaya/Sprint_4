import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверяем, что объекту присвоен пустой словарь
    def test_book_genre_is_empty(self):
        collector = BooksCollector()
        assert collector.books_genre == {}

    # проверяем, что объекту присвоен пустой список
    def test_favorites_list_is_epmty(self):
        collector = BooksCollector()
        assert collector.favorites == []

    # проверяем, что объекту присвоен нужный список жанров
    def test_genre_list_true(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    # проверяем, что объекту присвоен нужный список жанров с ограничением по возрасту
    def test_genre_age_rating_list_true(self):
        collector = BooksCollector()
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # проверяем, что в словарь books_genre добавляются книги с валидным  кол-вом символов в названии
    @pytest.mark.parametrize('name', ['П', 'Die Hard'])
    def test_add_new_book_one_and_forty_symbols_added(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.books_genre

    # проверяем, что в словарь не добавляются книги, с невалидной длиной названия

    @pytest.mark.parametrize('name', ['', 'В поисках утраченного времени: Путь героя'])
    def test_add_new_book_zero_forty_one_symbols_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.books_genre

    # проверяем, что в словарь не добавляются книги, если они уже есть в в словаре

    def test_add_new_book_dublicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Avatar')
        collector.add_new_book('Avatar')
        assert len(collector.get_books_genre()) == 1

    # проверяем, что в словарь добавляется жанр
    @pytest.mark.parametrize(
        'name, genre',
         [
             ['Первому игроку приготовиться', 'Фантастика'],
             ['Мгла', 'Ужасы'],
             ['Паутина', 'Детективы'],
             ['Смешарики', 'Мультфильмы'],
             ['Пакун', 'Комедии']
         ]
    )
    def test_set_book_genre_book_genre_in_list_true(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_books_genre() == {name: genre}

    # проверяем, что в словарь не добавляется жанр, если нет книги в словаре self.books_genre
    def test_set_book_genre_no_book_in_list_no_set_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Avatar', 'Фантастика')
        assert len(collector.get_books_genre()) == 0

    # проверяем, что в словарь не добавляется жанр, если жанра нет в списке self.genre
    def test_set_book_genre_no_genre_in_list_no_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Harry Potter')
        collector.set_book_genre('Harry Potter', 'Fantasy')
        assert collector.get_books_genre()['Harry Potter'] == ''

    # проверяем, что у добавленной книги нет жанра
    def test_get_books_genre_added_book_have_no_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Avatar')
        assert collector.get_books_genre()['Avatar'] == ''

    # проверяем, что выводятся книги с определеным жанром
    def test_get_books_with_specific_genre_true(self):
        collector = BooksCollector()
        collector.add_new_book('Avatar')
        collector.add_new_book('Pakun')
        collector.set_book_genre('Avatar', 'Фантастика')
        collector.set_book_genre('Pakun', 'Комедии')
        assert 'Pakun' in collector.get_books_with_specific_genre('Комедии')

    # проверяем, что в список для детей не входят Ужасы и Детективы
    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Мгла', 'Ужасы'],
            ['Паутина', 'Детективы']
        ]
    )
    def test_get_books_for_children_age_rate_genre_not_in_list(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.set_book_genre(name, genre)
        assert len(collector.get_books_for_children()) == 0

    # проверяем, что книгу из словаря self.books_genre можно добавить в избранное
    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.add_book_in_favorites('Мгла')
        assert len(collector.get_list_of_favorites_books()) == 1

    # проверяем, что книгу, которой нет в словаре self.books_genre нельзя добавить в избранное
    def test_add_book_in_favorites_no_book_in_dict_false(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Мгла')
        assert len(collector.get_list_of_favorites_books()) == 0


    # проверяем, что книгу из избранного можно удалить
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.add_book_in_favorites('Мгла')
        collector.delete_book_from_favorites('Мгла')
        assert len(collector.get_list_of_favorites_books()) == 0




















