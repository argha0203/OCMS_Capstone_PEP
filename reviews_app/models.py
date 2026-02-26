from django.db import models
from django.conf import settings
from courses_app.models import Course


class Review(models.Model):

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="reviews"
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")
        indexes = [
            models.Index(fields=["student"]),
            models.Index(fields=["course"]),
        ]

    def __str__(self):
        return f"{self.student.email} - {self.course.title} ({self.rating})"