valor1 = float(input ("Digite o valor 1: "))
valor2 = float(input("Digite o valaor 2: "))

def somar (valor1 , valor2):
    return valor1 + valor2

resultado = somar(valor1, valor2)

if resultado > 40:
    print (resultado)
else:
    print ("não retorno valores menores que 40")

   
