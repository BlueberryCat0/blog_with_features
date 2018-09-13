import datetime
from haystack import indexes
from .models import Post

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    content = indexes.CharField(model_attr='text')
    # pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Post
