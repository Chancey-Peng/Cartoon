from datetime import datetime

from django.db import models

from organizations.models import CartoonAuthor


class Cartoon(models.Model):
    """
    漫画
    """
    cartoon_sn = models.CharField(max_length=30, verbose_name="漫画编号", primary_key=True)
    cartoon_name = models.CharField(max_length=50, verbose_name="漫画名称")
    author = models.ForeignKey(CartoonAuthor, related_name='cartoon_author', on_delete=models.CASCADE, verbose_name="漫画作者")
    cartoon_brief = models.TextField(max_length=300, verbose_name="漫画描述")
    cartoon_front_image = models.ImageField(upload_to="", null=True, blank=True, verbose_name="漫画封面图")
    cartoon_chapter = models.ImageField(default=0, verbose_name="章节数量")
    cartoon_tag = models.CharField(default="", verbose_name="漫画标签", max_length=10)
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    is_new = models.BigIntegerField(default=False, verbose_name="是否为新上架")
    is_pay = models.BooleanField(default=False, verbose_name="是否付费")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数量")
    is_state = models.CharField(max_length=10, choices=(("serial", "连载中"), ("end", "已完结")), default="serial",
                                verbose_name="漫画状态")
    start_time = models.DateTimeField(default=datetime.now, verbose_name="开始时间")

    class Meta:
        verbose_name = "漫画信息"
        verbose_name_plural = verbose_name
        db_table = 'cartoon'

    def __str__(self):
        return self.cartoon_name


class Chapter(models.Model):
    """
    漫画章节
    """
    chapter_sn = models.CharField(max_length=100, verbose_name="章节", primary_key=True)
    cartoon_name = models.ForeignKey(Cartoon, verbose_name="漫画章节", on_delete=models.CASCADE)  #on_delete表示对应的外键数据被删除后，当前的数据应该被删除
    chapter_name = models.CharField(max_length=100, verbose_name=u"漫画章节名")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "漫画章节"
        verbose_name_plural = verbose_name
        db_table = 'cartoon_chapter'

    def __str__(self):
        return self.cartoon_name


class ChapterContent(models.Model):
    """
    章节内容
    """
    chapter_name = models.ForeignKey(Chapter, related_name='chapter_content', on_delete=models.CASCADE,
                                     verbose_name="章节内容")
    content_name = models.CharField(max_length=100, verbose_name="章节名称")
    url = models.CharField(max_length=200, verbose_name=u"访问地址")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "章节内容"
        verbose_name_plural = verbose_name
        db_table = 'chapter_content'

    def __str__(self):
        return self.chapter_name


class CartoonResource(models.Model):
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE, verbose_name="漫画")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    file = models.FileField(max_length=200, upload_to="cartoon/resource/%Y/%m", verbose_name="下载地址")
    upload_time = models.DateTimeField(default=datetime.now, verbose_name="上传时间")

    class Meta:
        verbose_name = "漫画资源"
        verbose_name_plural = verbose_name
        db_table = "cartoon_resource"
