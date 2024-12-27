from flask import Flask
import redis, os

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', '127.0.0.1')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

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