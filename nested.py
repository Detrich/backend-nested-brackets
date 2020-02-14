#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Detrich with help from derek barnes and jordan davidson"

import sys

# (  )
# [  ]
# {  }
# <  >
# (*  *)


def is_nested(line):
    """Validate a single input line for correct nesting"""
    matchingDict = {")": "(",
                    ">": "<",
                    "*)": "(*",
                    "]": "[",
                    "}": "{"}
    holdparen = []
    counter = 0
    while line:
        if line.startswith("(*"):
            if "*)" in holdparen:
                return counter
            token = line[:2]
        elif line.startswith("*)"):
            token = line[:2]
        else:
            token = line[0]
        counter += 1
        if token in matchingDict.values():
            holdparen.append(token)
        if token in matchingDict.keys():
            if matchingDict[token] == holdparen[-1]:
                holdparen.pop()
            else:
                return counter
        line = line[len(token):]
    if holdparen:
        return counter



def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    with open('input.txt') as f:
        with open('output.txt', 'w') as f_out:
            for line in f:
                result = is_nested(line)
                print(result)
                if result:
                    f_out.write(f'No {result}\n')
                else:
                    f_out.write('Yes\n')
    print(is_nested(sys.argv[1]))


if __name__ == '__main__':
    main(sys.argv[1:])
