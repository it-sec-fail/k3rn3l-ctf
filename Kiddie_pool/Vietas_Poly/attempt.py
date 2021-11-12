#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *

context.log_level = 'debug' #will print all input and output for debugging purposes
r = remote('ctf.k3rn3l4rmy.com',2236)

def get_input(): #function to get one line from the netcat
    input = r.recvline().strip().decode()
    return input

def parse(polynomial):
    '''
    TODO: Parse polynomial
    For example, parse("x^3 + 2x^2 - x + 1") should return [1,2,-1,1]
    '''

for _ in range(4): get_input() #ignore challenge flavortext

for i in range(100):
    type = get_input()
    coeffs = parse(get_input())
    print(coeffs)
    ans = -1
    if 'sum of the roots' in type:
        ans = -1
        #TODO: Find answer
    elif 'sum of the reciprocals of the roots' in type:
        ans = -1
        #TODO: Find answer
    elif 'sum of the squares of the roots' in type:
        ans = -1
        #TODO: Find answer
    r.sendline(str(ans)) #send answer to server
    get_input()

r.interactive() #should print flag if you got everything right