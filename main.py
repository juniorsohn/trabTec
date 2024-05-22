import re

def cria_saida(lista_formatada):
    
    with open('output.txt', 'w') as arquivo:
        for elemento in lista_formatada:
            linha = ' '.join(elemento)
            arquivo.write(linha + '\n')

def guarda_primeiro_estado(lista_de_estados, lista_formatada):
    
    for elemento in lista_formatada:
        lista_de_estados.append(elemento[0])
        print('o estado inicial eh:',elemento[0])
        
       
    lista_de_estados = list(set(lista_de_estados)) 
    print('\n',lista_de_estados)
    return lista_de_estados

def insere_rotina_inicial_sipser(lista_formatada):

    nova_inicial_0 = ['0', '0', '#', 'r', 'passa0']
    nova_inicial_1 = ['0', '1', '#', 'r', 'passa1']

    passa0_0 = ['passa0', '0', '0', 'r', 'passa0']
    passa0_1 = ['passa0', '1', '0', 'r', 'passa1']
    passa0_branco = ['passa0', '_', '0', 'r', 'retornaInicio']

    passa1_0 = ['passa1', '0', '1', 'r', 'passa0']
    passa1_1 = ['passa1', '1', '1', 'r', 'passa1']
    passa1_branco = ['passa1', '_', '1', 'r', 'retornaInicio']

    retornaInicio_tudo = ['retornaInicio', '*', '*', 'l', 'retornaInicio']
    retornaInicio_hash = ['retornaInicio', '#', '#', 'r', 'ini']
    
    ignora_mov_ext_esq = ['*', '#', '#', 'r', '*']
    
    lista_formatada.append(nova_inicial_0)
    lista_formatada.append(nova_inicial_1)
    lista_formatada.append(passa0_0)
    lista_formatada.append(passa0_1)
    lista_formatada.append(passa0_branco)
    lista_formatada.append(passa1_0)
    lista_formatada.append(passa1_1)
    lista_formatada.append(passa1_branco)
    lista_formatada.append(retornaInicio_tudo)
    lista_formatada.append(retornaInicio_hash)
    lista_formatada.append(ignora_mov_ext_esq)


    return lista_formatada


def faz_sipser(lista_formatada):
    
    #;S para DUPLAMENTE INFINITA
    # Marcar início da fita com "#" e joga tudo pra direita               
               
    # criar lista com o número de todos os estados (para uso posterior na criação "automática" de estados)
    # mover os estados '0' iniciais para "INI"
    # criar novo estado de início com índice 0
    
    
        # |0 0 # r passa0|
        # |0 1 # r passa1|

        # |passa0 0 0 r passa0|
        # |passa0 1 0 r passa1|
        # |passa0 _ 0 r retornaInicio|
       
                  
        # |passa1 0 1 r passa0|
        # |passa1 1 1 r passa1|
        # |passa1 _ 1 r retornaInicio|
        
        # |retornaInicio * * l retornaInicio|
        # |retornaInicio # # r ini|
        
    
    # Se "#" for lido, apenas move para a direita e volta para qualquer estado
        #   |* # # r *| 
    # executa normalmente
    
    
    # altera os estados iniciais lidos para uma nova designação "ini"
    for elemento in lista_formatada:
        if elemento[0] == '0':
            elemento[0] = 'ini'
        if elemento[4] == '0':
            elemento[4] = 'ini'
        #print(elemento)
            
    print('\nA lista com ini eh:', lista_formatada)
    
    # aqui começa a rotina inicial
    lista_formatada = insere_rotina_inicial_sipser(lista_formatada)
    
    print('\nA lista com rotina inicial eh:', lista_formatada)
    
    return lista_formatada


def main():
    #print('Hello World')
    
    #cria lista com programa inteiro
    lista_programa = []
    
    with open("odd.txt", "r") as arquivo_in:
        for linha in arquivo_in:
            if linha == ';S' or ';I':
                lista_programa.append(linha)
            else:
                linha = re.split(r'(\s)',arquivo_in.readline())
                linha = ' '.join(linha).split()
                lista_programa.append(linha)
    print('A lista eh:',lista_programa,'\n')
    

    #tira o '\n' de cada elemento da lista    
    lista_formatada = [linha_lida.split() for linha_lida in lista_programa]
    lista_de_estados = []

    #lista_programa.pop(0)
    
    print('elemento 1: ',lista_formatada[0])

    
    
    if ';S' in lista_formatada[0]:
        print('Recebido programa de Sipser para rodar em Maquina de Fita Duplamente Infinita\n')
        lista_formatada.pop(0)
        lista_de_estados = guarda_primeiro_estado(lista_de_estados,lista_formatada)    
        
        faz_sipser(lista_formatada)
        cria_saida(lista_formatada)
    else:
        if ';I' in lista_formatada[0]:
            print('Recebido programa de Fita Duplamente Infinita para rodar em Maquina de Sipser\n')
            lista_formatada.pop(0)
            lista_de_estados = guarda_primeiro_estado(lista_de_estados,lista_formatada)
            #faz_duplaInf(lista_formatada)
            #cria_saida(lista_formatada)
    
    #print('a nova lista eh:',lista_formatada,'\n')
    
    #for i, elemento in enumerate(lista_formatada):
    #    print(f'Elemento {i+1}:', end='')
    #    for j, caractere in enumerate(elemento):
    #        print(f"caractere {j + 1} = {caractere}", end=", " if j < len(elemento) - 1 else "\n")


            
    #;I para SIPSER
    # primeira coisa é ler o arquivo de input
    # separar os atributos por espaço, em:
    
    # <estado> <simbolo lido> <simbolo escrito> <movimento> <próximo estado>
    
    # colocar símbolo de borda esquerdo (#) e símbolo de borda direito (&) + rotina de voltar ao início
        # |0 0 # r passa0|
        # |0 1 # r passa1|

        # |passa0 0 0 r passa0|
        # |passa0 1 0 r passa1|
        # |passa0 _ 0 r marcaFim|

        # |passa1 0 1 r passa0|
        # |passa1 1 1 r passa1|
        # |passa1 _ 1 r marcaFim|

        # |marcaFim _ & l retornaInicio|

        # |retornaInicio * * l retornaInicio|
        # |retornaInicio # # r ini|
    
    # Garantir que: 
        # Caso "#" seja lido, colocar mais um espaço à esquerda ( e volta para o primeiro símbolo à direita)
        # Caso "&" seja lido, colocar mais um espaço à direita (e volta para o primeiro símbolo encontrado à esquerda, ou seja, não volta pro começo).
        # Voltar ao estado que "chamou" essa rotina:
            # para #: 
               #      |$n_estado$_passaHash 0 _ r $n_estado$_passaHash0|
               #      |$n_estado$_passaHash 1 _ r $n_estado$_passaHash1|
               #      |$n_estado$_passaHash _ _ r $n_estado$_passaHashBranco|
               
               #      |$n_estado$_passaHash0 0 0 r $n_estado$_passaHash0|
               #      |$n_estado$_passaHash0 1 0 r $n_estado$_passaHash1|
               #      |$n_estado$_passaHash0 _ 0 r $n_estado$|
               
               #      |$n_estado$_passaHash1 1 1 r $n_estado$_passaHash1|
               #      |$n_estado$_passaHash1 0 1 r $n_estado$_passaHash0|
               #      |$n_estado$_passaHash1 _ 0 r $n_estado$|
               
               #      |$n_estado$_passaHashBranco _ _ r $n_estado$_passaHashBranco|
               #      |$n_estado$_passaHashBranco 0 _ r $n_estado$_passaHash0|
               #      |$n_estado$_passaHashBranco 1 _ r $n_estado$_passaHash1|
               
               
            # para &:
                #         |$n_estado$ & _ r espaçoDireita_$n_estado$|
                #         |espaçoDireita_$n_estado$ _ & l $n_estado$|
               


if __name__ == "__main__":
    main()

