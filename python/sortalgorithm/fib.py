#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Fib:

    """
    黄金分割数列
    """

    def __init__(self):
        pass

    def fib(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib(n-1) + self.fib(n-2)


if __name__ == '__main__':
    print(Fib().fib(10))
