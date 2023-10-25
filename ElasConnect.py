from elasticsearch import Elasticsearch


class ElasConnect:

    def __init__(self):
        self.elasticsearch_url = "https://172.16.172.10:9200"
        self.apikey = {
            "apikey_id": "7hfdIosBVeVLy-711ebt",
            "apikey_secret": "i0KTzfkURMePpvDxKZV8gQ",
            "apikey_base64": "N2hmZElvc0JWZVZMeS03MTFlYnQ6aTBLVHpma1VSTWVQcHZEeEtaVjhnUQ=="
        }

    def elas_connect(self):
        print("Loading ES...")

        es = Elasticsearch(
            self.elasticsearch_url,
            api_key=(self.apikey["apikey_id"], self.apikey["apikey_secret"]),
            verify_certs=False
        )

        return es
