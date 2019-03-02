from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# ベースモデルを作成
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)


# エンジンを作成
engine = create_engine('sqlite:///db/sql_training.sqlite')

# DBと通信するセッションオブジェクトの作成
# sqlite3におけるconnectionオブジェクトに近い
Session = sessionmaker(bind=engine)
session = Session()

for user in session.query(User).all():
    print(user.id, user.username)
