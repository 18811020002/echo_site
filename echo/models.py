# -*- coding=UTF-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Node(models.Model):
    type=(
        (U'总部','总部'),
        (U'分部','分部'),
    )
    node_name = models.CharField(verbose_name='节点名称', max_length=255)
    node_type = models.CharField(verbose_name='节点类型', max_length=50,choices=type)
    node_address = models.CharField(verbose_name='节点地址', max_length=255)
    node_contact = models.CharField(verbose_name='节点联系人', max_length=50,blank=True, null=True)
    node_signer = models.CharField(verbose_name='登记人',max_length=50, default='system')
    node_remarks = models.CharField(verbose_name='备注',max_length=255,blank=True)
    node_signtime = models.DateField(auto_now_add= True)
    
    def __str__(self):
        return self.node_name