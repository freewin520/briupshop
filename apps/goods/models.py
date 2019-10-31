from django.db import models

# Create your models here.
#商品分类信息表
class GoodsType(models.Model):
    name = models.CharField(max_length=20,verbose_name='分类名称')
    level = models.IntegerField(verbose_name='分类级别')
    uper_type = models.ForeignKey('self',on_delete=models.CASCADE,verbose_name='上级编号',null=True,blank=True,related_name='son')

    class Meta():
        verbose_name = '商品分类信息表'

    def __str__(self):
        return self.name

#商品信息表
class Goods(models.Model):
    name = models.CharField(max_length=20,verbose_name='商品名称')
    original_price = models.FloatField(verbose_name='原价')
    actual_price = models.FloatField(verbose_name='现价')
    freight = models.FloatField(verbose_name='运费')
    image = models.ImageField(upload_to='uploads/goods/%Y/%m/%d/',verbose_name='商品图片')
    detail =models.CharField(max_length=200,verbose_name='说明')
    sale_nums = models.IntegerField(verbose_name='销量')
    all_nums = models.IntegerField(verbose_name='库存')
    view_nums = models.IntegerField(verbose_name='浏览量')
    favor_nums = models.IntegerField(verbose_name='收藏数')
    comments_nums = models.IntegerField(verbose_name='评论数')
    created_time = models.DateTimeField(verbose_name='录入时间')
    one_typename = models.ForeignKey('GoodsType', on_delete=models.CASCADE,related_name='one',null=True,blank=True)
    two_typename = models.ForeignKey('GoodsType', on_delete=models.CASCADE, related_name='two', null=True, blank=True)
    three_typename = models.ForeignKey('GoodsType', on_delete=models.CASCADE, related_name='three', null=True, blank=True)

    class Meta():
        verbose_name = '商品信息表'

    def __str__(self):
        return self.name
class GoodsDisplayFiles(models.Model):
    goods = models.ForeignKey('Goods', on_delete=models.CASCADE)
    text = models.CharField(max_length=255,verbose_name='说明')
    goods_file = models.FileField(upload_to='uploads/goods/%Y/%m/%d',verbose_name='展示图')
    list = GoodsType.objects.all()#[<>,<>]



    class Meta():
        verbose_name = '商品展示文件信息表'

    def __str__(self):
        return self.text