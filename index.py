altura = float(input("Digite sua altura: "))#criou uma variavel chamada ALTURA do tipo float, onde o usuario ira digitar no console para dar valor a ela
peso = float(input("Digite seu peso: "))

imc = (peso / altura ** 2)

if imc > 18.5:#SE IMC FOR MENOR QUE 18.5
    resultado = "se ta magro em fi"#A VARIAVEL 

elif imc < 24.9:
    resultado = "ta de boas ou normal"

elif imc > 29.9:
    resultado = "ce ta pouco gordim"

else:
    resultado = "ce ta bem gordin"

print(f"Seu imc é {imc:.2f} , classificado como {resultado}")


while True:
    
    print("HELLO WORLD")

#PARA ELE SABER OQ ESTA DENTRO DE CADA IF OU ELIF OU ELSE, TERA QUE TER O ESPAÇAMENTO, PRA FICAR MELHOR EXPLICADO A LINHA BRANCAS