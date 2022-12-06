import pika

# connection = pika.BlockingConnection(
#    pika.ConnectionParameters(host='172.17.0.5'))
#channel = connection.channel()

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('127.0.0.1',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='hello')
message = 'UFU Engenharia da Computação!!'
channel.basic_publish(exchange='ufu', routing_key='hello', body=message)
print(" [x] Sent 'Hello World!'")
