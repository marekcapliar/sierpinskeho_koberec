import math

date = input("Write date in format dd.mm.yyyy: ")

q, m, year = date.split('.')
q = int(q)
if int(m) < 3:
    m = int(m) + 12
    year = int(year) - 1
else:
    m = int(m)
    year = int(year)

K = year%100
J = math.floor(year/100)
day = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

h = (q + math.floor((13 * (m+1))/5) + K + math.floor(K/4) + math.floor(J/4) - 2*J) % 7
print("Day is " + day[h])