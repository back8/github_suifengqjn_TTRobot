import scrapy


class JinfomationItem(scrapy.Item):
    info_id = scrapy.Field()
    user_img = scrapy.Field()
    user_name = scrapy.Field()
    title = scrapy.Field()
    publish_time = scrapy.Field()
    reference = scrapy.Field()
    content_desc = scrapy.Field()
    content_imgs = scrapy.Field()
    thumbnail_img = scrapy.Field()
    video_id = scrapy.Field()
    video_url = scrapy.Field()
    video_duration = scrapy.Field()