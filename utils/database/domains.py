import mongoengine


class Domain(mongoengine.EmbeddedDocument):
    name = mongoengine.StringField(required=True)
    rhash = mongoengine.StringField(required=True)

