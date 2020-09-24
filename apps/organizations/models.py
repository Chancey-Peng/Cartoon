from datetime import datetime

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"地区")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = verbose_name


class CartoonAuthor(models.Model):
    """
    作者
    """
    author = models.CharField(max_length=20, verbose_name="作者姓名")
    gender = models.CharField(max_length=5, verbose_name="作者性别")
    author_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="作者所在地区")
    author_avatar = models.ImageField(max_length=100, default="", upload_to="author/%Y/%m", verbose_name="作者头像")
    author_age = models.CharField(max_length=4, verbose_name="作者年龄")
    like_nums = models.IntegerField(default=0, verbose_name="作者热度")
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
    author_publisher = models.ForeignKey(CartoonAuthor, on_delete=models.CASCADE, verbose_name="作者所在出版社")
    publisher_address = models.CharField(max_length=100, verbose_name="出版社地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "出版社"
        verbose_name_plural = verbose_name
        db_table = 'cartoon_publisher'

    def __str__(self):
        return self.publisher_name
