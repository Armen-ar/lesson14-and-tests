# * выводит все столбцы запрос:
# SELECT DISTINCT получает значения без повторов уникальные
# SELECT вместо * (всё) конкретно те столбцы, которые хотим видеть
# director (режисёр), duration (продолжительность), title (название), country (страны)
# WHERE (где) значение число, то просто число
# если строка в ковычках одинарных названия строки '',
# а двойные ковычки "" названия столбцов
# можно и писать director == 'Cristina Jacob'
# отрицание director != 'Cristina Jacob'
# может быть > < значение число
# и дополнительное условие AND duration > 110 (продолжительность больше 110 мин.)
# если условие вывода задаём WHERE country = 'Argentina' OR (или) country = 'Armenia'
# или можно WHERE country IN (Argentina, Armenia, .....) если нужно перечислять много стран
# WHERE country LIKE (похожая) 'A%' (% знак после буквы значит страны, которые начинаются с А)
# '%A' в конце слова и '%A%' в середине слова
# WHERE "cast" (играет) LIKE '%Maria%'
# cast это зарезервированное слово, поэтому нужно писать в двойных ковычках или с название файла netflix.cast
# release_year > 2000 все фильмы производство после 2000 года
# можно писать интервал так: release_year < 1950(не включительно) AND release_year > 1945(не включительно)
# но можно писать BETWEEN совпадение в числах между 1945 AND 1950 (включительны обе границы)
# AND director IS NOT NULL означает эта строка не заполнена вообще
# ORDER BY release_year DESC  сортировка от большего к меньшему
# ГРУППИРОВКА ставится в конце, т.е. на полученном результате
# ORDER BY release_year ASC  сортировка от меньшего к большему (применяется по умолчанию)
# GROUP BY type, country группировка по типу
# __________________________________________________________________________________________
# GROUP BY - это ключевое слово для агрегирующих функций
# COUNT - функция агрегации строк, которая считает и возвращает количество записей в группе
# SUM - функция, которая считает сумму всех значений из столбца в группе
# AVG - функция, которая считает среднее арифметическое значения столбца в группе
# MIN - функция, которая определяет минимальное значение в столбце группы
# MAX - функция, которая определяет максимальное значение в столбце группы
# HAVING - это условие после группировки

"""
Агрегирующие функции

COUNT()
DISTINCT
SUM()
AVG()
MIN()
MAX()
"""

import sqlite3

with sqlite3.connect("part1/netflix.db") as connection:

    cursor = connection.cursor()
    query_1 = """
        SELECT COUNT()
        FROM netflix
     """
    query_2 = """
        SELECT COUNT(*)
        FROM netflix
        GROUP BY director
    """    # COUNT(*) количество строчек, только по столбцу director
    query_3 = """
        SELECT COUNT(DISTINCT director)
        FROM netflix
    """    # COUNT(DISTINCT, director) количество строчек, только по столбцу director уникальные(без повторов)
    query_4 = """
        SELECT COUNT(*), country
        FROM netflix
        WHERE country != ''
        GROUP BY country
    """    # COUNT(*) количество строчек, только по столбцу country
    query_5 = """
        SELECT MIN(release_year), MAX(release_year)
        FROM netflix
    """
    query_6 = """
        SELECT type, country, AVG(duration)
        FROM netflix
        GROUP BY type, country
    """  # средняя продолжительность фильмов в минутах, сериалов в сезонах и сгруппированные по странам
    query_7 = """
        SELECT country, SUM(duration)
        FROM netflix
        WHERE type = 'TV Show'
        GROUP BY country
        ORDER BY SUM(duration)
        LIMIT 10
    """  # количество сезонов в сериалах по всем странам (вывод по 10 строк), сортированная от меньшего по умолчанию
    query_8 = """
        SELECT country, SUM(duration) AS total_duration
        FROM netflix
        WHERE type = 'TV Show'
        AND country != ''
        GROUP BY country
        ORDER BY total_duration DESC
        LIMIT 10
    """  # количество сезонов в сериалах по всем странам (вывод по 10 строк), сортированная от большего,
         # но с псевдонимом SUM(duration) перезаписывает в total_duration

    cursor.execute(query_2)

    for row in cursor.fetchall():
        print(row)
