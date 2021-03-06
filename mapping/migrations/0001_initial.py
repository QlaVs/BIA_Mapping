# Generated by Django 3.2.5 on 2021-07-01 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ac_choice', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_choice', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='NewUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_choice', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=150)),
                ('auto_column', models.CharField(max_length=150)),
                ('channel', models.TextField(choices=[('Работа на складе', 'Работа на складе'), ('Клиент и контактные данные', 'Клиент и контактные данные'), ('Проблемы с оборудованием', 'Проблемы с оборудованием'), ('Работа в рейсе', 'Работа в рейсе'), ('Работа в АК', 'Работа в АК')])),
                ('epic', models.TextField(choices=[('Последовательность загрузки', 'Последовательность загрузки'), ('Выезд со склада после 9.00', 'Выезд со склада после 9.00'), ('Долгая загрузка на складе', 'Долгая загрузка на складе'), ('Долгая выгрузка на складе', 'Долгая выгрузка на складе'), ('Долгая очередь на загрузку/выгрузку', 'Долгая очередь на загрузку/выгрузку'), ('Некорректный телефон клиента', 'Некорректный телефон клиента'), ('Некорректный адрес клиента', 'Некорректный адрес клиента'), ('Некорректные координаты адреса', 'Некорректные координаты адреса'), ('Нужен пропуск к клиенту за сутки', 'Нужен пропуск к клиенту за сутки'), ('Некорректный обед/время работы клиента', 'Некорректный обед/время работы клиента'), ('Касса', 'Касса'), ('Мобильное устройство', 'Мобильное устройств'), ('Мобильное приложение CDC', 'Мобильное приложение CDC'), ('Некорректная последовательность рейса', 'Некорректная последовательность рейса'), ('Не заложен простой на адресе', 'Не заложен простой на адресе'), ('Не хватает места в ТС для забора груза', 'Не хватает места в ТС для забора груза'), ('Мало времени на проезд между адресами', 'Мало времени на проезд между адресами'), ('Невозможен проезд на адрес', 'Невозможен проезд на адрес'), ('Несколько посещений одного адреса в разное время', 'Несколько посещений одного адреса в разное время'), ('Объемный груз в конце реестра', 'Объемный груз в конце реестра'), ('Нарушен интервал по заявке', 'Нарушен интервал по заявке'), ('Два ТС на один адрес', 'Два ТС на один адрес'), ('Начисления', 'Начисления'), ('Спец. Одежда', 'Спец. Одежда'), ('Транспортное средство', 'Транспортное средство'), ('Инструкции', 'Инструкции'), ('Прочее', 'Прочее')])),
                ('user', models.CharField(max_length=150)),
            ],
        ),
    ]
