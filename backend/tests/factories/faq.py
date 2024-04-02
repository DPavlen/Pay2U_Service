import datetime

import factory.fuzzy
from faqs.models import Faq


class FaqFactory(factory.django.DjangoModelFactory):
    """Test factory for FAQ model."""

    class Meta:
        model = Faq

    topic_question = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    сategory = Faq.Category.REGISTRATION
    question = factory.Faker("sentence", nb_words=5, variable_nb_words=True)
    answer = factory.Faker("sentence", nb_words=15, variable_nb_words=True)
    created = factory.fuzzy.FuzzyDate(
        datetime.date.today() + datetime.timedelta(days=5),
        datetime.date.today() + datetime.timedelta(days=10),
    )
    updated = factory.LazyAttribute(lambda o: o.created + datetime.timedelta(days=30))
