from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    street = models.CharField(max_length=50, null=True, blank=True)
    house = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f'{self.country}, {self.city}'


class Product(models.Model):
    title = models.CharField(max_length=50)
    model = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ChainLink(models.Model):
    class Type(models.IntegerChoices):
        factory = 1, 'Завод'
        retailer = 2, 'Розничная сеть'
        entrepreneur = 3, 'Индивидуальный предприниматель'

    title = models.CharField(verbose_name='Наименование', max_length=100, null=False)
    type = models.PositiveSmallIntegerField(verbose_name='Тип звена', choices=Type.choices)
    contact = models.ForeignKey(Contact, verbose_name='Контакты', null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, verbose_name='Продукты', blank=True)
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=15, decimal_places=2, default=0)
    supplier = models.ForeignKey(
        'sales_chain.ChainLink', verbose_name='Поставщик', null=True, blank=True, on_delete=models.SET_NULL
    )
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Звено'
        verbose_name_plural = 'Звенья'

    def __str__(self):
        return f'{self.title}'
