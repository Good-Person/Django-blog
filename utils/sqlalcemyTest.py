# coding=utf8

from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'
PORT = 3306
USER = 'huige'
PASSWORD = 'huige123,./'
DATABASE = 'test_server'

db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USER, PASSWORD, HOSTNAME, PORT, DATABASE)

engine = create_engine(db_url)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Areas(Base):

    __tablename__ = 'areas'

    id = Column(Integer, primary_key=True)
    atitle = Column(String(10))
    pid = Column(Integer)

    def __repr__(self):
        return self.atitle.encode('utf8')


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    mobile = Column(String(11))

    def __repr__(self):
        return self.name.encode('utf8')


class Caiwu(Base):
    __tablename__ = 'caiwu'
    id = Column(Integer, primary_key=True)
    atitle = Column(String(10))

    def __repr__(self):
        return self.atitle.encode('utf8')


class Data(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    info = Column(String(10))
    create_time = Column(String(10))
    user_id = Column(Integer, ForeignKey('user.id'))
    caiwu_id = Column(Integer, ForeignKey('caiwu.id'))
    user = relationship("User", backref=backref('data', order_by=id))
    caiwu = relationship("Caiwu", backref=backref('data', order_by=id))

    def __repr__(self):
        return self.info.encode('utf8')




if __name__ == '__main__':
    # connect = engine.connect()
    # result = connect.execute('select * from areas')
    # print result.fetchall()

    # 创建所有数据表
    Base.metadata.create_all(engine)

    session = Session()
    result = session.query(Caiwu).all()
    for item in result:
        print item
