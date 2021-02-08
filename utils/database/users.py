import mongoengine

from utils.database.domains import Domain


class User(mongoengine.Document):
    user_id = mongoengine.LongField(required=True)

    domains = mongoengine.EmbeddedDocumentListField(Domain)

    meta = {
        'db_alias': 'core',
        'collection': 'users'
    }
