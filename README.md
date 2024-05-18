#Vamos calcular a média aritmética

#Verificar se o valor inserido é do tipo float.
def is_float(input_str):
    try:
        float(input_str)
        return True
    except ValueError:
        return False

def insira_um_numero(prompt):
    while True:
        n = input(prompt)
        if is_float(n):
            return float(n)
        else:
            print('Por favor, digite uma nota válida.')

nota1 = insira_um_numero('Digite a primeira nota: ')
nota2 = insira_um_numero('Digite a segunda nota: ')
nota3 = insira_um_numero('Digite a terceira nota: ')

media = (nota1 + nota2 + nota3) / 3

print(f'A média das notas é: {media:.2f}')
