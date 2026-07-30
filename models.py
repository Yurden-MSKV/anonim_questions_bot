from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.BigIntField(pk=True)
    telegram_id = fields.BigIntField(unique=True, index=True)
    created_at = fields.DatetimeField(null=True)

    class Meta:
        table = 'users'

    def __str__(self):
        return f"User #{self.id} ({self.telegram_id})"