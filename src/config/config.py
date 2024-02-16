from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnection:

    def __init__(self) -> None:
        host = "mysqldb"
        porta = 3306
        usuario = "root"
        senha = "ideia"
        banco_de_dados = "teste"    

        self.__connection_string = f"mysql+pymysql://{usuario}:{senha}@{host}:{porta}/{banco_de_dados}"
        self.session = None
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()