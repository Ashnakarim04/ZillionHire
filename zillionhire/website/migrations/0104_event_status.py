# Generated by Django 5.0.1 on 2024-02-12 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0103_event_alumni'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
    ]
