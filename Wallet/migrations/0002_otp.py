# Generated by Django 2.2.5 on 2019-10-29 21:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(default=12362)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='otp_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
