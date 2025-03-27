import jwt
import datetime
from auth.redis_handler import redis_client

SECRET_KEY = 'secret'

def create_token(user_id, role: str):
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    redis_client.set(token, 'whitelisted', ex=3600)

    return token

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        if redis_client.get(token) == 'blacklisted':
            return None

        return payload
    except jwt.ExpireSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


