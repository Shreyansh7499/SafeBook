# Generated by Django 2.2.5 on 2019-10-25 02:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_privacy', models.CharField(choices=[('private', 'private'), ('public', 'public'), ('friends', 'friends')], default='private', max_length=20)),
                ('user_type', models.CharField(choices=[('casual', 'casual'), ('silver', 'silver'), ('gold', 'gold'), ('platinum', 'platinum'), ('commercial', 'commercial')], default='casual', max_length=20)),
                ('number_of_transactions', models.IntegerField(default=0)),
                ('number_of_groups', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_constraint', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
