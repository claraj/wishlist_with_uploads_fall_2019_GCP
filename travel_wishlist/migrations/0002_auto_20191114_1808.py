# Generated by Django 2.2.6 on 2019-11-14 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='place',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_images/'),
        ),
    ]
