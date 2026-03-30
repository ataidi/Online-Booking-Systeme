from connections import Base, engine
from models import Online

Base.metadata.create_all(bind=engine)