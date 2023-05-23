from django.db import models

class RegexQuery(models.Model):
    class MatchType(models.TextChoices):
        FULL = 'full', 'Full Match'
        FIRST = 'first', 'First Match'
    
    pattern = models.CharField(max_length=255)
    string = models.TextField()
    match_type = models.CharField(
        max_length=10,
        choices=MatchType.choices,
        default=MatchType.FIRST,
    )
