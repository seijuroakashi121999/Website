# Generated by Django 2.0.7 on 2018-07-10 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='rating',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='girl',
            name='g_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='score',
            name='points',
            field=models.PositiveIntegerField(),
        ),
    ]
