from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField(unique=True,
                                     index=True)
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    is_active = fields.BooleanField(default=True)
    data = fields.JSONField(default=dict, null=True)

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
    created_at = fields.DatetimeField(null=True, auto_now_add=True)
    data = fields.JSONField(default=dict, null=True)

    class Meta:
        table = "sources"


class AnonimMessage(Model):
    id = fields.BigIntField(pk=True)
    sender = fields.ForeignKeyField('models.User',
                                    related_name='sent_messages',
                                    on_delete=fields.SET_NULL,
                                    null=True)
    recipient = fields.ForeignKeyField('models.User',
                                       related_name='received_messages',
                                       on_delete=fields.CASCADE)
    source = fields.ForeignKeyField('models.Source',
                                    related_name='messages',
                                    on_delete=fields.CASCADE)
    text = fields.TextField()
    created_at = fields.DatetimeField(null=True)
    msg_id_in_recipient_chat = fields.BigIntField(null=True)
    msg_id_in_sender_chat = fields.BigIntField(null=True)

    class Meta:
        table = 'anonymous_messages'


class SystemStats(Model):
    id = fields.BigIntField(pk=True)
    user_count = fields.BigIntField()
    