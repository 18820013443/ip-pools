import mongoengine

# Create your models here.


class Account(mongoengine.Document):
    username = mongoengine.StringField(required=True, unique=True)
    password = mongoengine.StringField(required=True)
    meta = {
        'collection': 'Account'
    }
