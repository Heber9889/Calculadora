global A,B,C,D,X,E,F

A = '\033[1;31m'
X = '\033[1;32m'
C = '\033[1;33m'
D = '\033[1;34m'
E = '\033[1;37m'
B = '\033[1;35m'
F = '\033[1;36m'

print (f"\n\n\n                   {X}####CALCULADORA####        \n\n\n\n")

print (f'{D}____________________________________________________ 2022 ©')
print (f'{E}#-SOMA',f'{C}[1]-',f'{E}#DIVIZAO',f'{A}[2]-',f'{E}#SUBITRACAO',f'{B}[3]-',f'{E}#MUTIPLICACAO',f'{F}[4]')
print (f'{D}===========================================================\n')

operacao = input('escolha a opçao: ')
print (f'\n{D}===========================================================\n')

numero1 = input('\n|                #_PRIMA_O_PRIMEIRO_VALOR:_   ')
print (f'\n\n{D}===========================================================\n')
numero2 = input('\n|                 #__PRIMA_O_SEGUNDO_VALOR:_   ')
print (f'\n\n{D}===========================================================\n')

if operacao ==  "1" :
    resultado = int(numero1) + int(numero2)
    print ('ok')

if operacao == "2" :
    resultado = int(numero1) / int(numero2)

if operacao == "3" : resultado = int(numero1) - int(numero2)

if operacao == "4" :
    resultado = int(numero1) * int(numero2)
    print ('ok')

else:
    resultado = "OPERADOR_NAO_SUPORTADO"

print ("\n\n              _O_RESULTADO_DA_OPERACAO_É : \n\n                ", str(resultado))

print (f'\n{D}===========================================================\n')
print (f'{D}===========================================================\n')
print (f'{D}===========================================================\n')

