from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        "Когда создано объявление",
        default=timezone.now,
        db_index=True)

    description = models.TextField("Текст объявления", blank=True)
    price = models.IntegerField("Цена квартиры", db_index=True)
    new_building = models.NullBooleanField(
        "Новое здание",
        default=None,
        db_index=True,
    )

    town = models.CharField(
        "Город, где находится квартира",
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        "Район города, где находится квартира",
        max_length=50,
        blank=True,
        help_text="Чертаново Южное")
    address = models.TextField(
        "Адрес квартиры",
        help_text="ул. Подольских курсантов д.5 кв.4")
    floor = models.CharField(
        "Этаж",
        max_length=3,
        help_text="Первый этаж, последний этаж, пятый этаж")

    rooms_number = models.IntegerField(
        "Количество комнат в квартире",
        db_index=True)
    living_area = models.IntegerField(
        "количество жилых кв.метров",
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField("Наличие балкона", db_index=True)
    active = models.BooleanField("Активно-ли объявление", db_index=True)
    construction_year = models.IntegerField(
        "Год постройки здания",
        null=True,
        blank=True,
        db_index=True)

    likes = models.ManyToManyField(
        User,
        related_name="from_users",
        default=None,
        verbose_name="Кто лайкнул",
        blank=True,
    )

    def __str__(self):
        return f"{self.town}, {self.address} ({self.price}р.)"


class Complaint(models.Model):
    from_who = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name="user_complaints",
        default=None,
        verbose_name="Кто жаловался",
    )
    about_flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        related_name="flat_complaints",
        default=None,
        verbose_name="Квартира, на которую пожаловались",
    )
    text = models.TextField(
        verbose_name="Текст жалобы",
        default=""
    )

    def __str__(self):
        return f"{self.__class__.__name__} " \
               f"from {self.from_who} about {self.about_flat}"


class Owner(models.Model):
    name = models.CharField(
        "ФИО владельца",
        max_length=200,
        db_index=True,
    )
    phonenumber = models.CharField("Номер владельца", max_length=20)
    standartized_phonenumber = PhoneNumberField(
        "Номер телефона (стандартизированный)",
        default="",
        blank=True,
        null=True,
    )
    flats = models.ManyToManyField(
        Flat,
        related_name="owners",
        verbose_name="Квартиры в собственности",
        blank=True,
    )

    def __str__(self):
        return f"{self.__class__.__name__} '{self.name}'"
