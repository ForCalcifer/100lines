BOT_NAME = 'baidutieba'

SPIDER_MODULES = ['baidutieba.spiders']
NEWSPIDER_MODULE = 'baidutieba.spiders'

ITEM_PIPELINES = {'baidutieba.pipelines.ImageDownloadAndMongoDBPipeline': 1}
# 存放图片路径
IMAGES_STORE = '/Users/calcifer/meimei'

# mongodb配置
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "meizidb"
MONGODB_COLLECTION = "meizi"