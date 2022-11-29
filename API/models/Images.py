import datetime
from sqlalchemy import  (Table, Column, Integer,String, MetaData,
                        ForeignKey, DateTime, Float, Boolean, Text, Date, Time, Enum, UniqueConstraint,LargeBinary)

from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign
from sqlalchemy.util.langhelpers import safe_reraise
from Databases.db import Base
from sqlalchemy.sql.sqltypes import Enum , TIMESTAMP 
from sqlalchemy.sql.expression import column, text



    
    
class Image(Base):
    __tablename__ = 'Images'
    id = Column(Integer,unique=True, primary_key=True)
    image_url = Column(String(50), unique=True, nullable=False)
    search_query = Column(String(50), nullable=False)
    image = Column(LargeBinary)

    # category = relationship("imageCartegory", cascade = "all delete" , backref = "Image")

    

class ImageCategory(Base):
    __tablename__ = 'cartegory'
    category_id = Column(Integer,unique = True, primary_key = True)
    category_name = Column(String(50),unique = True,null= False)