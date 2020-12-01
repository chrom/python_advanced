# 2) Создать модуль, который будет заполнять базу данных
# случайными валидными значениями (минимум 100 студентов).

import mongoengine as me
from faker import Faker
import random
from models import Author, Tag, Post

fake: Faker = Faker()
me.connect(host='mongodb://test:test@localhost:27017/test')

authors = []
tags = []


def generate_author(qty: int = 40):
    Author.drop_collection()
    for i in range(qty):
        author = Author(first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        age=random.randint(6, 120),
                        published_post=random.randint(0, 500),
                        )
        author.save()
        authors.append(author)


def generate_tag(qty: int = 20):
    Tag.drop_collection()
    for i in range(qty):
        tag = Tag(tag=fake.catch_phrase())
        tag.save()
        tags.append(tag)


def generate_post(qty: int = 200):
    Post.drop_collection()
    for i in range(qty):
        tag = Post(title=fake.bs(),
                   body=fake.paragraph(nb_sentences=5),
                   author=random.sample(authors, random.randint(1, 3)),
                   show=random.randint(0, 5000),
                   published_at=fake.date(),
                   tags=random.sample(tags, random.randint(0, 10))
                   )
        tag.save()


if __name__ == '__main__':
    generate_author()
    generate_tag()
    generate_post()
