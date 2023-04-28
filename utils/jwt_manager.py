from jwt import encode, decode

def create_token(data: dict) -> str:
    token: str = encode(payload=data,key="Esto_va_ser_epico_papu",algorithm="HS256")
    return token
def validate_token(token:str) -> dict:
    data: dict = decode(token,key="Esto_va_ser_epico_papu",algorithms=['HS256'])
    return data


