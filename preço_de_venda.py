print("Informe o preço de compra")
compra = float(input())
print("Informe a % de lucro ")
perct = float(input())
lucro = compra/(1-(perct/100))
print(f"Preço de venda é ${lucro:.2f}")