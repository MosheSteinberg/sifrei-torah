# Generated by Django 4.0.2 on 2022-02-15 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_physicallocation_sefertorah_current_ownership_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='physicallocation',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Physical Location'),
        ),
        migrations.AlterField(
            model_name='sefertorah',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='sefertorah',
            name='quality',
            field=models.CharField(choices=[('1', 'First'), ('2', 'Second'), ('3', 'Third'), ('4', "Don't Use")], default='4', max_length=10),
        ),
    ]
