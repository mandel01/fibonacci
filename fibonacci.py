#!/usr/bin/env python

"""Prints the first 500 elements in the Fibonacci sequence

Used to illustrate some concepts of Python programming
for first-grade students."""

numbers = 500
fib = [1,1]

i=2
while i < numbers:
    fib.append(fib[-2] + fib[-1])
    i += 1

for n in fib:
    print('{0:,}\n'.format(n))
