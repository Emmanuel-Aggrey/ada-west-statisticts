# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    positions = models.TextField(max_length=255, blank=False)
    date = models.DateField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.CharField(max_length=255, )
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    text = models.CharField(max_length=255, blank=True)
    # search = models.CharField(max_length=255)
    # search = models.CharField(max_length=255)
    # email was here
    deliver_to = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    telephone = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deliver_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True)
    end_date = models.DateTimeField()
    notes = models.CharField(max_length=255, blank=True)
