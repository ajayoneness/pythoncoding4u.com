from django.db import models




class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.designation}"
