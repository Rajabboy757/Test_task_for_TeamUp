from django.db import models
import datetime
import base64


class Test(models.Model):
    login = models.CharField(max_length=10, unique=True, blank=True, null=True)
    IQ_result = models.SmallIntegerField(blank=True, null=True)
    IQ_test_pass_time = models.TimeField(blank=True, null=True)
    EQ_result = models.CharField(max_length=40, blank=True, null=True)
    EQ_test_pass_time = models.TimeField(blank=True, null=True)

    def set_login(self):
        number_generate = str(self.id).rjust(6, "0")

        self.login = base64.b32encode(bytes(number_generate, 'utf-8')).decode('utf-8').replace('=', '')

    def set_time(self, key):
        if key == 'IQ':
            self.IQ_test_pass_time = datetime.datetime.now()
        else:
            self.EQ_test_pass_time = datetime.datetime.now()

    def __str__(self):
        return self.login
