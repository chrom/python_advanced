# Реализовать модель Пост (название, содержание, дата публикации, автор, кол-во просмотров, тег).
# Реализовать модель тег.
# Реализовать модель автор (имя, фамилия, кол-во публикаций автора).

import datetime
import mongoengine as me
me.connect(host='mongodb://test:test@localhost:27017/test')

class Author(me.Document):
    first_name = me.StringField(min_length=2, max_length=64, required=True)
    last_name = me.StringField(min_length=2, max_length=64)
    age = me.IntField(min_value=6, max_value=200)
    published_post = me.IntField(type=int)
    created_at = me.DateTimeField()

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)


class Tag(me.Document):
    tag = me.StringField(min_length=2, max_length=300, type=str, required=True)


class Post(me.Document):
    title = me.StringField(min_length=10, max_length=500, required=True)
    body = me.StringField(min_length=10, max_length=50000, required=True)
    show = me.IntField(type=int, default=0)
    created_at = me.DateTimeField()
    published_at = me.DateTimeField()
    author = me.fields.ListField(me.fields.ReferenceField(Author))
    tags = me.fields.ListField(me.fields.ReferenceField(Tag))

    def save(self, *args, **kwargs):
        self.created_at = datetime.datetime.now()
        super().save(*args, **kwargs)

# User.drop_collection()
# User.objects().delete()
