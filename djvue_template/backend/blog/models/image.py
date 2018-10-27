"""Models of Blog."""
from django.db import models


class Image(models.Model):
    """Images of posts."""

    name = models.CharField(
        max_length=15,
        null=False,
        unique=True,
    )
    image = models.ImageField()

    def __str__(self):
        """Printable object."""
        return self.name

    class Meta:
        """Metadata."""

        ordering = (
            'name',
        )
