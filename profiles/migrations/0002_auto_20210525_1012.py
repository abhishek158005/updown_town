# Generated by Django 3.2.3 on 2021-05-25 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='flipped_profile_photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='match',
            field=models.ManyToManyField(through='profiles.ProfileMatch', to='profiles.Profile'),
        ),
        migrations.AddField(
            model_name='profilematch',
            name='user1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='first', to='profiles.profile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilematch',
            name='user2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='second', to='profiles.profile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profilematch',
            name='match_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='profilematch',
            unique_together={('user1', 'user2')},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='Profiles',
        ),
        migrations.RemoveField(
            model_name='profilematch',
            name='match_profile',
        ),
        migrations.RemoveField(
            model_name='profilematch',
            name='requested_profile',
        ),
    ]
