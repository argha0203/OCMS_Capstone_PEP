from django.db import models
from django.conf import settings


# ==========================
# Category Model
# ==========================
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["slug"]),
        ]

    def __str__(self):
        return self.name


# ==========================
# Course Model
# ==========================
class Course(models.Model):

    class Level(models.TextChoices):
        BEGINNER = "BEGINNER", "Beginner"
        INTERMEDIATE = "INTERMEDIATE", "Intermediate"
        ADVANCED = "ADVANCED", "Advanced"

    title = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    level = models.CharField(
        max_length=20,
        choices=Level.choices
    )

    instructor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="instructor_courses"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    is_published = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["category"]),
            models.Index(fields=["price"]),
            models.Index(fields=["level"]),
            models.Index(fields=["instructor"]),
        ]

    def __str__(self):
        return self.title


# ==========================
# Module Model
# ==========================
class Module(models.Model):

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="modules"
    )

    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ("course", "order")
        ordering = ["order"]

    def __str__(self):
        return f"{self.course.title} - {self.title}"


# ==========================
# Lecture Model
# ==========================
class Lecture(models.Model):

    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="lectures"
    )

    title = models.CharField(max_length=255)
    video_url = models.TextField()
    notes = models.TextField(blank=True)

    order = models.PositiveIntegerField()
    duration = models.PositiveIntegerField(help_text="Duration in seconds")

    class Meta:
        unique_together = ("module", "order")
        ordering = ["order"]
        indexes = [
            models.Index(fields=["module"]),
        ]

    def __str__(self):
        return self.title