import jwt
from sqlalchemy.sql.coercions import expect

# Define header and payload
headers = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "username": "test_user",
    "email": "testuser@gmail.com",
    "is_active": False
}

# Secret key for signing
secret = "secret_1234"

# Encode JWT correctly
encoded_token = jwt.encode(payload, secret, algorithm="HS256", headers=headers)

# print("Generated JWT Token:")
# print(token)

try:
    decoded_token = jwt.decode(encoded_token, secret, algorithms=["HS256"])
    print(decoded_token)
except jwt.InvalidTokenError:
    print("Invalid token")
except jwt.DecodedError:
    print("Decoded Error")
