from jose import jwt ,JWTError 
from datetime import datetime , timedelta
import pywebscrapper.API.schema.images as userschema
from sqlalchemy.orm import Session
import Databases.db as database
import models.Images as models
from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# secret key
#algorithm = 'HS256'
#token expiration time

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "YRpWWw6BAX1nWFIYaJvs7c5iN8cBBQr5"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# create token

def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    if expires_delta:
        expire = timedelta(minutes=expires_delta)
        return f" 'Detail': 'token expired' "
    else:
        expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": datetime.utcnow() + expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)
    return encoded_jwt

#verify token

def verify_token(token: str , credentials_exeption):
    
    print('starting verify token')
    try:
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        id: str = payload.get("user_id")
        
        if id is None: 
            raise credentials_exeption
        token_data = userschema.TokenData(id=id)
        print('done verifying token')
    except JWTError:
        raise credentials_exeption
    
    return token_data

#get_current_user

def get_current_user(Token: str = Depends(oauth2_scheme),db: Session = Depends(database.get_db)):
    print('starting get current user')
    credentials_exeption = HTTPException(
        detail="Could not validate credentials",headers={"WWW-Authenticate": "Bearer"},)
    token = verify_token( Token , credentials_exeption)
    
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
        
    return user