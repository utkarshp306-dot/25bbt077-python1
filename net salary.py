# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 13:13:28 2026

@author: Admin
"""

def netsalary():
    a=float(input("enter gross salary:"))
    b=(10*a)/100
    c=(3*a)/100
    d=a+b-c
    print('net salary:',d)
    
netsalary()