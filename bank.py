p = float(input("ENTER PRINCIPAL AMOUNT: "))
r = float(input("ENTER ANNUAL INTEREST RATE: "))
n = int(input("ENTER NUMBER OF TIMES COMPOUNDED PER YEAR: "))
t = float(input("ENTER YEARS: "))

investment = p * ((100+r)/100) ** (n * t)
interest = investment - p

print("Total investment =", investment)
print("Total interest =", interest) 