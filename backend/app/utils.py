from passlib.context import CryptContext
import traceback

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str):
    try:
        print(f"Password received: {repr(password)}")
        print(f"Password length: {len(password)}")
        return pwd_context.hash(password)
    except Exception as e:
        print("ERROR INSIDE hash_password()")
        traceback.print_exc()
        raise

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )