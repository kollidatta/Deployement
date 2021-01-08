# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:51:19 2020

@author: kolli
"""



from flask import Flask,render_template,url_for,request
import pandas as pd 



app = Flask(__name__)
# Python3 program to find last digit of  
# nth Fibonacci number 
  
# Function that returns nth Fibonacci number  
def fib(n): 
  
    F = [[1, 1], [1, 0]]; 
    if (n == 0): 
        return 0; 
    power(F, n - 1); 
  
    return F[0][0]; 
  
# Utility function to multiply two 
# matrices and store result in first. 
def multiply(F, M): 
  
    x = F[0][0] * M[0][0] + F[0][1] * M[1][0]; 
    y = F[0][0] * M[0][1] + F[0][1] * M[1][1]; 
    z = F[1][0] * M[0][0] + F[1][1] * M[1][0]; 
    w = F[1][0] * M[0][1] + F[1][1] * M[1][1]; 
  
    F[0][0] = x; 
    F[0][1] = y; 
    F[1][0] = z; 
    F[1][1] = w; 
  
# Optimized version of power() in  
# method 4  
def power(F, n): 
  
    if( n == 0 or n == 1): 
        return; 
    M = [[1, 1], [1, 0]]; 
  
    power(F, int(n / 2)); 
    multiply(F, F); 
  
    if (n % 2 != 0): 
        multiply(F, M); 
  
# Returns last digit of  
# n'th Fibonacci Number 
def findLastDigit(n): 
  
    return (fib(n) % 10); 
  
# Driver code 
n = 10; 
print(findLastDigit(n)); 
# n = 61; 
# print(findLastDigit(n)); 
# n = 7; 
# print(findLastDigit(n)); 
# n = 67; 
# print(findLastDigit(n)); 
  

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        data = int(request.form['message'])
        data = findLastDigit(data)
        
    return render_template('result.html',output = data)


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=4000)




