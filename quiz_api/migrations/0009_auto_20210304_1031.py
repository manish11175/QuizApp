# Generated by Django 3.0.6 on 2021-03-04 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_api', '0008_auto_20210304_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image_four',
            field=models.FileField(default='', upload_to='student/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='question',
            name='image_one',
            field=models.FileField(default='', upload_to='student/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='question',
            name='image_three',
            field=models.FileField(default='', upload_to='student/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='question',
            name='image_two',
            field=models.FileField(default='', upload_to='student/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='question',
            name='question_image',
            field=models.FileField(default='', upload_to='student/%Y/%m/%d/'),
        ),
    ]
