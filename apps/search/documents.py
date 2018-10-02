from django_elasticsearch_dsl import DocType, Index, Text, fields
from apps.posts.models import Post

posts = Index('posts')

posts.settings(
    number_of_shards=1,
    number_of_replicas=0
)

@posts.doc_type
class PostDocument(DocType):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'text',
            'is_created',
            'created_at',
        ]
