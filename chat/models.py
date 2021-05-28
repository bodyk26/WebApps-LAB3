from django.db import models

class ConnectedUsers(models.Model):
    username = models.CharField(max_length=50)
    connected = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "%s_ID%s connected at %s" % (self.username, self.id, self.connected)