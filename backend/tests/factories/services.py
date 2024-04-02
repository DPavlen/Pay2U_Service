import datetime
import json

import factory.fuzzy
from factories.users import UserFactory
from services.models import Category, Services, Subscription, TariffList


class JSONFactory(factory.DictFactory):

    @classmethod
    def _generate(cls, create, attrs):
        obj = super()._generate(create, attrs)
        return json.dumps(obj)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('category_name')
    slug = factory.Sequence(lambda n: "name{}".format(n))
    description = factory.SubFactory(UserFactory)
    icon = factory.django.ImageField()


class ServicesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Services

    name = factory.Sequence(lambda n: "Сервис {}".format(n))
    category = factory.SubFactory(CategoryFactory)
    link = factory.LazyAttribute(lambda o: '%s@example.com' % o.name)
    icon_big = factory.django.ImageField()
    icon_square = factory.django.ImageField()
    icon_small = factory.django.ImageField()
    is_popular = True
    description = factory.Sequence(lambda n: "Сервис{}".format(n))


class TariffListFactory(factory.django.DjangoModelFactory):
    duration = [x[0] for x in TariffList.Duration]

    class Meta:
        model = TariffList

    name = factory.Sequence(lambda n: "Урок{}".format(n))
    description = factory.Sequence(lambda n: "Урок{}".format(n))
    services = factory.SubFactory(ServicesFactory)
    services_duration = factory.fuzzy.FuzzyChoice(duration)
    tariff_full_price = factory.fuzzy.FuzzyInteger(500, 1000)
    tariff_promo_price = factory.fuzzy.FuzzyInteger(100, 600)


class SubscriptionFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Subscription

    created_at = factory.fuzzy.FuzzyDate(
        datetime.date.today() + datetime.timedelta(days=5),
        datetime.date.today() + datetime.timedelta(days=10),
    )
    updated_at = factory.LazyAttribute(lambda o: o.created_at + datetime.timedelta(days=30))
    user = factory.SubFactory(UserFactory)
    tariff = factory.SubFactory(TariffListFactory)
    is_active = True
