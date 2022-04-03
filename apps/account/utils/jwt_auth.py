from django.conf import settings
import datetime
import jwt
from jwt import exceptions


def create_token(payload, timeout=9999):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    salt = settings.SECRET_KEY
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=timeout)
    result = jwt.encode(payload=payload, key=salt, algorithm="HS256", headers=headers)
    return result


def parse_payload(token):
    salt = settings.SECRET_KEY
    result = {'status': False, 'data': None, 'error': None}
    try:
        # verified_payload = jwt.decode(token, JWT_SALT, True)
        verified_payload = jwt.decode(token, salt, algorithms=["HS256"])
        result['status'] = True
        result['data'] = verified_payload
    except exceptions.ExpiredSignatureError:
        result['error'] = 'token已失效'
    except jwt.DecodeError:
        result['error'] = 'token认证失败'
    except jwt.InvalidTokenError:
        result['error'] = '非法的token'
    return result
