#coding: utf8

def Print_f():
    print("печатает")

def My_Print(func):
    func()

if __name__ == "__main__":
    My_Print(Print_f)