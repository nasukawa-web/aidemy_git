#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def main():

<<<<<<< HEAD
print("今日の一句" + wakas[random.randrange(len(wakas))])
=======
    with open("./hyakunin.txt", encoding="utf-8") as f:
        wakas = [s.strip() for s in f.readlines()]
        print("今日の一句" + wakas[random.randrange(len(wakas))])

if __name__ == '__main__':
    main()
>>>>>>> add_main
