#Jade Carvalho (11261100871) e Eduarda Andrade (11261100359)
#14/03/2026
#Engenharia de Software - UMC
#Software Básico - 1B
#Trabalho Avaliativo 01

#Cabeçalho 
titulo=r""" #Utilizamos a "raw string" pois o ASCII art que queriamos, utlizava muitas "\" que é um caractere especial usado em python, por isso optamos em utilizar essa string para evitar possíveis erros
  /$$$$$$           /$$                     /$$                         /$$                    
 /$$__  $$         | $$                    | $$                        |__/                    
| $$  \__/ /$$$$$$ | $$  /$$$$$$$ /$$   /$$| $$  /$$$$$$  /$$$$$$/$$$$  /$$  /$$$$$$   /$$$$$$ 
| $$      |____  $$| $$ /$$_____/| $$  | $$| $$ |____  $$| $$_  $$_  $$| $$ /$$__  $$ |____  $$
| $$       /$$$$$$$| $$| $$      | $$  | $$| $$  /$$$$$$$| $$ \ $$ \ $$| $$| $$  \ $$  /$$$$$$$
| $$    $$/$$__  $$| $$| $$      | $$  | $$| $$ /$$__  $$| $$ | $$ | $$| $$| $$  | $$ /$$__  $$
|  $$$$$$/  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$|  $$$$$$$| $$ | $$ | $$| $$|  $$$$$$$|  $$$$$$$
 \______/ \_______/|__/ \_______/ \______/ |__/ \_______/|__/ |__/ |__/|__/ \____  $$ \_______/
                                                                            /$$  \ $$          
                                                                           |  $$$$$$/          
                                                                            \______/
"""
subtit="A cálculadora da Trabalhadora Horista (CTH)"
linha="#" *110

#Entrada de dados
print(titulo)
print(subtit)
print(linha)

NOME=input("Insira o seu nome: ")
CPF=input("Insira o seu CPF: ")
CARGO=input("Insira o seu cargo: ")
HN=float(input("Insira o total de horas regulares trabalhadas (desconsiderando horas extras): "))
VH=float(input("Insira o valor da hora trabalhada: (exemplo: valor= R$40,95 escreva: 40.95) R$: "))
HE=float(input("Insira o total de horas extras trabalhadas: "))
AD=float(input("Insira o valor do percentual adicional sobre as horas extras (exemplo: valor= 20,2% escreva: 20.2): "))
Desc=float(input("Informe o percentual de descontos gerais aplicado sobre o salário (exemplo: valor= 15,3% escreva: 15.3): "))

#Processamento
SHN=HN*VH #Cálculo para descobrir o salário normal do funcionário
SHE=HE*VH #Cálculo para descobrir o salário com o acréscimo da hora extra
SHEA=SHE*(AD/100)+SHE #Cálculo para descobrir o salário com hora extra mais a porcentagem adicional
SB=SHEA+SHN #Cálculo para descobrir o salário bruto
SL=SB-SB*(Desc/100) #Cálculo para descobrir o salário líquido

#Saída de dados
saída=f"""
        {"=" *70}
        {"RECIBO DE PAGAMENTO":^70} 
        {"=" *70}

        TRABALHADOR:\033[1;35m {NOME} \033[0m
        CPF: \033[1;35m {CPF} \033[0m
        CARGO: \033[1;35m {CARGO} \033[0m

        {"=" *70}
        {"DEMOSNTRATIVO DO SALÁRIO":^70}
        {"=" *70}

        O salário regular é igual a:\033[1;32mR$ {SHN:.2f} \033[0m
        O salário com acréscimo das horas extras trabalhadas é igual a:\033[1;32mR$ {SHE:.2f} \033[0m
        O salário com hora extra acrescentado a porcentagem adicional é igual a:\033[1;32mR$ {SHEA:.2f} \033[0m
        O salário bruto tem valor igual a:\033[1;32mR$ {SB:.2f} \033[0m
        O salário líquido tem valor igual a:\033[1;32mR$ {SL:.2f} \033[0m
"""

print(saída)