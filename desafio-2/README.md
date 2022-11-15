# Desafio 2

## Construção do projeto
No projeto criei um pagina html simples que será utilizado no Dockerfile.<br>
Dockerfile irá construir a imagem com ngnix e com o arquivo index.html.<br>
Depois de disponibilizar a imagem no DockerHub utilizei ela no docker-compose.<br>
Utilizei o docker-compose para a construção do container que utliza a imagem que está no DockerHub.<br>
[Imagem no DockerHub](https://hub.docker.com/repository/docker/kadeguilherme/desafio-2)

## Como executar
 ```bash
# Clone do repositório
$ git clone https://github.com/kadeguilherme/desafio-sensedia.git

# Executar o comando dentro da pasta /desafio-2 
$ docker-compose up
```
 Acessse o localhost na porta 8080 http://localhost:8080 para acessar a pagina principal.
