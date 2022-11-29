from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str ):
    return pwd_context.hash(password)

def verify (plainpwd , hashedpwd):
    verify = pwd_context.verify(plainpwd, hashedpwd)
    return verify
    
    