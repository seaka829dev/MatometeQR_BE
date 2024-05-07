from django.db import models
import uuid

# Create your models here.
class QRInfo(models.Model):
    id = models.UUIDField("ID", primary_key=True, default=uuid.uuid4, editable=False)
    title1 = models.TextField("タイトル1", max_length=255)
    title2 = models.TextField("タイトル2", max_length=255)
    title3 = models.TextField("タイトル3", max_length=255, null=True, blank=True)
    title4 = models.TextField("タイトル4", max_length=255, null=True, blank=True)
    title5 = models.TextField("タイトル5", max_length=255, null=True, blank=True)
    title6 = models.TextField("タイトル6", max_length=255, null=True, blank=True)
    title7 = models.TextField("タイトル7", max_length=255, null=True, blank=True)
    title8 = models.TextField("タイトル8", max_length=255, null=True, blank=True)
    title9 = models.TextField("タイトル9", max_length=255, null=True, blank=True)
    url1 = models.URLField("URL1")
    url2 = models.URLField("URL2")
    url3 = models.URLField("URL3", null=True, blank=True)
    url4 = models.URLField("URL4", null=True, blank=True)
    url5 = models.URLField("URL5", null=True, blank=True)
    url6 = models.URLField("URL6", null=True, blank=True)
    url7 = models.URLField("URL7", null=True, blank=True)
    url8 = models.URLField("URL8", null=True, blank=True)
    url9 = models.URLField("URL9", null=True, blank=True)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)