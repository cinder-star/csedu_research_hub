from django.db import models

from accounts.models import User
# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"
    name = models.CharField(max_length=32, null=False, blank=False, unique=True)
    author = models.ForeignKey(User, to_field="registration_number", null=False, blank=False, on_delete=models.CASCADE)
    date = models.DateTimeField(["%Y-%m-%d"])

class Tag(models.Model):
    class Meta:
        db_table = "tag"
    name = models.TextField(null=False)

class ArticleTag(models.Model):
    class Meta:
        db_table = "article_tag"
        unique_together = [["article", "tag"],]
    article = models.OneToOneField(Article, to_field="id", on_delete=models.CASCADE)
    tag = models.OneToOneField(Tag, to_field="id", on_delete=models.CASCADE)

