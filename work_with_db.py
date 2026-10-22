from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()


class Pep(Base):
    __tablename__ = 'pep'
    id = Column(Integer, primary_key=True)
    pep_number = Column(Integer, unique=True)
    name = Column(String(200))
    status = Column(String(20))


if __name__ == '__main__':
    engine = create_engine('sqlite:///sqlite.db', echo=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        if session.query(Pep).count() == 0:
            session.add_all([
                Pep(pep_number=8, name='Style Guide for Python Code', status='Active'),
                Pep(pep_number=20, name='The Zen of Python', status='Active'),
                Pep(pep_number=216, name='Docstring Format', status='Rejected'),
            ])
            session.commit()
