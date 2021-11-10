nesse projeto foi implementado um comportamento de um tocador de musical,que possui as seguintes funcionalidades:

play: começa a tocar as músicas da lista, na ordem da lista, a partir da música atual, caso já não esteja tocando (não tem efeito caso
contrário).

stop: interrompe a execução da música atual.
add id: acrescenta a música id ao final da lista.

del id: retira a primeira ocorrência da música id na lista, se houver e desde que não esteja tocando. Não interrompe a execução da
música atual.

next id: define que a música id, se presente na lista, será a próxima a ser tocada, desde que não seja a que esteja sendo tocada no
momento. A ocorrência de id na lista é realocada para tanto.

list: mostra os ids das músicas na lista, separados por vírgula, ou a mensagem "[vazia]" caso a lista esteja vazia.
current mostra o id da música atual (sendo tocada no momento), ou da próxima a ser tocada, caso nenhuma esteja no momento. Se
a lista estiver vazia, apresente a mensagem: "Toque! Toque, Dijê!".

undo: [*] desfaz os efeitos de uma instrução add, del, next ou play. Isoladamente, desfaz o efeito da última instrução. Havendo o
argumento opcional *, desfaz o efeito de todas as instruções dadas até aquele ponto.

fight: interrompe o programa para iniciar o ataque ao Império.