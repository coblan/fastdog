from . elastic import ELKHander,helpers

class ELKNginx(ELKHander):
    def make_index(self):
        properties =  { 
            "@timestamp":    { "type": "date"  }, 
            "level":     { "type": "keyword"  }, 
            "host": {"type": "keyword"},
            "message":      { "type": "text" }, 
            "path":{"type": "keyword"},
            "url":{"type": "keyword"},
            "ip":{"type": "ip"},
             "method":{"type": "keyword"},
             "agent":{"type":"keyword"},
        }
        if self.es.info().get('version').get('number').startswith('7'):
            _index_mappings = {
                "mappings": {
                    "properties":properties
                }
              }
        else:
            _index_mappings = {
                "mappings": {
                    "_doc":{
                        "properties": properties
                    }
                }
              }
            
        if self.es.indices.exists(index= self.index ) is not True:
            res = self.es.indices.create(index = self.index, body=_index_mappings) 

    
    def send(self,lines):
        actions=[ ]
        for line in lines:
            actions.append({
                    "_index": self.index,
                    "_type": "_doc",
                    "_source": {
                        "level":line.get('level','NULL'),
                        "host":line.get('host',self.hostName),
                        "message":line.get('message'),
                        '@timestamp':line.get('@timestamp'),
                        "path":line.get('path'),
                        "url":line.get('url'),
                        "ip":line.get('ip'),
                        "method":line.get('method'),
                        "agent":line.get('agent'),
                    }
            })
        helpers.bulk(self.es, actions)