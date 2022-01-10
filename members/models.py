from django.db import models

# Create your models here.

class Member(models.Model):
    TIER_CHOICES = [
        ('BRONZE','Bronze'),
        ('SILVER','Silver'),
        ('GOLD','Gold'),
        ('PLATINUM','Platinum'),
        ('DIAMOND','Diamond'),
        ('MASTER','Master'),
        ('GRAND_MASTER','GrandMaster'),
        ('CHALLENGER','Challenger'),
    ]

    LINE_CHOICES = [
        ('TOP','Top'),
        ('JUNGLE','Jungle'),
        ('MID','Mid'),
        ('ADC','Adc'),
        ('SUPPORT','Support'),
    ]

    nickname      = models.CharField(max_length=50)
    game_nickname = models.CharField(max_length=50)
    tier          = models.CharField(max_length=20,choices=TIER_CHOICES)
    line          = models.CharField(max_length=20, null=True,choices=LINE_CHOICES)

    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "members"

