# Generated by Django 4.2.3 on 2023-08-04 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diet', '0003_day_diet_delete_foodtype_day_diet_day_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diet',
            name='name',
        ),
        migrations.AlterField(
            model_name='diet',
            name='diet',
            field=models.CharField(max_length=100),
        ),
    ]