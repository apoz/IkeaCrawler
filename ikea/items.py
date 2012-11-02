# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class IkeaItem(Item):
    # define the fields for your item here like:
    # name = Field()
    description = Field()
    keywords = Field()
    country = Field()
    language = Field()
    store_id = Field()
    title = Field()
    product_name = Field()
    category_name = Field()
    subcategory_if = Field()
    price = Field()
    price_other = Field()
    changed_family_price = Field()
    changed_family_price_other = Field()
    item_id = Field()
    partnumber = Field()
    url = Field()
    image = Field()
    pass
