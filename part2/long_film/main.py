# Самый длинный фильм
# Теперь нам нужно узнать, какой самый длинный
# фильм среди тех, которые были сняты в 2019 году.
# Выводим название и его длительность.
#
# Пример результата:
# 100 Meters — 200 минут
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = """
        SELECT title, MAX(duration) AS max_duration
        FROM netflix
        GROUP BY release_year
        HAVING release_year = 2019
    """
cur.execute(sqlite_query)
executed_query = cur.fetchall()[0]

# для последующей выдачи в требуемом формате

result = f"{executed_query[0]} — {executed_query[1]} минут"

if __name__ == '__main__':
    print(result)
