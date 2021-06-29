# amqps://dcznnvcv:dO7K5YreWZG0ZjUkmuaJAiRwvRAGUH7F@puffin.rmq2.cloudamqp.com/dcznnvcv

import pika, json

params = pika.URLParameters('amqps://dcznnvcv:dO7K5YreWZG0ZjUkmuaJAiRwvRAGUH7F@puffin.rmq2.cloudamqp.com/dcznnvcv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
