# Generated by Django 3.2.6 on 2021-08-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechStack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='myproject',
            name='requirement',
        ),
        migrations.AddField(
            model_name='myproject',
            name='requirement',
            field=models.ManyToManyField(to='mainApp.TechStack'),
        ),
    ]
