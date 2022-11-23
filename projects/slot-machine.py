import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 10
ROWS = 3
COLUMNS = 3
symbols = {
    "😈": 2,
    "😀": 4,
    "😭": 6,
    "🤢": 8,
}
symbolsValues = {
    "😈": 5,
    "😀": 4,
    "😭": 3,
    "🤢": 2,
}

# getSlotMachineRotation()
# Tipando symbols principalmente para conseguir o auto complete no symbols.items()
# dict é o tipo object no javascript, é um dicionário com key pair values


def deposit():
    while True:
        amount = input("Quanto você gostaria de depositar? R$")
        # Se for um número negativo, vai retornar false
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Valor deve ser maior que R$0.")
        else:
            print("Por favor digite um número.")
    return amount


def getNumberOfLines():
    while True:
        lines = input(
            "Digite o número de linhas que você quer apostar: (1-" + str(MAX_LINES) + ")? ")
        # Se for um número negativo, vai retornar false
        if lines.isdigit():
            lines = int(lines)
            # Jeito legal no python para verificar valores dentro de uma range
            # Número de linhas maior ou igual a 1 e menor ou igual ao MAX_LINES
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Número de linhas deve ser entre 1 e " +
                      str(MAX_LINES) + ".")
        else:
            print("Por favor digite um número.")
    return lines


def getBet():
    while True:
        amount = input("Quanto você gostaria de apostar? R$")
        # Se for um número negativo, vai retornar false
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                # Colocar f antes da string para poder mostrar variáveis mais fáceis
                print(
                    f"Valor deve ser entre R${MIN_BET} - R${MAX_BET}. {10 - 1}")
        else:
            print("Por favor digite um número.")
    return amount


def getSlotMachineRotation(rows: int, cols: int, symbols: dict):
    # symbols é um dict e temos que criar uma list a partir dos symbols e da quantidade de vezes
    # que representam, ou seja "😈" tem o "valor" de 2, então o loop vai rodar duas vezes para
    # preencher o allSymbols. No final, allSymbols vai ficar desse jeito:
    # 😈, 😈, 😀, 😀, 😀, 😀, 😭, 😭, 😭, 😭, 😭, 😭, 🤢, 🤢, 🤢, 🤢, 🤢, 🤢, 🤢, 🤢
    allSymbols = [] 
    for symbol, symbolCount in symbols.items():
        # allSymbols.append(symbol)
        # _ é uma variável anônima. Usa-se _ quando não se importa com o valor
        for _ in range(symbolCount):
            # append seria o push() do javascript
            allSymbols.append(symbol)
    # 1) Começamos com um array ou list (no python) vazio
    columns = []
    # 2) Fazemos um loop de acordo com a quant. de colunas que foi passada na função
    for _ in range(cols):
        # 3) Como o padrão é 3 colunas, esse loop vai rolar 3 vezes, e para cada uma, criamos uma coluna
        column = []
        # [:] para fazer uma cópia do objeto, seria ... no javascript
        # 4) Fazemos uma cópia do objeto para conseguirmos excluir sem afetar o original (memory reference)
        allSymbolsCopy = allSymbols[:]
        # 5) Para cada iteração da coluna fazemos 3 iterações nas linhas que foi passada na função
        for _ in range(rows):
            # 6) Escolhemos um valor aleatório do array allSymbolsCopy
            value = random.choice(allSymbolsCopy)
            # 7) Removemos esse mesmo símbolo do allSymbolsCopy para não escolhermos duas vezes
            allSymbolsCopy.remove(value)
            # 8) Colocamos o valor gerado na column do loop anterior. Cada column vai ter 3 rows
            column.append(value)
        # Aqui colocamos cada column gerada com suas respectivas 3 rows no array columns que
        # representa a máquina. columns = [ [], [], [] ]
        columns.append(column)
    return columns


def showSlotMachine(columns):
    # Input:
    # [😈, 🤢, 🤢] -> length = 3 elements - len = 3 porque no python não começa pelo index 0
    # [😶‍🌫️, 🤯, 🤢] -> length = 3 elements - len = 3 porque no python não começa pelo index 0
    # [😶‍🌫️, 🤯, 🤯] -> length = 3 elements - len = 3 porque no python não começa pelo index 0
    # Porém temos que recriar verticalmente
    # [😈, 😶‍🌫️, 😶‍🌫️] -> length = 3 elements - len = 3 porque no python não começa pelo index 0
    # [🤢, 🤯, 🤯] -> length = 3 elements - len = 3 porque no python não começa pelo index 0
    # [🤢, 🤢, 🤯] -> length = 3 elements - len = 3 porque no python não começa pelo index 0
    # Esse problema se chama red TRANSPOSE red
    # Isso assume que temos um array de arrays em cada um dos arrays tem uma length igual
    for row in range(len(columns[0])):
        # enumarate retorná além do valor do array, o index
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                # end por padrão cria uma nova linha ( end="\n" )
                print(f"{column[row]}", end=" | ")
            else:
                print(f"{column[row]}", end="")
        print()


def checkVictory(columns: int, lines: int, bet: int, values: dict):
    winnings = 0
    winningLines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)
    return winnings, winningLines


def game(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet > balance:
            print(
                f"Você não pode apostar essa quantidade porque na sua conta tem R${balance}.")
        else:
            break
    print(
        f"Você está apostando R${bet} em um total de {lines} linhas. Total da aposta é igual à {totalBet}")

    slots = getSlotMachineRotation(ROWS, COLUMNS, symbols)
    showSlotMachine(slots)
    winnings, winningLines = checkVictory(slots, lines, bet, symbolsValues)
    print(f"Você ganhou R${winnings}.")
    print(f"Você ganhou nas linhas: ", *winningLines)
    return winnings - totalBet


def main():
    balance = deposit()
    while True:
        print(f"Total na carteira: R${balance}")
        spin = input("Aperte enter para girar (s para sair).")
        if spin == "s":
            break
        balance += game(balance)
    print(f"Você saiu com R${balance}")


main()
