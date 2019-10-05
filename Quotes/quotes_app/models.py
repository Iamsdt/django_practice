from django.db import models

# Create your models here.
class QuoteCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)

    quoteCategory = models.ForeignKey(
        "QuoteCategory",
        on_delete = models.CASCADE
    )

    def __str__(self):
        if len(self.quote) >= 30:
            return self.quote[:30]+" ..."
        else:
            return self.quote