from doc import *
from os import *
from sys import *
import time

print(argv)

test = Doc(argv[1])
for k in test.getVar():
    elt = test.getVar()[k]
    if(elt["type"] == "string"):
        print(k + "?")
        v = raw_input()
        test.setVar(k, v)
    if(elt["type"] == "choice"):
        for i in range(len(elt["choices"])):
            print(str(i) + " : " + elt["choices"][i])
        v = raw_input("?")
        test.setVar(k, v)
print(test.getVar())

test.applyVar(argv[1] + "-" + str(int(time.time())))
system("pdflatex -interaction=nonstopmode " + argv[1] + "/"+ argv[1] + "-" + str(int(time.time())) +".tex")
