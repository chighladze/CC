from django.db import models


class Cdr(models.Model):
    recid = models.AutoField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    linkedid = models.CharField(max_length=32)
    destination = models.CharField(max_length=45)
    user_id = models.CharField(max_length=45)
    listen = models.IntegerField()
    reported = models.IntegerField()
    trunk = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'cdr'

    def __str__(self):
        return self.clid


class QueueLog(models.Model):
    time = models.CharField(max_length=32, blank=True, null=True)
    callid = models.CharField(max_length=64, blank=True, null=True)
    queuename = models.CharField(max_length=64, blank=True, null=True)
    uniqueid = models.CharField(max_length=45)
    agent = models.CharField(max_length=64, blank=True, null=True)
    event = models.CharField(max_length=32, blank=True, null=True)
    data = models.CharField(max_length=64, blank=True, null=True)
    data1 = models.CharField(max_length=64, blank=True, null=True)
    data2 = models.CharField(max_length=64, blank=True, null=True)
    data3 = models.CharField(max_length=64, blank=True, null=True)
    data4 = models.CharField(max_length=64, blank=True, null=True)
    data5 = models.CharField(max_length=64, blank=True, null=True)
    rating = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'queue_log'

    def __str__(self):
        return self.queuename


class Statelog(models.Model):
    datetime = models.DateTimeField(blank=True, null=True)
    exten = models.CharField(max_length=16, blank=True, null=True)
    state = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statelog'


    def __str__(self):
        return self.exten



