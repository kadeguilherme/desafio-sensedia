# Desafio 1
## Linguagem 
Projeto foi desenvolvido em Python na versão 3.10.6.<br>
Foi utilizado o módulo python.os que é muito útil quando precisamos mexer com sistema de arquivos.

## Construção do código
Utilizei o paradigma funcional na construção desse codigo, ou seja, para simplifica a leitura, o codigo é composto por multiplas funções que faz uma determinada tarefa.  

### menu
Essa função é a responsável em exibir as opções:
<br>0 - Sair<br>
1 - Filtrar por nome do cliente<br>
2 - Filtrar por tipo de arquivo<br>
3 - Filtrar por data solicitada<br>
4 - Excluir todos os arquivos do cliente<br>

### foundcliente
Funcão recebe um parâmetro cliente, que é nome do cliente passado para a função.
Foi criada um variável found que conta o número de cliente econtrados, caso não seja encontrado nenhum entrará na condição found == 0.
A função contém dois laços de repetição que pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se o arquivo contém o nome do cliente passado como parâmetro.
Na verificação utulizei o method split para separar a string e em seguida comparo com o parâmetro cliente.

### deletecliente
Funcão é bem parecida com a foundcliente, recebe um parâmetro cliente, que é nome do cliente passado para a função.
Foi criada um variável found que conta o número de cliente econtrados, caso não seja encontrado nenhum entrará na condição found == 0.
A função contém dois laços de repetição que pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se o arquivo contém o nome do cliente passado como parâmetro, caso seja verdadeira a comparação, o arquivo é excluido.
Na verificação utulizei o method split para separar a string e em seguida comparo com o parâmetro cliente.
No final é impresso a cliente que foi excluído.

### typefile
A funcào é responsável pela escolha do tipo do arquivo, calls ou metrics.
Após a opcào escolhida é passa como parâmetro para a função  filtro.

### filtro
Função recebe um parâmetro file, que pode ser o tipo de arquivo ou data.
Essa função irá pecorrer o diretorio, subdiretorios e os arquivos, apos isso verifica se cada arquivo corresponde ao parametro passado para a função caso seja correspondente imprimirá.

## Arvore de diretorios
Estrutura do arquivo tem que igual para a busca dos arquivos funcionar.
O diretorio ***desafio*** tem que está dentro do diretorio ***desafio-sensedia***. Conforme abaixo.

```
├── desafio-sensedia
├── desafio
|  └── volume_1
|  └── volume_2
|  └── volume_3
|  └── volume_4
|  └── volume_5
|  └── volume_6
├── desafio-1
|  ├── main.py
├── desafio-2
```
## Como executar
 ```bash
# Clone do repositório
$ git clone https://github.com/kadeguilherme/desafio-sensedia.git

# Executar o comando dentro da pasta /desafio-1
# obs: No meu caso a opcão excluir cliente, deverá executar o main.py com usuário root
$ pyhton3 main.py
```
Após executar o camando exibirá no terminal o menu a seguir:<br>
<img src="https://github.com/kadeguilherme/k8s-basico/blob/main/images/menu.png" >

