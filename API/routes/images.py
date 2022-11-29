from fastapi import FastAPI ,status ,HTTPException ,Response ,Depends ,APIRouter
from typing import List, Optional
from typing import Optional
#import psycopg2
from sqlalchemy.sql import schema
from sqlalchemy.sql.elements import Null
from starlette.routing import Router 
import models.Images as models
import Databases.db as databases
from Databases.db import Base
from sqlalchemy.orm import Session
#from psycopg2.extras import RealDictCursor 
from time import sleep
from schema import images
from Databases.db import engine ,SessionLocal,get_db
import utils , Oauth2


Router = APIRouter(
    prefix="/images"
)


#get images in database

@Router.get("/",  status_code= status.HTTP_200_OK ,response_model= List[ images.ImageOut ] ) #admin path search by id/username
def get_user(db: Session = Depends(get_db)):
    Images = db.query(models.Images).all()
    if Images == [] or Images == None:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail="no images in database" )
    return Images 

# add images

@Router.post("/addImg",status_code= status.HTTP_201_CREATED , response_model= images.ImageOut) #users path TARGET homepage new user

def add_user( Image: images.ImageIn, db: Session = Depends(get_db)):
    image = models.Image(**Image.dict())
    db.add(image)
    db.commit()
    db.refresh(image)
    return image


# get one user by query / cartegory /subcartegory

@Router.get("/{cartegory}", status_code= status.HTTP_200_OK ,response_model= images.ImageOut) #admin path search by id/username
def get_user(cartegory: str,db: Session = Depends(get_db)):
    image = db.query(models.Image).filter(models.ImageCategory == cartegory).first()
    if image == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="cartegory not available")
    return image

# update image

@Router.put("/{id}" , status_code= status.HTTP_202_ACCEPTED  ) #admin path search by id/username

def update_user(id: int , image: images.ImageIn ,db: Session = Depends(get_db)):
    Image = db.query(models.Image).filter(models.Image.id == id)
    imageToUpdate = Image.first()
    if imageToUpdate == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="image not found")
    imageToUpdate.update(image.dict(), synchronize_session=False)
    db.commit()
    db.refresh(imageToUpdate)
    return imageToUpdate



# download through search engine

# what i need
# a function that can crawl images on google with a search term #
# a function that can download images from a search term
# and save the images to a database and the parent links 

Router.get()