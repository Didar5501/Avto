from django.db import models

import uuid


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)

class mcfcarbrand(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100)
    idbs = models.IntegerField()
    country = models.ForeignKey('country', on_delete=models.CASCADE)
    creationdate = models.DateField()
    creationauthor = models.ForeignKey(User, related_name='created_mcfcarbrands', on_delete=models.CASCADE)
    changedate = models.DateField()
    changeauthor = models.ForeignKey(User, related_name='changed_mcfcarbrands', on_delete=models.CASCADE)
    mcfcode = models.CharField(max_length=100, default='id')


class mcfcarmodel(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100)
    carbrand = models.ForeignKey(mcfcarbrand, on_delete=models.CASCADE)
    idbs = models.IntegerField()
    creationdate = models.DateField()
    creationauthor = models.ForeignKey(User, related_name='created_mcfcarmodels', on_delete=models.CASCADE)
    changedate = models.DateField()
    changeauthor = models.ForeignKey(User, related_name='changed_mcfcarmodels', on_delete=models.CASCADE)
    mcfcode = models.CharField(max_length=100, default='id')



class mcfcarcolor(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.UUIDField(default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=100)
    idbs = models.IntegerField()
    creationdate = models.DateField()
    creationauthor = models.ForeignKey(User, related_name='created_mcfcarcolors', on_delete=models.CASCADE)
    changedate = models.DateField()
    changeauthor = models.ForeignKey(User, related_name='changed_mcfcarcolors', on_delete=models.CASCADE)
    isdeleted = models.BooleanField()



class country(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

 

class z_avtomodel(models.Model):
    BrandID = models.ForeignKey('z_avtobrand', on_delete=models.CASCADE)
    ModelID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)



class z_avtobrand(models.Model):
    BrandID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)



class z_avtocolor(models.Model):
    ColorID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)

  
