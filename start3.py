#!/usr/bin/env python3
import math
from datetime import date

D = {'A': 100, 'B': 200, 'C': 150}

asoiaf_books = [
    {'title': 'Game of Thrones', 'published': '1996-08-01', 'pages': 694},
    {'title': 'Clash of Kings', 'published': '1998-11-16', 'pages': 761},
    {'title': 'Storm of Swords', 'published': '2000-08-08', 'pages': 973},
    {'title': 'Feast for Crows', 'published': '2005-10-17', 'pages': 753},
    {'title': 'Dance with Dragons', 'published': '2011-07-12', 'pages': 1016}
]

fn = lambda k, b: D.get(k) + b  # доступ по ключу к элементу и добавление заданного числа
print(fn('A', 50))
print((lambda k, b: D.get(k) + b)('B', 60))  # understand lambda as function, function(parameters)

# example from https://habr.com/ru/post/507642/
todays_weekday = date.today().weekday()


def sum(a, b):
    if todays_weekday == 1:
        result = a + b
        print(f'sum is {result} and result class is {type(result)}')
    else:
        result = str(a + b)
        print(f'sum is {result} and result class is {type(result)}')


todays_weekday = 1
sum(4, 5)
todays_weekday = 4
sum(4, 5)

pi_const = round(math.pi, 2)
print((lambda radius: pi_const * (radius ** 2))(5))
print((lambda radius: pi_const * (radius ** 2))(12))
print((lambda radius: pi_const * (radius ** 2))(26))


# ******************
def get_title(book):
    return book.get('title')


def get_publish_date(book):
    return book.get('published')


# Функция по получению количества страниц в книге
def get_pages(book):
    return book.get('pages')


# Сортируем по названию
asoiaf_books.sort(key=get_title)
for book in asoiaf_books:
    print(book)
print('-------------')
# Сортируем по датам
asoiaf_books.sort(key=get_publish_date)
for book in asoiaf_books:
    print(book)
print('-------------')
# Сортируем по количеству страниц
asoiaf_books.sort(key=get_pages)
for book in asoiaf_books:
    print(book)
# using lambda
print('==================')
# Сортируем по названию
for book in sorted(asoiaf_books, key=lambda book: book.get('title')):
    print(book)

print('-------------')

# Сортируем по датам
for book in sorted(asoiaf_books, key=lambda book: book.get('published')):
    print(book)

print('-------------')

# Сортируем по количеству страниц
for book in sorted(asoiaf_books, key=lambda book: book.get('pages')):
    print(book)
