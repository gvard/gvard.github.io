import datetime
import json

from sqlalchemy import create_engine, Table, Column, ForeignKey, \
    Integer, BigInteger, Float, String, Boolean, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATES_JSON_FILENAME = 'astrocosm.json'
DATES_JSON_PTH = '../dates/'
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
    img_url = Column(String)
    img_filename = Column(String(19))
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

with open(DATES_JSON_PTH + DATES_JSON_FILENAME, 'rb') as JSON_BIN:
    EVENTS = json.load(JSON_BIN)

for event_daymon in EVENTS.keys():
    for event in EVENTS[event_daymon]:
        date = datetime.datetime.strptime(event_daymon + '.' + event['year'], "%d.%m.%Y").date()
        imgs = []
        if 'http' in event['img']:
            imgs.append(Img(img_url=event['img']))
        else:
            imgs.append(Img(img_filename=event['img']))
        tags = []
        event_tags = event.get('tags')
        if event_tags:
            for tag in event_tags.split():
                tags.append(Tag(tag=tag))
        event_obj = Event(date=date, name=event['slug'], text=event['desc'], imgs=imgs, tags=tags)
        session.add(event_obj)

if __name__ == '__main__':
    session.commit()
