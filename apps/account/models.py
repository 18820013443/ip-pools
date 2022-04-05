import mongoengine
# from celery.signals import task_prerun
# Create your models here.


# @task_prerun.connect()
class Account(mongoengine.Document):
    username = mongoengine.StringField(required=True, unique=True)
    password = mongoengine.StringField(required=True)
    meta = {
        'collection': 'Account'
    }
