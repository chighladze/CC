# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class cc_monthly_st(models.Model):
    created_date = models.DateTimeField(auto_now=True, verbose_name='Created Date')
    update_date = models.DateTimeField(auto_now_add=True)
    departament = models.CharField(max_length=128, blank=True, default='null')
    total_calls = models.IntegerField(null=True)
    answered_calls = models.IntegerField(null=True)
    month = models.CharField(max_length=32, blank=True, default='null')
    year = models.CharField(max_length=32, blank=True, default='null')
    service_level = models.CharField(max_length=32, blank=True, default='null')
    abandonment_rate = models.CharField(max_length=32, blank=True, default='null')
    response_time = models.CharField(max_length=32, blank=True, default='null')

    class Meta:

        verbose_name_plural = 'Calls'

    def __str__(self):
        return self.departament
