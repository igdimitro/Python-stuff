# -*- coding: utf-8 -*-
import re

# Задача 5:
# В подаден текст, всички суми в евро или долари(€, EUR, $, USD) да се приведат
# в лева по подадени курсове. След преобразуването да се изведат всички суми
# над 1000лв.
# Вход: Низ, коефициент за преобразуване от евро в лева и коефициент за
# преобразуване от долари в лева.
# Изход (на екран): Поредица от сумите над 1000лв.

test = 'dog, 200 EUR money  obsession $13.22 lock actor 4251 €  misshapen €123.12 details factory 20 USD ,USD 52 eating martini EUR 1240 building cords parallel 450.12$.'
dollars_pattern = r'USD\s?\d+[[\.,]?\d+]?|\s\d+[\.,]?\d+\s?USD|\$\s?\d+[[\.,]?\d+]?|\s\d+[\.,]?\d+\s?\$'
euros_pattern = r'EUR\s?\d+[[\.,]?\d+]?|\s\d+[\.,]?\d+\s?EUR|€\s?\d+[[\.,]?\d+]?|\s\d+[\.,]?\d+\s?€'


def foo(data, rating_euro_bgn, rating_usd_bgn):
    dollars = []
    euros = []
    bgn = []
    for money in re.findall(dollars_pattern, data, re.UNICODE):
        dollars.append(
            float(re.findall(r'\s?\d+[[\.,]?\d+]?', money, re.UNICODE)[0]))
    bgn = [x * rating_usd_bgn for x in dollars]
    for money in re.findall(euros_pattern, data, re.UNICODE):
        euros.append(
            float(re.findall(r'\s?\d+[[\.,]?\d+]?', money, re.UNICODE)[0]))
    bgn.extend([x * rating_euro_bgn for x in euros])
    return list(filter(lambda x: x >= 1000, bgn))


if __name__ == "__main__":
    print(foo(test, 1.95, 1.82))
