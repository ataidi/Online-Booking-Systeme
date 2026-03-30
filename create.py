from connections import Base, engine
from models import online

Base.metadata.create_all(bind=engine)