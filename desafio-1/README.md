# Desafio 1
## Linguagem 
Projeto foi desenvolvido em Python na versão 3.10.6.<br>
Foi utilizado o módulo python.os que é muito útil quando precisamos mexer com sistema de arquivos.

## Construção do código
Utilizei o paradigma funcional na construção desse codigo, ou seja, para simplifica a leitura, o codigo é composto por multiplas funções que faz uma determinada tarefa.  

### def menu
Essa função é a responsável em exibir as opções:
<br>0 - Sair<br>
1 - Filtrar por nome do cliente<br>
2 - Filtrar por tipo de arquivo<br>
3 - Filtrar por data solicitada<br>
4 - Excluir todos os arquivos do cliente<br>

### def foundcliente
Funcão recebe um parâmetro cliente, que é nome do cliente passado para a função.
Foi criada um variável found que conta o número de cliente econtrados, caso não seja encontrado nenhum entrará na condição found == 0.
A função contém dois laços de repetição que pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se o arquivo contém o nome do cliente passado como parâmetro.
Na verificação utulizei o method split para separar a string e em seguida comparo com o parâmetro cliente.

### def deletecliente



### def typefile

### def filtro
Função recebe um parâmetro file, que pode ser o tipo de arquivo ou data.
Essa função irá pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se cada arquivo corresponde ao parametro passado para a função caso seja correspondente imprimirá.
