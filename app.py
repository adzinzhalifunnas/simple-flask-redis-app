from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

def check_redis_connection():
    try:
        redis_client.ping()
        print('Connected to Redis server')
    except redis.ConnectionError:
        print('Error: Redis server is not running')
        exit(1)

check_redis_connection()

@app.route('/')
def hello():
    count = redis_client.incr('hits')
    return f'Hello! This page has been visited {count} times.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)