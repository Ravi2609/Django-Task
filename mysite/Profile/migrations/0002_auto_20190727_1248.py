# Generated by Django 2.2.3 on 2019-07-27 07:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='company_address',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_address', to='Address.Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, to='Profile.Profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='permanent_address',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='permanent_address', to='Address.Address'),
        ),
    ]
