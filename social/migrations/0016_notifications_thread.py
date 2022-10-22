# Generated by Django 4.1.1 on 2022-10-22 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_threadmodel_messagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='social.threadmodel'),
        ),
    ]
