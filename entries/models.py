from django.db import models

# Create your models here.

class Entry(models.Model):
    TEAM_CHOICIES = [
        ('RED','Red'),
        ('BLUE','Blue'),
    ]

    match_id  = models.IntegerField()
    member    = models.ForeignKey("members.Member", on_delete=models.CASCADE)
    leader_yn = models.BooleanField(default=False)
    team      = models.CharField(max_length=20, choices=TEAM_CHOICIES, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "entries"

    