from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_solsys_db import Sobject, Classes

SQLITE_DB_FILENAME = 'solsysobjs.db'
engine = create_engine('sqlite:///'+SQLITE_DB_FILENAME, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

query = session.query(Sobject).filter(Sobject.id == Classes.sobject_id).all()
for q in query:
    if q.anumber:
        print(f"({q.anumber}) ", end="")
    print(f"{q.name} {q.runame} {q.size} км, {q.mass} кг, {q.classes}", end=" ")
    if q.discoverdate:
        print(q.discoverdate.strftime("%d.%m.%Y"))
    else:
        print()
print(len(query), "objects")
