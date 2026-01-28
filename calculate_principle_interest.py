p = float(input("Enter the principal:"))
r = float(input("Enter rate of interest:"))
t = float(input("Enter Time period(in years):"))

si = (p*r*t)/100
amount = p*(1+r/100) ** t
ci = amount - p
print("Simple Interest:",si)
print("Compound Interest:",ci)
