import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True) # echo=True: クエリのログを出力する
# engine = sqlalchemy.create_engine('sqlite:///../test_sqlite.db', echo=True)

username = 'admin'
password = 'password'
host = 'mysql'
port = '3306'
database = 'python_db'

engine = sqlalchemy.create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}", echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine) # セッションを作成
session = Session()

p1 = Person(name='Mike')
session.add(p1)

p2 = Person(name='test1')
session.add(p2)

p3 = Person(name='22222')
session.add(p3)

session.commit()

# update
p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

# delete
p5 = session.query(Person).filter_by(name='22222').first()
session.delete(p5)

session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)