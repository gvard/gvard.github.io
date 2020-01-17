import datetime
from sqlalchemy import create_engine, Table, Column, ForeignKey, \
    Integer, BigInteger, Float, String, Boolean, Date 
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from dates_data import events

SQLITE_DB_FILENAME = 'dates.sqlite'

Base = declarative_base()
engine = create_engine('sqlite:///'+SQLITE_DB_FILENAME, echo=True)


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    tag = Column(String(10))
    event = relationship("Event", back_populates="tags")

    def __repr__(self):
        return "%s" % (self.tag)


class Img(Base):
    __tablename__ = 'imgs'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'))
    img_url = Column(String(19))
    event = relationship("Event", back_populates="imgs")

    def __repr__(self):
        return "%s" % (self.img_url)


class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    name = Column(String(30))
    text = Column(String(800))
    # imgs = Column(String(19))
    # imgs = relationship("Img", back_populates="events")
    imgs = relationship("Img", order_by=Img.id, back_populates="event")
    # tags = relationship("Tag", back_populates="events")
    tags = relationship("Tag", order_by=Tag.id, back_populates="event")

    def __repr__(self):
        return "%s %s" % (self.date, self.name)

    # def __init__(self, date, name, text):

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


for event in events:
    date = datetime.datetime.strptime(event[1], "%d.%m.%Y").date()
    imgs = []
    for img_url in event[3]:
        imgs.append(Img(img_url=img_url))
    tags = []
    for tag in event[4]:
        tags.append(Tag(tag=tag))
    imgs
    event_obj = Event(date=date, name=event[0], text=event[2], imgs=imgs, tags=tags)

    session.add(event_obj)

if __name__ == '__main__':
    session.commit()
