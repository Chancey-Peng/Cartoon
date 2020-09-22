from django.db import models

# Create your models here.


from datetime import datetime


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


class Caricature(models.Model):
    """
    漫画
    """
    category = models.ForeignKey(Category, related_name='cartoon_category', null=True, blank=True, verbose_name="漫画类目",
                                 on_delete=models.CASCADE)
    cartoon_sn = models.CharField(max_length=50, verbose_name="漫画编号", primary_key=True)
    cartoon_name = models.CharField(max_length=100, verbose_name="漫画名称")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数量")
    cartoon_brief = models.TextField(max_length=500, verbose_name="漫画描述")
    cartoon_front_iamge = models.ImageField(upload_to="", null=True, blank=True, verbose_name="漫画封面图")
    is_hot = models.BooleanField(default=False, verbose_name="是否热门")
    is_new = models.BigIntegerField(default=False, verbose_name="是否为新上架")
    is_update = models.BooleanField(default=False, verbose_name="是否更新")
    is_pay = models.BooleanField(default=False, verbose_name="是否付费")
    update_time = models.DateTimeField(default=datetime.now, verbose_name="更新时间")

    class Meta:
        verbose_name = "漫画"
        verbose_name_plural = verbose_name
        db_table = 'cartoon'

    def __str__(self):
        return self.cartoon_name


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

