from elasticsearch import Elasticsearch


class LivedoorNewsSearch:
    def __init__(self):
        self.es = Elasticsearch("localhost:9200")
        self.index = "ldnews"

    def search(self):
        res = self.es.search(index=self.index,  body={
                             "query": {"match_all": {}}})
        return res

    def addDocument(self, category, title, contents):
        document = {
            "category": category,
            "title": title,
            "contents": contents
        }

        res = self.es.index(
            index=self.index, body=document)

        return res
