"""Faça um programa que leia algo pelo teclado e mostre na 
tela o seu tipo primitivo e todas as informações possiveis sobre ele"""

a = input('Digite algo: ')
print('o tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanúmerico?', a.isalnum())
print('Está em maiusculas?', a.isupper())
print('Está em minusculas?', a.islower())
print('Está capitalizada?', a.istitle())
