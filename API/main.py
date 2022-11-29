from fastapi import FastAPI ,status ,HTTPException ,Response ,Depends,APIRouter
from typing import List, Optional
from typing import Optional
#import psycopg2
from sqlalchemy.sql import schema
from sqlalchemy.sql.elements import Null 
import models.Images as models
import Databases.db as databases
from Databases.db import Base
from sqlalchemy.orm import Session
#from psycopg2.extras import RealDictCursor 
from time import sleep
from schema import product , inventory ,User , store
from Databases.db import engine ,SessionLocal
import utils
from routes import users , authentication 
import Oauth2

models.Base.metadata.create_all(bind=engine)

#schemas

app = FastAPI(title='pywebscrapper', description='web scrapping API ,reusable for other projects ', version='0.1')



#ROUTERS
app.include_router(users.Router)
app.include_router(authentication.router)


