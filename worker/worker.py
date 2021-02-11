import redis
import json
from time import sleep
from random import randint

if __name__ == '__main__':
    r = redis.Redis(host='queue', port=6379, db=0)
    print ('waiting for massages...')
    while True:
        message = json.loads(r.blpop('sender')[1])
        # E-mail send simulation
        print('Send a message', message['subject'])
        sleep(randint(15, 45))
        print('Message', message['subject'], 'enviada')