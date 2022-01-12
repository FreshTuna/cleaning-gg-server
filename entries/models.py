from django.db import models

# Create your models here.

class Entry(models.Model):
    match_id  = models.IntegerField()
    member_id = models.IntegerField()
    leader_yn = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "entries"

    