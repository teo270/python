#! /usr/bin/python3

import json, yaml
import pickle as pkl
import numpy as np
import matplotlib.pylab as plt

import time

def sestej(a):
    b = 2*a
    return b

def odstej(a):
    return a-a


def main():
    global zgdovina


    print("hello world")

    while True:
        vhod = input("izberite opcijo:\na")
        stevilka = input("izberi stevilko")
        rezultat ={"stevilka":stevilka}


        if vhod == "sestevanje":
            print(f"rezultat:{sestej(stevilka)}")

        elif vhod == "odstevanje":
            print(f"rezultat:{odstej(stevilka)}")

        elif vhod == "q":
            with open("../log.txt", "w") as f:
                f.writelines(yaml.dump(zgodovina))

        else:
            break
        


if __name__ == "__main__":
    main()

