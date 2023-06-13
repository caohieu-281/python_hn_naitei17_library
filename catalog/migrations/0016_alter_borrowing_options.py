# Generated by Django 4.2.1 on 2023-05-25 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_delete_bookinstance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='borrowing',
            options={'ordering': ['-updated_at'], 'permissions': (('can_view_all_borrowing', 'Can view all borrowing requests'), ('can_approve_borrowing', 'Can set borrowing request as approved'), ('can_decline_borrowing', 'Can set borrowing request as declined'), ('can_mark_borrowing', 'Can set borrowing request as borrowing'), ('can_mark_returned', 'Can set borrowing request as returned'))},
        ),
    ]
