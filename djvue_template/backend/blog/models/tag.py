"""Models of Blog."""
from django.core.validators import RegexValidator
from django.db import models


class Tag(models.Model):
    """Keyword assigned to a post."""

    name = models.CharField(
        blank=False,
        max_length=30,
        null=False,
        unique=True,
        )
    color = models.CharField(
        default='#3F7C82',
        max_length=7,
        validators=[RegexValidator(
            regex='^#.{6}$',
            message='Char has to be Hash key and a Hexadecimal code with 6 '
                    'char lenght. Example: #FFFFFF (one hash and 6 chars)',
            code='nomatch'
        )]
    )

    def check_color_format(self):
        """Check long and hexa code of color.

        Correct format requires seven characters. First '#' and six hex chars.
        """
        try:
            if(self.color and len(self.color) == 7 and self.color[0] == '#'):
                int(self.color[1:], 16)
                return True
        except ValueError:
            pass
        return False

    def __str__(self):
        """Printable object."""
        return self.name

    class Meta:
        """Metadata."""

        ordering = (
            'name',
        )
