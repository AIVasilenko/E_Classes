#!/usr/bin/env python3
import sys
from E_File import FlConfig, Parallel


def mk_incr(n):
    return lambda x, inc=n: x + inc


def main():
    print(sys.version)
    cnf = FlConfig('config')
    cnf.read_config()
    cnf.get_config()
    # seq1 = ['a', 'b', 'c', 'd', 'e']
    # seq2 = ['1', '2', '3', '5', '7']
    # seq3 = ['8', '7', '6', '5', '4']
    # pp = Parallel(seq1, seq2, seq3)
    # # for x, y, z in Parallel(seq1, seq2, seq3):
    # for x, y, z in pp:
    #     print(x, y, z)
    # print(pp[3])


if __name__ == '__main__':
    main()
