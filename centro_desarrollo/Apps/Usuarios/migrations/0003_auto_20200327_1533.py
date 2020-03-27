# Generated by Django 3.0.2 on 2020-03-27 21:33

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Usuarios', '0002_auto_20200327_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='usuario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
        migrations.AddField(
            model_name='usuario',
            name='user_ptr',
            field=models.OneToOneField(auto_created=True, default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]