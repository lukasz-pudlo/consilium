# Generated by Django 5.1.3 on 2024-11-24 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GrantApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('title_of_request', models.CharField(max_length=255)),
                ('funding_summary', models.TextField()),
                ('how_spend_grant', models.TextField()),
                ('importance_of_grant', models.TextField()),
                ('goals', models.TextField()),
                ('required_date', models.DateField()),
                ('amount_requested', models.DecimalField(decimal_places=2, max_digits=10)),
                ('funding_in_place', models.TextField(blank=True, null=True)),
                ('benefit_description', models.TextField()),
                ('commitment_description', models.TextField()),
                ('barriers_description', models.TextField(blank=True, null=True)),
                ('result_availability', models.TextField(blank=True, null=True)),
                ('heard_from', models.CharField(blank=True, max_length=255, null=True)),
                ('additional_info', models.TextField(blank=True, null=True)),
                ('previous_application_details', models.TextField(blank=True, null=True)),
                ('evaluation_proposal', models.TextField(blank=True, null=True)),
                ('support_network', models.TextField(blank=True, null=True)),
                ('other_support', models.TextField(blank=True, null=True)),
                ('applicant_signature', models.CharField(max_length=255)),
                ('signed_date', models.DateField()),
                ('parent_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
