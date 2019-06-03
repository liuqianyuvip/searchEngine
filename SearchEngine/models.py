from datetime import datetime

from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
 \
    analyzer, Completion, Keyword, Text, Integer

from elasticsearch_dsl.connections import connections

connections.create_connection(hosts=["localhost"])


class ArticleType(DocType):

    url = Keyword()
    title = Text(analyzer="ik_max_word")
    channel = Text()
    content = Text(analyzer="ik_max_word")
    author = Text()
    abstract = Text(analyzer="ik_max_word")
    create_date = Date()


    class Meta:
        index = 'search_news'
        doc_type = "NewsItem"

if __name__ == "__main__":
    ArticleType.init()