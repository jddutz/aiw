# app/services/token_manager.py

import os
from datetime import datetime, timedelta
from itsdangerous import URLSafeTimedSerializer

secret_key = os.getenv("AIW_FLASK_SECRET_KEY", None)
serializer = URLSafeTimedSerializer(secret_key)


async def generate_delete_token(expiration=None):
    if expiration is None:
        expiry = datetime.utcnow() + timedelta(minutes=5)
    else:
        expiry = expiration

    # Encrypt the expiry time using the secret key
    token = serializer.dumps(expiry.strftime("%Y-%m-%d %H:%M:%S"))

    return token


async def validate_delete_token(token, max_age=300):
    try:
        expiry_str = serializer.loads(token, max_age=max_age)
        expiry = datetime.strptime(expiry_str, "%Y-%m-%d %H:%M:%S")
        return expiry > datetime.utcnow()
    except:  # Catch any error related to token tampering or expiry
        return False
