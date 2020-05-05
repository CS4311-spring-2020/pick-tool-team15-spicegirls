class LogEntry:
    def _init_(self, number, timestamp, content, source, event_type, last_step):
        self.number = number
        self.timestamp = timestamp
        self.content = content
        self.source = source
        self.eventType = event_type
        self.status = last_step