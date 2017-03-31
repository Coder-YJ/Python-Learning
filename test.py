# -*- coding: utf-8 -*-
def calculate(number):
    sum = 0
	n = 1
    while n < number:
        sum = sum + n*n
		n = n + 1
    return sum