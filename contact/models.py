from django.db import models

# Create your models here.


class Contact(models.Model):

    class Meta:
        verbose_name = 'Contact'

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=2000, null=False, blank=False)

    def __str__(self):
        return self.name


class NewsletterSubscribe(models.Model):

    class Meta:
        verbose_name = 'Newsletter Subscribe'

    email = models.EmailField(max_length=50, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
