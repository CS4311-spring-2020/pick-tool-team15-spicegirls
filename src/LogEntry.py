
class LogEntry(object):    
    def __init__(self, timestamp, identifier, content, host, source, source_type):
        self.timestamp = timestamp
        self.identifier = identifier
        self.content = content
        self.host = host
        self.source = source
        self.source_type = source_type
