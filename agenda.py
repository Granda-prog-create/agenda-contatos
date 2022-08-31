from os import system 

lista_de_contatos = [] 

def add_contato():
    nome = str(input('Digite o nome do contato: ')).title()
    numero = int(input('Digite o número do contato: '))
    system('cls')
    lista_add = {}
    lista_add['Nome'] = nome
    lista_add['Número'] = numero
    lista_de_contatos.append(lista_add) 
    print('###########################')
    print('Contato adicionado')
    print('###########################')
    
def mostra_contato():
    system('cls')
    for contato in lista_de_contatos:
        for chave, valor in contato.items():
            print(f'{chave}: {valor}')
              
def remove_contato():
    nome = str(input('Digite o nome que deseja remover: ')).lower()
    for c in lista_de_contatos: 
        if c['Nome'].lower() == nome.lower():
            i = lista_de_contatos.index(c) 
            lista_de_contatos.pop(i) 
            break
        else:
            print('Esse contato não existe') 
            
    
def edita_contato():
    nome = str(input('Digite o nome que deseja editar: ')).lower()
    for c in lista_de_contatos:
        if c['Nome'].lower() == nome.lower():
            opc = int(input('Deseja alterar o nome do contato? \n1-Sim\n2-Não'))
            if opc == 1:
                system('cls')
                novo = str(input('Digite o novo nome: '))
                c['Nome'] = novo
            opc-int(input('Deseja alterar o número? \n1-Sim\n2-Não '))     
            if opc == 1:
                system('cls')
                num = int(input('Digite o novo número: '))
                c['Número'] = num 
            system('cls')
            print('###########################')
            print('Contato atualizado com sucesso!')
            print('###########################')
            
        else:
                print('Esse contato não existe') 
                break
    return                            
             
        
while True:
    print('1- Adicionar contato: ')
    print('2- Mostrar contato: ')
    print('3- Remover contato: ')
    print('4- Editar contato: ')
    print('5- Sair: ')
    
    op = int(input('Digite a opção desejada: '))
    
    if op == 1:
        add_contato()
    if op == 2:
        mostra_contato()
    if op == 3:
        remove_contato()
    if op == 4:
        edita_contato()
    if op == 5:
        break 
    
print("Obrigado! Até a próxima!")                  
            