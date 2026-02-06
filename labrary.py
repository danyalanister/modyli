class LibraryItem:
    """Базовый класс для всех материалов библиотеки."""
    _next_id = 1

    def __init__(self, title: str, author: str, year: int):
        self._title = title
        self._author = author
        self._year = year
        self.__item_id = LibraryItem._next_id
        LibraryItem._next_id += 1
        self.__is_checked_out = False

    # Геттеры
    def get_title(self) -> str:
        return self._title

    def get_author(self) -> str:
        return self._author

    def get_year(self) -> int:
        return self._year

    def get_item_id(self) -> int:
        return self.__item_id

    def get_is_checked_out(self) -> bool:
        return self.__is_checked_out

    # Сеттер для __is_checked_out
    def set_is_checked_out(self, value: bool):
        if isinstance(value, bool):
            self.__is_checked_out = value
        else:
            raise ValueError("Значение должно быть True или False")

    def __str__(self):
        return f"{self.get_item_id()}: {self.get_title()} ({self.get_year()})"


class Book(LibraryItem):
    """Класс для книг."""
    def __init__(self, title: str, author: str, year: int, genre: str, page_count: int):
        super().__init__(title, author, year)
        self.genre = genre
        self.set_page_count(page_count)  # Используем сеттер для валидации

    # Геттер и сеттер для __page_count
    def get_page_count(self) -> int:
        return self.__page_count

    def set_page_count(self, value: int):
        if value < 1:
            raise ValueError("Количество страниц не может быть меньше 1")
        self.__page_count = value

    def __str__(self):
        return f"Книга: {super().__str__()}, жанр: {self.genre}, страниц: {self.get_page_count()}"


class Magazine(LibraryItem):
    """Класс для журналов."""
    def __init__(self, title: str, author: str, year: int, issue_number: int):
        super().__init__(title, author, year)
        self._issue_number = issue_number

    def get_magazine_info(self) -> str:
        return f"Журнал: {self.get_title()}, выпуск №{self._issue_number}, год: {self.get_year()}"

    def __str__(self):
        return self.get_magazine_info()


class DVD(LibraryItem):
    """Класс для DVD."""
    _valid_ratings = {"G", "PG", "PG-13", "R", "NC-17"}

    def __init__(self, title: str, author: str, year: int, duration: int, rating: str):
        super().__init__(title, author, year)
        self.set_duration(duration)
        self.set_rating(rating)

    # Геттеры и сеттеры для __duration
    def get_duration(self) -> int:
        return self.__duration

    def set_duration(self, value: int):
        if not (1 <= value <= 300):
            raise ValueError("Продолжительность должна быть от 1 до 300 минут")
        self.__duration = value

    # Геттеры и сеттеры для __rating
    def get_rating(self) -> str:
        return self.__rating

    def set_rating(self, value: str):
        if value not in DVD._valid_ratings:
            raise ValueError(f"Рейтинг должен быть одним из: {DVD._valid_ratings}")
        self.__rating = value

    def __str__(self):
        return f"DVD: {super().__str__()}, длительность: {self.get_duration()} мин., рейтинг: {self.get_rating()}"


class Library:
    """Класс для управления коллекцией материалов."""
    def __init__(self):
        self.__items = []

    def add_item(self, item: LibraryItem):
        """Добавить материал в библиотеку."""
        self.__items.append(item)
        print(f"Добавлен: {item}")

    def remove_item(self, item_id: int):
        """Удалить материал по ID."""
        for i, item in enumerate(self.__items):
            if item.get_item_id() == item_id:
                removed = self.__items.pop(i)
                print(f"Удален: {removed}")
                return
        print(f"Материал с ID {item_id} не найден.")

    def search(self, query: str):
        """Поиск материалов по названию или автору."""
        query = query.lower()
        results = []
        for item in self.__items:
            if query in item.get_title().lower() or query in item.get_author().lower():
                results.append(item)
        return results

    def get_statistics(self) -> dict:
        """Статистика по типам материалов."""
        stats = {"Книги": 0, "Журналы": 0, "DVD": 0}
        for item in self.__items:
            if isinstance(item, Book):
                stats["Книги"] += 1
            elif isinstance(item, Magazine):
                stats["Журналы"] += 1
            elif isinstance(item, DVD):
                stats["DVD"] += 1
        return stats

    def get_available_items(self):
        """Список доступных материалов (не выданных)."""
        return [item for item in self.__items if not item.get_is_checked_out()]

    def display_all(self):
        """Показать все материалы."""
        if not self.__items:
            print("Библиотека пуста.")
        for item in self.__items:
            print(item)


# Пример использования
if __name__ == "__main__":
    # Создание библиотеки
    library = Library()

    # Создание материалов
    book1 = Book("Война и мир", "Лев Толстой", 1869, "Роман", 1225)
    book2 = Book("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328)
    magazine1 = Magazine("National Geographic", "Various", 2023, 145)
    dvd1 = DVD("Интерстеллар", "Кристофер Нолан", 2014, 169, "PG-13")

    # Добавление в библиотеку
    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)
    library.add_item(dvd1)

    print("\n--- Все материалы ---")
    library.display_all()

    print("\n--- Поиск по 'оруэлл' ---")
    results = library.search("оруэлл")
    for item in results:
        print(item)

    print("\n--- Статистика ---")
    stats = library.get_statistics()
    for key, value in stats.items():
        print(f"{key}: {value}")

    print("\n--- Доступные материалы ---")
    available = library.get_available_items()
    for item in available:
        print(item)

    # Изменение статуса выдачи
    book1.set_is_checked_out(True)
    print(f"\nКнига '{book1.get_title()}' выдана: {book1.get_is_checked_out()}")

    print("\n--- Доступные материалы после выдачи ---")
    available = library.get_available_items()
    for item in available:
        print(item)

    # Удаление материала
    print("\n--- Удаление материала ---")
    library.remove_item(book2.get_item_id())

    print("\n--- Все материалы после удаления ---")
    library.display_all()