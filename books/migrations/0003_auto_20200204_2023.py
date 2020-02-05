# Generated by Django 2.2.4 on 2020-02-04 12:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200202_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
