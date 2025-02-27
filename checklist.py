#!/usr/bin/env python3

print('''
Python Checklist version 0.02
Pensando Panama Copyright 2025

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
''')

input("PRESS ENTER ANY KEY TO CONTINUE or CTRL+C TO QUIT")

print("Please type yes or no")

def answer():
    global p
    if p not in ("yes", "no"):
        print("Please read instructions again")
    elif p == "yes":
        print("Good JOB")
    elif p == "no":
        print("START OVER!!!")
        quit()

print("*****")
print("Did you start your function definition with def?")
p = input('> ')
answer()

print("Does your function name have only characters and _ (underscore) characters?")
p = input('> ')
answer()

print("Did you put an open parenthesis ( right after the function name?")
p = input('> ')
answer()

print("Did you put your arguments after the parenthesis ( separated by commas?")
p = input('> ')
answer()

print("Did you make each argument unique (meaning no duplicated names)?")
p = input('> ')
answer()

print("Did you put a close parenthesis and a colon ): after the arguments?")
p = input('> ')
answer()

print("Did you indent all lines of code you want in the function four spaces? No more, no less.")
p = input('> ')
answer()

print("Did you 'end' your function by going back to writing with no indent (dedenting we call it)?")
p = input('> ')
answer()

print("And when you run ('use' or 'call') a function, check these things:")
p = input('> ')
answer()

print("Did you call/use/run this function by typing its name?")
p = input('> ')
answer()

print("Did you put the ( character after the name to run it?")
p = input('> ')
answer()

print("Did you put the values you want into the parenthesis separated by commas?")
p = input('> ')
answer()

print("Did you end the function call with a ) character?")
p = input('> ')
answer()

print("*****")
print("You have finished debugging")
quit()
