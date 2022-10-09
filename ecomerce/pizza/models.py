from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save, m2m_changed
from django.dispatch import receiver

User = get_user_model()


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User)


# pre_save.connect(team_pre_save, sender=Team)
# m2m_changed.connect(team_members_changed, sender=Team.members.through)


@receiver(pre_save, sender=Team)
def team_pre_save(sender, instance, **kwargs):
    if instance.pk:
        print('instance pk now ')
        instance._old_m2m = set(list(instance.members.values_list('pk', flat=True)))
    else:
        print('create or set ')
        instance._old_m2m = set(list())


@receiver(m2m_changed, sender=Team.members.through)
def team_members_changed(sender, instance, **kwargs):
    if kwargs['action'] == "post_clear":
        # remove all users from group
        print("post_clear hit 1",kwargs['action'])
        group = Group.objects.get(name='some group')
        for member in instance._old_m2m:
            user = User.objects.get(pk=member)
            user.groups.remove(group)

    if kwargs['action'] == "post_add":
        print("post_add hit 2",kwargs['action'])
        added_members = list(kwargs['pk_set'].difference(instance._old_m2m))
        deleted_members = list(instance._old_m2m.difference(kwargs['pk_set']))

        if added_members or deleted_members:
            # we got a change - do something, for example add them to a group?
            group = Group.objects.get(name='some group')

            for member in added_members:
                user = User.objects.get(pk=member)
                user.groups.add(group)

            for member in deleted_members:
                user = User.objects.get(pk=member)
                user.groups.remove(group)
