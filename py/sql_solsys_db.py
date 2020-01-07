"""Make sqlite database with data from obj_data.
WRT https://docs.sqlalchemy.org/en/13/orm/tutorial.html
"""

import datetime
from sqlalchemy import create_engine, Table, Column, Integer, String, Date, \
    BigInteger, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from object_data import obj_data

SQLITE_DB_FILENAME = 'solsysobjs.db'

Base = declarative_base()
engine = create_engine('sqlite:///'+SQLITE_DB_FILENAME, echo=True)


class Sobject(Base):
    __tablename__ = 'sobject'
    id = Column(Integer, primary_key=True)
    anumber = Column(Integer)
    name = Column(String(16))
    runame = Column(String(16))
    size = Column(Float)
    mass = Column(String(15)) # BigInteger
    discoverdate = Column(Date)
    classes = relationship("Classes", back_populates="sobject")
    filename = Column(String(16))

    def __repr__(self):
        return "Obj names: (%s) %s /%s/, size=%s, mass=%s, date=%s" % (
                            self.anumber, self.name, self.runame, self.size, self.mass, self.discoverdate)

    def __init__(self, anumber, name, runame, size, mass, discoverdate, classes, filename):
        if anumber:
            self.anumber = anumber
        self.name = name
        if runame:
            self.runame = runame
        self.size = size
        if mass:
            self.mass = mass
        if discoverdate and type(discoverdate) is str:
            self.discoverdate = datetime.datetime.strptime(discoverdate, "%d.%m.%Y").date()
        elif discoverdate and isinstance(discoverdate, datetime.date):
            self.discoverdate = discoverdate
        if type(classes) is str:
            classes = classes.split()
        self.classes = []
        for cl in classes:
            self.classes.append(Classes(clss=cl))
        if filename:
            self.filename = filename

class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    sobject_id = Column(Integer, ForeignKey('sobject.id'))
    clss = Column(String(10))
    sobject = relationship("Sobject", back_populates="classes")

    def __repr__(self):
        return "%s" % (self.clss)


Sobject.classes = relationship("Classes", order_by=Classes.id, back_populates="sobject")

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def extr_name(txt):
    intnum = lambda num: int(num.lstrip("(").rstrip(")"))
    DW = "(dwarf planet)"
    MO = "(moon)"
    num = None
    if DW in txt:
        num, name = txt.replace(DW, '').split()
        num = intnum(num)
    elif MO in txt:
        name = txt.replace(MO, '')
    elif "(" in txt:
        num = txt.split()[0]
        name = txt.strip(num)
        num = intnum(num)
    else:
        name = txt
    return num, name.strip()

for obj in obj_data:
    num, name = extr_name(obj[0])
    mass = obj[3]
    if mass == "None":
        mass = None
    if obj[4] == "None":
        date = None
    else:
        date = datetime.datetime.strptime(obj[4], "%d.%m.%Y").date()
    sobj = Sobject(anumber=num, name=name,
        runame=obj[1], size=obj[2], mass=str(mass),
        discoverdate=date, classes=[], filename=obj[-1])
    for cl in obj[-2]:
        sobj.classes.append(Classes(clss=cl))
    session.add(sobj)

if __name__ == '__main__':
    session.commit()
