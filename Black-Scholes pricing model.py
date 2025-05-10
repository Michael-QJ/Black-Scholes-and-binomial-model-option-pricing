import math

def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("The value you entered is invalid. Please enter a non-negative number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

s0 = get_non_negative_float("Enter the current stock price: ")
x = get_non_negative_float("Enter desired strike price: ")
r = get_non_negative_float("Enter risk free interest rate: ")
T = get_non_negative_float("Enter maturity: ")

while True:
    pricing_model = input ("Black-Scholes model or binomial model? ").lower()
    if pricing_model == "black-scholes model":
        sigma = float(input("Enter volatility: "))
        while True:
            dividend = input("Does the stock pay dividend? ").lower()
            if dividend == "yes":
                dividend_r = float(input("What's the rate of dividend? "))
                break
            elif dividend == "no":
                dividend_r = 0
                break
            else:
                print("Invalid, please try again.")
        break
    elif pricing_model == "binomial model":
        s1_u = float(input("Enter stock price at T=1 if it goes up: "))
        s1_d = float(input("Enter stock price at T=1 if it goes down: "))
        break
    else:
        print("Invalid choice, please try again.")

while True:
    option = input("Is it a call or put? ").lower()
    if option == "call":
        break
    elif option == "put":
        break
    else:
        print("Invalid choice, please try again.")

def binomial(s0, x, r, T, s1_d, s1_u, option):
    if option == "call":
        c1_u = max(s1_u-x, 0)
        c1_d = max(s1_d-x, 0)
        delta = (c1_u-c1_d)/(s1_u-s1_d)
        wb = c1_u - delta*s1_u
        price = delta * s0 + math.e ** (-r * T) * wb
        return price
    elif option == "put":
        p1_u = max(x-s1_u, 0)
        p1_d = max(x-s1_d, 0)
        delta = (p1_u-p1_d)/(s1_u-s1_d)
        wb = p1_d-delta*s1_d
        price = delta * s0 + math.e ** (-r*T) * wb
        return price

import numpy as np
from scipy.stats import norm

def black_scholes(s0, x, r, T, sigma, option, dividend_r):
    d1 = (np.log(s0/x) + (r - dividend_r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option == "call":
        call_price = s0 * np.exp(-dividend_r * T) * norm.cdf(d1) - x * np.exp(-r * T) * norm.cdf(d2)
        return call_price
    elif option == "put":
        put_price = x * np.exp(-r * T) * norm.cdf(-d2) - s0 * np.exp(-dividend_r * T) * norm.cdf(-d1)
        return put_price

if pricing_model == "black-scholes model":
    result = black_scholes(s0, x, r, T, sigma, option, dividend_r)
elif pricing_model == "binomial model":
    result = binomial(s0, x, r, T, s1_d, s1_u, option)

print(f"You used {pricing_model} to calculate the price of a {option} option, the result is {result:.2f}")





