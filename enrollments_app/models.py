from django.db import models
from django.conf import settings
from courses_app.models import Course, Lecture


# ==========================
# Enrollment Model
# ==========================
class Enrollment(models.Model):

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"

    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course")
        indexes = [
            models.Index(fields=["student"]),
            models.Index(fields=["course"]),
        ]

    def __str__(self):
        return f"{self.student.email} - {self.course.title}"


# ==========================
# Lecture Progress Model
# ==========================
class LectureProgress(models.Model):

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="lecture_progress"
    )

    lecture = models.ForeignKey(
        Lecture,
        on_delete=models.CASCADE,
        related_name="progress_records"
    )

    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["enrollment"]),
            models.Index(fields=["lecture"]),
        ]

    def __str__(self):
        return f"{self.enrollment} - {self.lecture.title}"