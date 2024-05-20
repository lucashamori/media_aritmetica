Este código Python calcula a média aritmética de três notas inseridas pelo usuário. Aqui está uma breve descrição de cada parte:

1. **Função `is_float(input_str)`**: Verifica se a string fornecida pode ser convertida para um número de ponto flutuante (float). Retorna `True` se for possível, caso contrário, `False`.

2. **Função `insira_um_numero(prompt)`**: Solicita repetidamente ao usuário que insira um número, utilizando a mensagem fornecida pelo parâmetro `prompt`. A função usa `is_float` para validar a entrada. Se a entrada for válida, converte a string para float e a retorna. Caso contrário, solicita novamente a entrada até que um número válido seja inserido.

3. **Coleta de notas**: Utiliza a função `insira_um_numero` para solicitar e armazenar três notas do usuário:
    - `nota01 = insira_um_numero('Digite a primeira nota: ')`
    - `nota02 = insira_um_numero('Digite a segunda nota: ')`
    - `nota03 = insira_um_numero('Digite a terceira nota: ')`

4. **Cálculo da média**: Calcula a média aritmética das três notas coletadas:
    - `media = (nota01 + nota02 + nota03) / 3`

5. **Impressão da média**: Exibe a média aritmética calculada, formatada com duas casas decimais:
    - `print('A média aritmética das notas é: {:.2f}'.format(media))`

O código garante que as entradas do usuário sejam números válidos e fornece um feedback contínuo até que entradas válidas sejam fornecidas, resultando no cálculo correto da média das notas inseridas.
