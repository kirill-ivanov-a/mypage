import enum
from datetime import datetime
from flask_security import UserMixin, RoleMixin
from sqlalchemy import Column, Integer, String, DateTime, Text, Enum, ForeignKey, Table, Boolean
from sqlalchemy.orm import relationship, backref
from database import Base, db_session

roles_users = Table('roles_users',
                    Base.metadata,
                    Column('user_id', Integer, ForeignKey('user.id')),
                    Column('role_id', Integer, ForeignKey('role.id')))


class ModelBase:
    def save(self):
        db_session.add(self)
        db_session.commit()


class User(Base, UserMixin, ModelBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(255))
    active = Column(Boolean)
    roles = relationship('Role', secondary=roles_users, backref=backref('user'), lazy='dynamic')


class Role(Base, RoleMixin, ModelBase):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)


class VKUser(Base, ModelBase):
    __tablename__ = 'vkuser'

    id = Column(Integer, primary_key=True)
    vk_uid = Column(Integer, nullable=False)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    preferred_username = Column(String(255), nullable=True, unique=True)
    picture_url = Column(String(512), nullable=True)
    gender = Column(String(255), nullable=True)
    questions = relationship('Question')

    def __init__(self, vk_uid=None, first_name=None, last_name=None,
                 preferred_username=None, picture_url=None, gender=None):
        self.vk_uid = vk_uid
        self.first_name = first_name
        self.last_name = last_name
        self.preferred_username = preferred_username
        self.picture_url = picture_url
        self.gender = gender

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'

    def __str__(self):
        return self.__repr__()


class CategoryEnum(enum.Enum):
    CAREER = 0
    EDUCATION = 1
    PERSONAL = 2
    OTHER = 3

    def get_ru_name(self):
        return {
            0: 'Карьера',
            1: 'Образование',
            2: 'Личное',
            3: 'Другое'
        }[self.value]

    @classmethod
    def choices(cls):
        return [(member.value, member.get_ru_name()) for member in cls.__members__.values()]

    @classmethod
    def coerce(cls, item):
        return cls(int(item)) if not isinstance(item, cls) else item


class Question(Base, ModelBase):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    vkuser_id = Column('vkuser_id', Integer, ForeignKey('vkuser.id'), nullable=True)
    publication_date = Column(DateTime, default=datetime.utcnow)
    category = Column(Enum(CategoryEnum), nullable=False)
    question = Column(String(255), nullable=False)
    detailed_description = Column(Text, nullable=True)
    answer = relationship("Answer", uselist=False, back_populates="question")

    def __init__(self, vkuser_id, topic, question, detailed_description):
        self.vkuser_id = vkuser_id
        self.category = topic
        self.question = question
        self.detailed_description = detailed_description

    def __repr__(self):
        return f'<Question: {self.question}; ' \
               f'category: {self.category}; ' \
               f'{self.question}; ' \
               f'deatailed: {self.detailed_description}>'

    def __str__(self):
        return self.__repr__()


class Answer(Base, ModelBase):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('question.id'))
    question = relationship("Question", back_populates="answer")
    answer = Column(Text, nullable=False)
    publication_date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Answer: {self.answer}; question: {self.question_id} >'

    def __str__(self):
        return self.__repr__()
