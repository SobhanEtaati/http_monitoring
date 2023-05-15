from django.db import models
from api.models import User

# Create your models here.
class Url(models.Model):
    url = models.CharField(primary_key=True, editable=False, max_length=500)
    email = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    is_successful = models.BooleanField(default=False)
    url_status_code = models.IntegerField

    if (url_status_code == 200):
        successful = True

    class Meta:
        constraints = [
            models.UniqueConstraint(
            fields=['email','url'], name = 'Urls_unique_value'
            )
        ]