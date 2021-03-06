# Generated by Django 2.2.4 on 2019-08-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrolls', '0005_auto_20190815_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='basic_salary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='PAYE',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='gross_salary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='net_salary',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='nhif_deductions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='nssf_deductions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='other_deductions',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='overtime',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='salary_advance',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='payrolls',
            name='taxable_income',
            field=models.TextField(),
        ),
    ]
