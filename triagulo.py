#Aluno:João Victor Guimarães

print("Insira 3 valores\n")
num1 = float(input("Primeiro valor: "))
num2 = float(input("Segundo valor: "))
num3 = float(input("Terceiro valor: "))

if num1 < (num2+num3):
    if num2 < (num1+num3):
        if num3 < (num2+num1):
            print("É um triagulo")
        else:
            print("Não é um triagulo")
    else:
            print("Não é um triagulo")
else:
            print("Não é um triagulo")
            