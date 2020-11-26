import mongoengine as me


class Student(me.Document):
    fio = me.StringField(min_length=2, max_length=255, required=True)
    group = me.StringField(min_length=1, max_length=255, required=True)
    rating = me.ListField()
    curator = me.StringField(min_length=2, max_length=255, required=True, )
    email = me.StringField(min_length=2, max_length=255, required=True, )
    faculty = me.StringField(min_length=2, max_length=255, required=True)
    address = me.StringField(min_length=2, max_length=1000, required=True)
    created_at = me.DateTimeField()