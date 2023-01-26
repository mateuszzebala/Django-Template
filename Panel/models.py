import subprocess

from django.db import models

processes = {}
class Command(models.Model):
    command = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.command

    def is_run(self):
        try:
            run = True if processes[self.command].poll() is None else False
            return run
        except:
            return False

    def run(self):
        if self.is_run():
            return False
        processes[self.command] = subprocess.Popen(self.command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def kill(self):
        try:
            processes[self.command].kill()
            processes.pop(self.command)
            return True
        except:
            return False


class Message(models.Model):
    content = models.TextField()
    email = models.CharField(max_length=128)
    readed = models.BooleanField(default=False)
    datetime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.email} - {self.datetime}"

