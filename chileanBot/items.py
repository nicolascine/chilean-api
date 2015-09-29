from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field
from congress.models import Senator

class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = Senator
