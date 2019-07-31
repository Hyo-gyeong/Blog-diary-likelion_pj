# Generated by Django 2.2.3 on 2019-07-31 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190731_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(verbose_name='내용'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/', verbose_name='(추억이 있는) 사진'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(help_text='200자 내로 입력 가능합니다.', max_length=200, verbose_name='제목'),
        ),
    ]
