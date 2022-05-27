# #Самый свежий фильм
# Давайте узнаем, какой фильм или сериал был добавлен в базу самым последним.
#
# Пример результата:
# 100 Meters
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
        SELECT title, MAX(date_added), type 
        FROM netflix
    """
cur.execute(sqlite_query)
executed_query = cur.fetchall()[0][0]

# для последующей выдачи в требуемом формате

result = f"{executed_query}"

if __name__ == '__main__':
    print(result)
