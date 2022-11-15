# Desafio 1
## Linguagem 
Projeto foi desenvolvido em Python na versão 3.10.6.<br>
Foi utilizado o modulo python.os que é muito util quando precisamos mexer com sistema de arquivos.

## Construção do codigo
Utilizei o paradigma funcional na construção desse codigo, ou seja, para simplifica a leitura o codigo é composto por multiplas funções que faz uma determinada tarefa.  

### def menu
Essa função é a responsavel em exibir as opções:
<br>0 - Sair<br>
1 - Filtrar por nome do cliente<br>
2 - Filtrar por tipo de arquivo<br>
3 - Filtrar por data solicitada<br>
4 - Excluir todos os arquivos do cliente<br>

### def foundcliente
Funcão recebe um paramentro cliente, que é nome do cliente.
Foi criada um variavel found que conta o numero de cliente econtrados, caso não seja encontrado nenhum entrará na condição found == 0.
Essa função irá pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se o arquivo contem o nome do cliente passado como paramentro logo em seguinda verifica se o ultimo carcater do arquivo é igual do paramentro.

### def deletecliente



### def typefile

### def filtro
Função recebe um parametro file, que é o nome do arquivo.
Essa função irá pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se cada arquivo corresponde ao parametro passado para a função caso seja correspondente imprimirá o nome do arquivo.
