# Generated by Django 4.0.4 on 2022-05-28 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAccount', '0003_alter_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='source',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
