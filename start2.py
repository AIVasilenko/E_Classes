#!/usr/bin/env python3
import sys
from T_Classes import TDictionary, update_dict


def main():
    print(sys.version)
    seq1 = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
    seq2 = {'k1', 'v1', 'k2', 'v2', 'k3', 'v3'}
    seq3 = {'k-3': 'v-3', 'k-2': 'v-2', 'k-1': 'v-1'}
    seq4 = {'k-3': 'val'}
    my_dict = TDictionary(seq1)
    my_dict.upd_dict()
    # update_dict(seq1)   # не получается совместить два метода: update_dict и upd_dict
    my_dict.print_dict()
    print('************')
    my_dict.upd_dict(seq3)
    my_dict.print_dict()
    print('************')
    my_dict.__init__(seq4)
    my_dict.upd_dict()
    my_dict.print_dict()


if __name__ == '__main__':
    main()
