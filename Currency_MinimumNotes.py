""" In a currency system the only available availabe notes are of
    Rs.500, Rs.100, Rs.50, Rs.20, Rs.5 and Rs.1. Mr.X has to pay 
    amount 'm' to a shopkeeper. Write a code in Python to find the
    minimum number of notes to make amount 'm'.

    Sample Input:                     Sample Output:
      Amount to pay: 1283               Minimum number of notes: 11
"""

m = int(input("Amount to pay: "))
n = 0

if m//500>0:
  n = m//500 + n
  m = m % 500
if m//100>0:
  n = m//100 + n
  m = m % 100
if m//50>0:
  n = m//50 + n
  m = m % 50
if m//20>0:
  n = m//20 + n
  m = m % 20
if m//5>0:
  n = m//5 + n
  m = m % 5
if m//1>0:
  n = m//1 + n
  m = m % 1
  
print("Minimum number of notes:",n)