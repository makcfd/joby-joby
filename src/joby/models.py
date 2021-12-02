from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50,
                            unique=True)
    slug = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '_').lower()
        super().save(*args, **kwargs)


class DevLanguage(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name="Programming language",
                            unique=True)
    slug = models.CharField(max_length=50,
                            blank=True,
                            unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(' ', '_').lower()
        super().save(*args, **kwargs)


class Vacancy(models.Model):

    url = models.URLField(unique=True)
    position_name = models.CharField(max_length=250)
    description = models.TextField(max_length=900)
    company = models.CharField(max_length=250)

    timetamp = models.DateTimeField(auto_now_add=True)

    city = models.ForeignKey('City',
                             on_delete = models.CASCADE)
    dev_langauge = models.ForeignKey('DevLanguage',
                                     on_delete = models.CASCADE)

    def __str__(self):
        return self.position_name


