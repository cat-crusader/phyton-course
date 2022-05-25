import pika

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='to_agency')
    channel.queue_declare(queue='from_agency')
    print('queues created successfully')
