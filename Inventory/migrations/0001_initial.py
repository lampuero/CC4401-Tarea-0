# Generated by Django 2.0.3 on 2018-03-28 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='nombre_del_producto')),
                ('stock', models.IntegerField(default=5)),
            ],
        ),
    ]
