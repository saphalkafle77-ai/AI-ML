# simple interest by converting principal, rate and time in float
principal = input("Enter principal:")
rate = input("Enter rate:")
time = input("Enter time:")

principal = float(principal)
rate = float(rate)
time = float(time)

SI = (principal * rate * time) / 100

print("Simple interest is:", SI)
