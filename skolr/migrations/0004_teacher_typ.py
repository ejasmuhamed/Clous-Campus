# Generated by Django 2.2.3 on 2019-07-04 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skolr', '0003_auto_20190704_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='typ',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]