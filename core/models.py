from django.db import models

from .validators import validate_file_extension


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/', validators=[validate_file_extension])
    cover = models.ImageField(upload_to='books/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)


class UploadFiles(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.file

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
