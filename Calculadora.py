#Pedro (Calculadora simples)
def add(x, y):
   return x + y

# Função para subtração
def subtract(x, y):
   return x - y

# Função para divisão
def divide(x, y):
   return x / y

# Função para multiplicação
def multiply(x, y):
   return x * y

print("Selecione o número da operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite sua opção (1/2/3/4): ")

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif opcao == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif opcao == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif opcao == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Opção inválida!")
