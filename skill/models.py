from xml.dom.minidom import Identified
from django.db import models

# Create your models here.
class member(models.Model):
    id=models.BigAutoField(primary_key=True,db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    # size=models.CharField(max_length=100,null=True,blank=True)
    # pic = models.ImageField(
    #     storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    name=models.CharField(max_length=200, null=True,blank=True,)
    post=models.CharField(max_length=200, null=True,blank=True,)

    # description=models.TextField(null=True,blank=True)
    # lang=models.ForeignKey(
    #     Lang, null=True, verbose_name="language21", on_delete=models.SET_NULL, db_index=True)
    # attr1=models.CharField(max_length=200, null=True,blank=True,)
    # attr2=models.CharField(max_length=200, null=True,blank=True, )
    # attr3=models.CharField(max_length=200, null=True,blank=True, )
    # attr4=models.CharField(max_length=200, null=True,blank=True, )
class skills(models.Model):
    id=models.BigAutoField(primary_key=True,db_index=True)
    keydata=models.CharField(max_length=200, null=True, db_index=True)
    # size=models.CharField(max_length=100,null=True,blank=True)
    # pic = models.ImageField(
    #     storage=OverwriteStorage(), upload_to='courses',null=True,blank=True)
    skill=models.CharField(max_length=200, null=True,blank=True,)
    member =models.ForeignKey(
        member, null=True, verbose_name="member name", on_delete=models.SET_NULL, db_index=True)
