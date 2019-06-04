from datetime import datetime

from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
 \
    analyzer, Completion, Keyword, Text, Integer

from elasticsearch_dsl.connections import connections
from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer
connections.create_connection(hosts=["localhost"])

# elasticsearch程序存在問題，这段代码避免报错
class CustomAnalyzer(_CustomAnalyzer):

    def get_analysis_definition(self):
        return {}
ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    origin_url = Keyword()
    title = Text(analyzer="ik_max_word")
    channel = Text()
    content = Text(analyzer="ik_max_word")
    author = Text()
    abstract = Text(analyzer="ik_max_word")
    create_date = Date()
    title_suggest = Completion(analyzer=ik_analyzer)
    abstract_suggest = Completion(analyzer=ik_analyzer)
    content_suggest = Completion(analyzer=ik_analyzer)
    class Meta:
        index = 'search_news'
        doc_type = "NewsItem"

if __name__ == "__main__":
    ArticleType.init()