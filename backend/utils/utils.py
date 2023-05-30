from datetime import datetime, timezone

def ISO8601_now():    
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')
