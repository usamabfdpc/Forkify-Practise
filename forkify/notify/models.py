from typing import Iterable, Optional
from django.db import models
import os
from twilio.rest import Client
# Create your models here.

class Score(models.Model):
    result = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return str(self.result)
    
    def save(self,*args,**kwargs):
        if self.result <90:
            account_sid ='AC3cd322393ac332e087e9d80cf8f9e0fe'
            auth_token ='a4eebece4e0f670b39696e66f8921e3a'
            client = Client(account_sid,auth_token)
            message = client.messages.create(
                                body='Hi there',
                                from_='+14846737929',
                                to='+923155699540'
                            )

            print(message.sid)
        return super().save(*args,**kwargs)
    