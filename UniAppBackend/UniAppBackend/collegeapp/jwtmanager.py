import jwt
from datetime import datetime, timedelta

def getToken(data, role):
    encoded_jwt = jwt.encode({
                "email": data["email"],
                "password": data["password"],
                "role": role,
                "expires": (datetime.now() + timedelta(hours=1)).strftime("%m/%d/%Y, %H:%M:%S"),
                }, "secret", algorithm="HS256")

    return encoded_jwt

def verifyToken(token):
    try:
        decoded_jwt = jwt.decode(token, "secret", algorithms=["HS256"])
        expireDate = datetime.strptime(decoded_jwt["expires"], "%m/%d/%Y, %H:%M:%S")

        if(expireDate > datetime.now()):
            return True

        else:
            return False

    except jwt.exceptions.InvalidTokenError:
        return False

def refreshToken(token):
    try:
        decoded_jwt = jwt.decode(token, "secret", algorithms=["HS256"])
        newToken = getToken(decoded_jwt, decoded_jwt["role"])

        return newToken

    except jwt.exceptions.InvalidTokenError:
        return False