from django.conf import settings
from django.db import models



class UserMixin(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="User",
        help_text="",
    )

    class Meta:
        abstract = True


class NameDescriptionMixin(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Name",
        help_text="",
        )

    description = models.CharField(
        max_length=150,
        null=False,
        blank=True,
        # Opcja Django
        default="",
        verbose_name="Descritpion",
        help_text="",
    )

    class Meta:
        abstract = True


class ImageMixin(models.Model):

    image_url = models.URLField(
        blank=True,
        default="",
        verbose_name="Image URL",
        help_text="",
    )

    class Meta:
        abstract = True


class Producent(NameDescriptionMixin, UserMixin, ImageMixin, models.Model):

    slug = models.SlugField(unique=True)


class Car(NameDescriptionMixin, UserMixin, models.Model,):

    producent = models.ForeignKey(
        Producent,
        on_delete=models.PROTECT,
        null=False,
        blank=False,
        verbose_name="Producent",
        help_text="",

    )
    production = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name="Production",
        help_text="",)

    car_class = models.DecimalField(
        decimal_places=3,
        null=False,
        max_digits=9,
        blank=False,
        verbose_name="length",
        help_text="In milimeters",
    )
    BODY_STYLE_CHOICES = [
        ("two-door", "Two-door"),
        ("convertiblee", "Convertible"),
        ("three-door", "Three-door"),
        ("five-door", "Five-door"),

    ]
    body_style = models.CharField(
        max_length=15,
        choices=BODY_STYLE_CHOICES,
        null=False, blank=False,
        verbose_name="body_style",
        help_text="",
    )

    ENGINE_CHOICES = [
        ("2.0l", "2.0L"),
        ("2.3l", "2.3L"),
        ("2.5l", "2.5L"),
    ]
    engine = models.CharField(
        max_length=10,
        choices=ENGINE_CHOICES,
        null=False, blank=False,
        verbose_name="engine_style",
        help_text="",
    )
    TRANSMISSION_CHOICES = [
        ("5 speed", "5 speed"),
        ("5 speed sensonic", "5 speed sensonic"),
        ("4 speed sensonic", "4 speed sensonic"),
    ]
    transmission = models.CharField(
        max_length=10,
        choices=ENGINE_CHOICES,
        null=False,
        blank=False,
        verbose_name="engine_style",
        help_text="",
    )

    airconditioning = models.BooleanField(
        default=False,
        # form pozwala na nie przesłanie tego pola
        null=False,
        blank=True,
        # nie musi być dany, false to dla umów
        verbose_name="airconditioning",
    )
    length = models.DecimalField(
        decimal_places=3,
        null=False,
        max_digits=9,
        blank=False,
        verbose_name="length",
        help_text="In milimeters"
    )
    width = models.DecimalField(
        decimal_places=3,
        null=False,
        max_digits=9,
        blank=False,
        verbose_name="width",
    )
    height = models.DecimalField(
        decimal_places=3,
        null=False,
        max_digits=9,
        blank=False,
        verbose_name="height",

    )


class Place(NameDescriptionMixin, UserMixin, models.Model):

    openair = models.BooleanField(
        default=False,
        null=False,
        blank=True,
        # nie musi być dany, false to dla umów
        verbose_name="Is open air?",
    )


class UserCar(NameDescriptionMixin, UserMixin, ImageMixin, models.Model):

    place = models.ForeignKey(
        Place,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Place",
        help_text="",

    )

    car = models.ForeignKey(
        Car,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Type of car",
        help_text=""

    )

    date_come = models.DateTimeField(
        null=True, blank=True,
        verbose_name="Timestamp of come to garage",
        help_text="",
    )
