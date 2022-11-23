from cryptography.fernet import Fernet
# https://cryptography.io/en/latest/fernet/

'''''
def writeKey():
    key = Fernet.generate_key()
    with open('./projects/key.key', 'wb') as keyFile:
        keyFile.write(key)


writeKey()'''''


def loadKey():
    file = open('./projects/key.key', 'rb')
    key = file.read()
    file.close()
    return key


# key = loadKey()
# fer = Fernet(key)


def add(fer: Fernet):
    name = input('Nome da conta: ')
    pwd = input('Senha: ')
    # Abrindo/criando um arquivo com with vai automaticamente fechar o arquivo depois da operação
    # 'a' = append
    with open('./projects/passwords.txt', 'a') as fs:
        # Outro jeito de abir, porém vai ter que fechar manualmente
        # file = open('passwords.txt', 'a')
        # file.close()
        # fs.write(f'{name} | {str(fer.encrypt(pwd.encode()))} \n')
        fs.write(f'{name} | {fer.encrypt(pwd.encode()).decode()} \n')


def view(fer: Fernet):
    # 'r' = read
    with open('./projects/passwords.txt', 'r') as fs:
        for line in fs.readlines():
            # Vai mostrar as linhas sem o \n
            # print(line.rstrip())
            data = line.rstrip()
            u, p = data.split('|')
            # print(f'Usuário: {u}. Senha: {str(fer.decrypt(p.encode()))}')
            print(f'Usuário: {u}. Senha: {fer.decrypt(p.encode()).decode()}')


def main():
    masterKey: str = input('Digite a Master Key: ')
    key: bytes = loadKey() + masterKey.encode()
    fer: Fernet = Fernet(key)

    while True:
        mode = input(
            'Gostaria de adiconar uma nova senha ou ou ver as existentes? (add, view). Aperte s para sair - ').lower()
        if mode == 's':
            break
        if mode == 'add':
            add(fer)
        elif mode == 'view':
            view(fer)
        else:
            print('Inválido. Escolhe entre add | view')
            continue


main()
