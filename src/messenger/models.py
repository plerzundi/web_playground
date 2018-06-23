from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


class Thread(models.Model):
    users = models.ManyToManyField(User, related_name='threads')
    messages = models.ManyToManyField(Message)


def messages_changed(sender, **kwargs):
    instance = kwargs.pop("instance", None) #hilo
    action = kwargs.pop("action", None)
    pk_set = kwargs.pop("pk_set", None) #usuarios
    print(instance, action, pk_set)


    false_pk_set = set()
    if action is "pre_add":
        for msg_pk in pk_set:
            msg = Message.objects.get(pk=msg_pk)
            if msg.user not in instance.users.all():
                print("Ups, ({}) no forma parte del hilo".format(msg.user))
                false_pk_set.add(msg_pk)

    # Se buscan los mensajes si estan en la pk_set y los borramos de la pk_set
    pk_set.difference_update(false_pk_set)

m2m_changed.connect(messages_changed, sender=Thread.messages.through)
