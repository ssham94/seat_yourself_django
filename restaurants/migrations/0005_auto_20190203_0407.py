# Generated by Django 2.1.5 on 2019-02-03 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurants', '0004_auto_20190202_2326'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='notes',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
    ]