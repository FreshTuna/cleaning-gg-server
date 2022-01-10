from django.db import models

# Create your models here.

class Match(models.Model):
    TEAM_CHOICIES = [
        ('RED','Red'),
        ('BLUE','Blue'),
    ]

    STATUS_CHOICES = [
        ('MATCHING','Matching'),
        ('PLAYING','Playing'),
        ('COMPLETE', 'Complete'),
        ('CANCLED','Cancled'),
    ]

    time     = models.IntegerField(null=True)
    start_at = models.DateTimeField(null=True)
    owner    = models.IntegerField(null=True)
    win_team = models.CharField(max_length=20, choices=TEAM_CHOICIES, null=True)
    status   = models.CharField(max_length=20, choices=STATUS_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "matches"