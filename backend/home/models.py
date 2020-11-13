from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    a1233455 = models.CharField(
        blank=True,
        max_length=150,
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    body = models.TextField()
    hgjhgjhg = models.BigIntegerField(
        null=True,
        blank=True,
    )
    jhgjhghjg = models.BigIntegerField(
        null=True,
        blank=True,
    )
    hjjgjhgjgh = models.BigIntegerField(
        null=True,
        blank=True,
    )
    jhgjhgjgjhgfhjg = models.BigIntegerField(
        null=True,
        blank=True,
    )
    ytrtyrytryr = models.BigIntegerField(
        null=True,
        blank=True,
    )
    hgfhfgfghfhg = models.BigIntegerField(
        null=True,
        blank=True,
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
