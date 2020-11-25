import mongoengine as me

me.connect(host='mongodb://test:test@localhost:27017/test')


class User(me.Document):
    first_name = me.StringField(min_length=2, max_length=255, required=True)
    last_name = me.StringField(min_length=2, max_length=255)
    interest = me.ListField()
    age = me.IntField(min_value=0, max_value=200)


if __name__ == '__main__':
    user = User(first_name='John', interest=['Spotr', 'Programming'], age=20)
    user.save()
