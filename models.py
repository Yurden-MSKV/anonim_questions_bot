from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField(unique=True,
                                     index=True)
    created_at = fields.DatetimeField(null=True)

    class Meta:
        table = 'users'

    def __str__(self):
        return f"User #{self.id} ({self.telegram_id})"


class Source(Model):
    id = fields.BigIntField(pk=True)
    user = fields.ForeignKeyField('models.User',
                                  related_name='sources',
                                  on_delete=fields.CASCADE)
    name = fields.CharField(max_length=50)
    link_word = fields.CharField(max_length=50,
                                 unique=True)
    created_at = fields.DatetimeField(null=True)

    class Meta:
        table = "sources"


class AnonimMessage(Model):
    id = fields.BigIntField(pk=True)
    source = fields.ForeignKeyField('models.Source',
                                    related_name='messages',
                                    on_delete=fields.CASCADE)
    text = fields.TextField()
    created_at = fields.DatetimeField(null=True)

    class Meta:
        table = 'anonymous_messages'
