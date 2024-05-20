#Vamos calcular a média aritmética
#Verificar se o valor inserido é do tipo float
def is_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False
        
def insira_um_numero(prompt):
    while True:
        num = input(prompt)
        if is_float(num):
            return float(num)
        else:
            print('Digite um número válido.')   

nota01 = insira_um_numero('Digite a primeira nota: ')
nota02 = insira_um_numero('Digite a segunda nota: ')
nota03 = insira_um_numero('Digite a terceira nota: ')

media = (nota01 + nota02 + nota03) / 3

print('A média aritmética das notas é: {:.2f}'.format(media))
