# ASA

Disciplina de Arquitetura de Software Aplicada

## O Framework Flask

O framework Flask é um micro framework web escrito em Python. É classificado como um microframework porque não requer ferramentas ou bibliotecas específicas. Ele não tem camada de abstração de banco de dados, validação de formulário ou quaisquer outros componentes onde bibliotecas de terceiros pré-existentes fornecem funções comuns.

### Instalação

```bash
pip install Flask
```

### Hello World

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

## Dockerfile

Um Dockerfile é um documento de texto que contém todos os comandos que um usuário poderia chamar na linha de comando para montar uma imagem. Usando o docker build, os usuários podem criar uma compilação automatizada que executa várias instruções de linha de comando em sucessão.

### Dockerfile
Exemplo de Dockerfile para Flask

```dockerfile
FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]
```

## Docker-compose

Docker Compose é uma ferramenta para definir e executar aplicativos multi-contêiner do Docker. Com o Compose, você usa um arquivo YAML para configurar os serviços do aplicativo. Em seguida, com um único comando, você cria e inicia todos os serviços a partir da sua configuração.

### docker-compose.yml

Exemplo de docker-compose.yml para Flask

```yaml
version: '3'
services:
  web:
    build: . #isso constrói a imagem a partir do Dockerfile no diretório atual
    ports:
      - "5000:5000"
```

## Mensageria

A mensageria é uma forma de comunicação entre duas ou mais partes, onde as partes que estão enviando as informações não são necessariamente conscientes de quem está recebendo as informações. As partes que estão enviando as informações são chamadas de produtores e as partes que estão recebendo as informações são chamadas de consumidores.

### MQTT e AMQP

MQTT e AMQP são protocolos de mensageria que são usados para se comunicar com dispositivos. MQTT é um protocolo de mensageria leve que é usado para comunicação máquina-a-máquina. AMQP é um protocolo de mensageria que é usado para comunicação entre aplicativos.

### RabbitMQ

RabbitMQ é um message broker de código aberto que implementa o Advanced Message Queuing Protocol (AMQP). É escrito na linguagem de programação Erlang e é construído no framework Open Telecom Platform para clustering e failover.

### Instalação

```bash
docker pull rabbitmq:3-management
```

### Mosquitto

Mosquitto é um message broker de código aberto que implementa o protocolo MQTT. É escrito em C e está disponível para Linux, Windows e MacOS.

### Instalação

```bash
docker pull eclipse-mosquitto
```

## Message Queue

Uma message queue é uma área de armazenamento temporária onde as mensagens são mantidas até serem processadas. Uma message queue é usada para se comunicar entre dois ou mais aplicativos. Os aplicativos que estão enviando as mensagens são chamados de produtores e os aplicativos que estão recebendo as mensagens são chamados de consumidores.

## Binding

Um binding é um link entre uma queue e um exchange. Um binding é criado por um exchange e uma queue. O exchange é a fonte das mensagens e a queue é o destino das mensagens. O binding é criado pelo exchange e a queue. O binding é criado pelo exchange e a queue. O binding é criado pelo exchange e a queue.

## Exchanges

Um exchange é um componente do RabbitMQ que recebe as mensagens de um ou mais produtores e as envia para uma ou mais filas. Um exchange é um componente do RabbitMQ que recebe as mensagens de um ou mais produtores e as envia para uma ou mais filas. Um exchange é um componente do RabbitMQ que recebe as mensagens de um ou mais produtores e as envia para uma ou mais filas. Um exchange é um componente do RabbitMQ que recebe as mensagens de um ou mais produtores e as envia para uma ou mais filas.

## Filas

Uma fila é um componente do RabbitMQ que armazena as mensagens. Uma fila é um componente do RabbitMQ que armazena as mensagens. Uma fila é um componente do RabbitMQ que armazena as mensagens. Uma fila é um componente do RabbitMQ que armazena as mensagens.

![RabbitMQ interface](https://www.cloudamqp.com/img/blog/management-overview.png)