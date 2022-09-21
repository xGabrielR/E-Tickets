from os import getenv
from elasticsearch import Elasticsearch
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ELASTIC_HOST = getenv("ELASTIC_HOST")
ELASTIC_AUTH_USER = getenv("ELASTIC_AUTH_USER")
ELASTIC_AUTH_CLOUD = getenv("ELASTIC_AUTH_CLOUD")

class ElasticCon():

    def __init__(self):
        self.con_host = ELASTIC_HOST
        self.auth_tokens = (ELASTIC_AUTH_USER, ELASTIC_AUTH_CLOUD)

    def make_es_con(self) -> Elasticsearch | bool:
        try:
            es = Elasticsearch(
                hosts=self.con_host,
                http_auth=self.auth_tokens
                
            )

            return es
        
        except:
            return None

    def clean_elastic_json(self, r, clean_json=True) -> list | bool:
        if not r['hits']['total']['value'] > 0:
            return None

        else:
            docs = r['hits']['hits']

            if clean_json:
                clean_docs = [doc['_source'] for doc in docs]
                return clean_docs

            else: 
                return docs


    def get_tickets_showroom(self, clean_json=True) -> list | bool:
        es = self.make_es_con()

        if es:
            r = es.search(
                    index="tickets",
                    body={"query": { "match_all": {}}}
            )

            return self.clean_elastic_json(r, clean_json)
        
        else: return None

    def search_tickets(self, text_query, clean_json=True) -> list | bool:
        text_query = text_query.strip().replace('\n', '').replace('\t', '').split(' ')

        es = self.make_es_con()

        if es:
            if len(text_query) == 1:
                r = es.search(
                        index="tickets",
                        body={"query": { "fuzzy": { "title": { "value": f"{text_query[0]}", "fuzziness": 2 } } } },        
                )

            else:
                r = es.search(
                        index="tickets",
                        body={"query": { "bool": { "must": [ 
                                {"wildcard": { "title": { "value": f"{text_query[0][:2]}*" } } }, 
                                {"wildcard": { "title": { "value": f"{text_query[1][:2]}*" } } } 
                        ] } } }
                )
                
            return self.clean_elastic_json(r, clean_json)

        else: 
            return None


    def get_all_users(self, clean_json=True) -> list | bool:
        es = self.make_es_con()

        if es:
            r = es.search(
                index="tickets-users",
                body={"query": { "match_all": {}}}
            )

            return self.clean_elastic_json(r, clean_json)
        
        else: 
            return None

    def get_user_name_by_email(self, email, clean_json=True) -> list | bool:
        es = self.make_es_con()

        if es:
            r = es.search(
                index="tickets-users",
                body={"query": {"match_phrase": {"email": f"{email}"}}}
            )

            return self.clean_elastic_json(r, clean_json)
        
        else: 
            return None

    def insert_new_user(self, first_name, last_name, email, pswd) -> list | bool:
        elastic_user_body = {
            "first_name": first_name,
            "last_name": last_name,
            "username": (first_name+last_name).lower(),
            "email": email,
            "pswd": pswd
        }
        
        es = self.make_es_con()

        if es:
            es.index(
                index='tickets-users',
                body=elastic_user_body
            )

        else:
            return None

    def get_secrets(self) -> tuple:
        usr = self.get_all_users()

        try:
            USERNAME = [(r['first_name']+r['last_name']).lower() for r in usr]
            EMAIL = [r['email'] for r in usr]
            PSWD  = [r['pswd'] for r in usr]

            return (USERNAME, PSWD, EMAIL)
        
        except:
            return (getenv('ADMIN_USERNAME'), getenv('ADMIN_PSWD'), getenv('ADMIN_EMAIL'))
