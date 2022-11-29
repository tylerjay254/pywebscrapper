from pydantic import BaseModel , EmailStr
from sqlalchemy import orm
from sqlalchemy.sql.expression import false
from datetime import datetime
from typing import List, Optional

class ImageIn(BaseModel):
    ImageName : str              
    ImageUrl : str 
    searchQuery :str            
    source : str                 
  
    class Config:
        orm_mode = True
        
class Usereturn(ImageIn):
    dateAdded: datetime
    #cartegory: str
    
    class Config:
        orm_mode = True
        
class ImageProfile(ImageIn):  
    # image: LargeBinary               
    ImageName: str
    DateAdded : datetime
    ImageUrl: str
    source: str
    searchQuery:str  
    Cartegory:str  
    
    class Config:
        orm_mode = True
    


class ImageOut(BaseModel):
    id : int
    ImageName : str
    ImageUrl : str

    
    class Config:
        orm_mode = True
    
class ImageUpdate(BaseModel):
    ImageName : str
    Cartegory : str
    Subcartegory : str
    Subcartegory1 : str
    Subcartegory2 : str
    Subcartegory3 : str
    ImageType : str #anime #monochrome #instacolors
    Queries : list
    roles : str

    class Config:
        orm_mode = True
    
class ImageQuery(BaseModel):
    SearchQuery : str
    # save_search : bool
    
    class Config:
        orm_mode = True
    

    
class Token(BaseModel):
    access_token: str
    token_type : str
    
    class Config:
        orm_mode = True
        
        
class TokenData (BaseModel):
    id : Optional[str] = None
    

   
         
  
    
    