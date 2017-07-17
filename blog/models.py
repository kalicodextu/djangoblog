# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# 增加元组用来设置消息枚举类型项
KIND_CHOICES = (
    ('python技术', 'python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体咨询', '文体谘询'),
    ('个人心情', '个人心情'),
    ('其它', '其它'),
)


# Create your models here.
class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=21, default = '匿名')
    # 修改kind的定义，加入choices参数
    kind = models.CharField(max_length=21, choices = KIND_CHOICES, default = KIND_CHOICES[0])
