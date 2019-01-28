from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20190127_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_count', models.PositiveSmallIntegerField(default=0)),
            ],
        ),

    ]
