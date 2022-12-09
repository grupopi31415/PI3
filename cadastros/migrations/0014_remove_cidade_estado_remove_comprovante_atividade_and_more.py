# Generated by Django 4.1.3 on 2022-12-03 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0013_cidade_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cidade',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='comprovante',
            name='atividade',
        ),
        migrations.RemoveField(
            model_name='comprovante',
            name='progressao',
        ),
        migrations.RemoveField(
            model_name='comprovante',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='progressao',
            name='classe',
        ),
        migrations.RemoveField(
            model_name='progressao',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='validacao',
            name='comprovante',
        ),
        migrations.RemoveField(
            model_name='validacao',
            name='validado_por',
        ),
        migrations.RemoveField(
            model_name='classe',
            name='nivel',
        ),
        migrations.RemoveField(
            model_name='servidor',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='situacao',
            name='movimentado_em',
        ),
        migrations.RemoveField(
            model_name='situacao',
            name='movimentado_por',
        ),
        migrations.DeleteModel(
            name='Atividade',
        ),
        migrations.DeleteModel(
            name='Campo',
        ),
        migrations.DeleteModel(
            name='Campus',
        ),
        migrations.DeleteModel(
            name='Cidade',
        ),
        migrations.DeleteModel(
            name='Comprovante',
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
        migrations.DeleteModel(
            name='Progressao',
        ),
        migrations.DeleteModel(
            name='Validacao',
        ),
    ]
