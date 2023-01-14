salary = int(input("Introduzca su salario:"))

if salary < 1000:
    # salario = salario + 15% salario
    salary = salary + (salary * 0.15)

print("Su salario es: " + str(salary))