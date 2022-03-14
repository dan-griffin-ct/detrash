from django.db import models


class Zone(models.Model):
    
    LITTER_LEVEL_CHOICES = (
        ("1", "Not too bad"),
        ("2", "Kind of gross"),
        ("3", "This place needs some work"),
        ("4", "Dear Lord please help"),
        ("5", "Trashpocalypse"),
    )
    reported_by = models.CharField(max_length=256, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    city = models.CharField(max_length=256, null=False, blank=False)
    level_of_litter = models.CharField(max_length=100, null=False,
                                       blank=False,
                                       choices=LITTER_LEVEL_CHOICES,
                                       default="1")
    # NOTE
    # 
    # When attempting to create a new zone, use get_or_create and incremement this value
    # Check if update or create is a better option
    times_reported = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.zip_code}"
    
    def save(self, *args, **kwargs):
        self.times_reported +=1
        super(Zone, self).save(*args, **kwargs)

