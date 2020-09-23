from datetime import datetime

from django.db import models

# Create your models here.

# from apps.users.models import UserLeavingMessage
from apps.users.models import BaseModel


class Category(models.Model):
    """
    漫画类别
    """
    CATEGORY_TYPE = (
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    category_name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
    category_code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
    category_desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "漫画类别"
        verbose_name_plural = verbose_name
        db_table = 'cartoon_category'

    def __str__(self):
        return self.category_name


class Caricature(BaseModel):
    """
    漫画
    """
    category = models.ForeignKey(Category, related_name='cartoon_category', null=True, blank=True, verbose_name="漫画类目",
                                 on_delete=models.CASCADE)
    cartoon_sn = models.CharField(max_length=50, verbose_name="漫画编号", primary_key=True)
    cartoon_name = models.CharField(max_length=50, verbose_name="漫画名称")
    cartoon_brief = models.TextField(max_length=300, verbose_name="漫画描述")
    cartoon_front_iamge = models.ImageField(upload_to="", null=True, blank=True, verbose_name="漫画封面图")
    cartoon_chapter = models.ImageField(default=0, verbose_name="章节数量")
    cartoon_tag = models.CharField(default="", verbose_name="漫画标签", max_length=10)
    # cartoon_comment = models.ForeignKey(UserLeavingMessage.message, related_name='cartoon_comment', null=True, blank=True, verbose_name="漫画评论",
    #                              on_delete=models.CASCADE)
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    is_new = models.BigIntegerField(default=False, verbose_name="是否为新上架")
    is_update = models.BooleanField(default=False, verbose_name="是否更新")
    is_pay = models.BooleanField(default=False, verbose_name="是否付费")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数量")
    # update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "漫画信息"
        verbose_name_plural = verbose_name
        db_table = 'cartoon'

    def __str__(self):
        return self.cartoon_name


class Chapter(BaseModel):
    """
    漫画章节
    """
    chapter_sn = models.CharField(max_length=100, verbose_name="章节", primary_key=True)
    cartoon_name = models.ForeignKey(Caricature, related_name='cartoon_chapter', verbose_name="漫画章节",
                                 on_delete=models.CASCADE)  #on_delete表示对应的外键数据被删除后，当前的数据应该被删除
    chapter_name = models.CharField(max_length=100, verbose_name=u"漫画章节名")
    # update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "漫画章节"
        verbose_name_plural = verbose_name
        db_table = 'cartoon_chapter'

    def __str__(self):
        return self.cartoon_name


class ChapterContent(BaseModel):
    """
    章节内容
    """
    chapter_name = models.ForeignKey(Chapter, related_name='chapter_content', verbose_name="章节内容",
                                 on_delete=models.CASCADE)
    content_name = models.CharField(max_length=100, verbose_name="章节名称")
    url = models.CharField(max_length=200, verbose_name=u"访问地址")

    class Meta:
        verbose_name = "章节内容"
        verbose_name_plural = verbose_name
        db_table = 'chapter_content'

    def __str__(self):
        return self.chapter_name


class CartoonResource(BaseModel):
    cartoon = models.ForeignKey(Caricature, on_delete=models.CASCADE, verbose_name="漫画")
    name = models.CharField(max_length=100, verbose_name=u"名称")
    file = models.FileField(max_length=200, upload_to="cartoon/resource/%Y/%m", verbose_name="下载地址")

    class Meta:
        verbose_name = "漫画资源"
        verbose_name_plural = verbose_name
        db_table = "cartoon_resource"


class Author(models.Model):
    """
    作者
    """
    author = models.CharField(max_length=20, verbose_name="作者姓名")
    gender = models.CharField(max_length=5, verbose_name="作者性别")
    author_own = models.ForeignKey(Caricature, related_name='author_cartoon', null=True, blank=True, verbose_name="作者版权漫画",
                                 on_delete=models.CASCADE)
    age = models.CharField(max_length=4, verbose_name="作者年龄")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "作者"
        verbose_name_plural = verbose_name
        db_table = 'cartoon_author'

    def __str__(self):
        return self.author


class Publisher(models.Model):
    """
    出版社
    """
    publisher_name = models.CharField(max_length=20, verbose_name="出版社")
    publisher_sn = models.CharField(max_length=50, verbose_name="出版社编号")
    publisher_own = models.ForeignKey(Caricature, related_name='publish_cartoon', null=True, blank=True, verbose_name="作者版权漫画",
                                 on_delete=models.CASCADE)
    publisher_address = models.CharField(max_length=100, verbose_name="出版社地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name
        db_table = 'cartoon_publisher'

    def __str__(self):
        return self.publisher_name

