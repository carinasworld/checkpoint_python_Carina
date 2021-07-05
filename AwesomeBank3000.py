# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:10:03 2021

@author: Carin
"""

customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salary = [155000, 755000, 455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

for i in range(0, 6):
    print(f'Employee:{customers[i]}, salary:{salary[i]}, tax:{taxes[i]}')

for i in range(0, 6):    
    taxrate = taxes[i]/salary[i] * 100
    print(f'Employee:{customers[i]}, {taxrate}')
