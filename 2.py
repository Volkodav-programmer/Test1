import sys
sys.stdin = open('input.txt', "r")
sys.stdout = open('output.txt', "w")
hh,mm,ss=map(int, input().split())
for i in range(5):
    if 0<=hh<24 and 0<mm<60 and 0<=ss<60:
        print('YES')
    else:
        print('NO')
    hh,mm,ss=map(int, input().split())