def soma(num1, num2):
    total = num1 + num2
    return total

n1 = int(input("Digite o primeiro valor da soma: "))
n2 = int(input("Digite o segundo valor da soma: "))
         
total = soma(n1,n2)
print("A soma de {} e {} é {}".format(n1,n2,total))    