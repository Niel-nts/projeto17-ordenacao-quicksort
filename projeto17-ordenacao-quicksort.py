# EXEMPLO DE CÓDIGO QUICK SORT

# Aqui começa as funções de ordenação
def quickSort(alist):  # função que serve apenas para iniciar a ordenação
    quickSortHelper(alist, 0, len(alist) - 1)  # Aqui a função chamada "quicksorthelper" é chamada, o primeiro parâmetro
        # se refere à lista de números que será analisada, o segundo parâmetro é o valor da posição inicial (se será o termo 0, 1, 2...)
        # e o terceiro parâmetro é o valor da posição final. Incialmente, o valor da posição inicial foi preenchido com "0" e o
        # valor da posição final é definido pelo comando "len" que nos diz quantos termos temos na lista, lembre-se que os
        # vetores de uma lista começam com "0" e a contagem de termos de uma lista len começa contando com 1, por
        # isso o "len(alist)-1" que equivale a 8!

def quickSortHelper(alist, first, last):  # função que se repetirá até que o valor de posição inicial seja imediatamente
    # antecessor ao valor de posição final. Incialmente começamos com first==0 e last==8, mas conforme a função é repetida,
    # splitpoint +1 e -1 vai diminuindo essa diferença;

    if first < last:  # essa condicional garante que a função será interrompida conforme explicado no comentário anterior;

        splitpoint = partition(alist, first, last)  # Aqui a variável "splitpoint" será preenchida pelo resultado retornado da
        # função "partition". Inicialmente temos os parâmetros "partition(alist, 0, 8)"; Depois de alguns loops dentro
        # da função partition, o primeiro valor retornado é 5 e agora o programa passa para a próxima linha de código;

        quickSortHelper(alist, first, splitpoint - 1)  # aqui, na primeira vez que essa parte do código é executada, temos
        # "quickSortHelper(alist, 0, 4)"; Ou seja, a função "quickSprtHelper" é novamente chamada e uma nova
        # cadeia de execução é realizada voltando novamente para "splitpoint = partition(alist, 0, 4)"; Na terceira vez
        # que algum valor retorna para "splitpoint" , temos o valor de "splitpoint" valendo 0, nesse ponto  é que o
        # código abaixo é executado.

        quickSortHelper(alist, splitpoint + 1, last)

        # OBS: Conforme a função quickSortHelper vai sendo executada, vai se formando uma cadeia de execução, de
        # modo que quando se alcança um ponto que a condicional "first < last" não é atendida, o programa volta
        # para a cadeia anterior com os valores antigos de first e last.

def partition(alist, first, last):  # função que realiza a ordenação

    pivotvalue = alist[first]  # Inicialmente, essa variável receberá o valor do termo "alist[0]"; Em outras rodadas de
    # execução do código também recebe o valor de splitpoint+1
    leftmark = first + 1  # Inicialmente, como o valor de "first" é 0, "leftmark" passa a valer 1;
    rightmark = last  # last incialmente vale 8
    done = False  # variável booleana para controle de repetição

    while not done:  # enquanto a variável "done" não for verdadeira
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:  # Esse loop acontecerá enquanto o valor de
            # "leftmark" (Inicialmente "1") for menor ou igual ao valor de "rightmark" (que inicialmente vale 8) e,
            # também, enquanto o próximo termo "alist[leftmark]" (que inicialmente é o "alist[1]") for menor ou igual ao
            # valor de "pivotvalue" (que inicialmente é o "alist[0]")
            leftmark = leftmark + 1  # incremento ao valor de "leftmark" (que incialmente começa, a partir desse ponto, a valer 2)
            # no primeiro momento em que o loop acontece, o loop vai parar quando chegar em "alist[2]" que equivale a
            # 93 e que é maior que "alist[0]" que vale 54.

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
            # resumo desse enquanto: faz a mesma coisa que o anterior porém no sentido inverso, da direita para
            # esquerda (ultimo termo da lista para o primeiro) e enquanto o contador rightmark não alcançar o valor do
            # contador leftmark. Inicialmente temos: alist[8] >= alist[0] ou seja, 20>=54; e rightmark sendo 8 e leftmark
            # sendo 2. Como já na primeira passagem as condições para o loop não são preenchidas, o decremento
            # ("rightmark-1") não acontece.

        if rightmark < leftmark:  # se o valor de rightmark for menor que o valor de "leftmark", então o loop é
            # interrompido. Inicialmente o loop ainda não será interrompido pois o rightmark vale 8 e o leftmark vale 2.
            done = True
        else:  # senão, as variáveis abaixo têm seus valores alterados e o loop volta para o começo
            # na primeira rodada, temos: alist[2] vale 93 e alist[8] vale 20
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            # agora, alist[2] vale 20 e alist[8] vale 93

        # Agora outros valores são trocados de posição; na primeira rodada, temos: alist[0] valendo 54 e alist[8] valendo 93
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        # agora, alist[0] vale 93 e alist[8] vale 54

    return rightmark  # quando o loop finalmente é interrompido ele retorna o valor de rightmark; Na primeira vez que isso ocorre, rightmark vale 5;


# aqui começa o programa
alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]  # essa é a lista de numeros com o nome "alist"
quickSort(alist)  # quicksort é o nome da função que irá ordenar a lista "alist"
print(alist)  # exibe a lista ordenada na tela
