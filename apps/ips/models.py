import mongoengine

# Create your models here.


class IpPools(mongoengine.Document):
    ip = mongoengine.StringField()
    port = mongoengine.IntField()
    protocol = mongoengine.IntField()
    nick_type = mongoengine.IntField()
    speed = mongoengine.FloatField()
    area = mongoengine.StringField()
    score = mongoengine.IntField()
    disable_domains = mongoengine.ListField()
    meta = {
        'collection': 'IpPools'
    }
