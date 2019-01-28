from django.db import migrations, models


def forwards(apps, schema_editor):
    UserCount = apps.get_model('poll', 'UserCount')
    UserCount.objects.create()
    assert(UserCount.objects.last().id == 1)


def backwards(apps, schema_editor):
    UserCount = apps.get_model('poll', 'UserCount')
    UserCount.objects.get(id=1).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0004_usercount_create_model'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
