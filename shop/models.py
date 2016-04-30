from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, UserManager

class ManufacturerCountry(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return u'%s' % self.name


class producer(models.Model):
    name = models.CharField(max_length = 100)
    def __str__(self):
        return u'%s' % self.name


class product(models.Model):
    name = models.CharField(max_length = 100, null = True )
    view = models.ImageField(null = True, blank = True)
    description = models.TextField(blank=True,null = True)
    price = models.IntegerField(null = True)
    producer = models.ForeignKey(producer, related_name = '+',blank = True, null = True)
    manufacturerCountry = models.ForeignKey(ManufacturerCountry, related_name = '+', null = True, blank = True)
    like_users = models.ManyToManyField('auth.User', related_name='user_likes', blank=True)
    comments = models.ManyToManyField('auth.User', through='comment', related_name='user_comments')
    def __str__(self):
        return u'%s' % self.name

class category(models.Model):
    name = models.CharField(max_length=100, null = True)
    products = models.ManyToManyField(product, blank=True)
    description=models.TextField(max_length=1000, null=True, blank=True)
    logo=models.ImageField(blank=True)
    def __str__(self):
        return u'%s' % self.name

class order (models.Model):
    products = models.ManyToManyField(product)
    user = models.ForeignKey('auth.User', related_name = '+', null = True)
    created_date = models.DateTimeField(
            default=timezone.now)
    PAYMENT_CHOICES = (
    (u'Card', u'Card'),
    (u'Cash', u'Cash'),
    )
    type_of_payment = models.CharField(max_length=4, choices=PAYMENT_CHOICES, null = True, blank=True)
    delivery_address = models.TextField(null = True)
    def __str__(self):
        return u'%s %s' % (self.user, self.id)


class comment(models.Model):
    user = models.ForeignKey('auth.User', related_name = '+', blank = True, null = True)
    product = models.ForeignKey(product, blank=True, null=True)
    #date_time = models.DateTimeField(auto_now=True)
    text = models.TextField(max_length=10000)
    def __str__(self):
        return u'%s is comment " %s "' % (self.user.username, self.text)


class userProfile(User):
    favoriteMark = models.CharField(max_length = 100, blank=True, null=True)
    objects = UserManager()