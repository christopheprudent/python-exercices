# web solution
from datetime import datetime, timezone
local_time = datetime.now(timezone.utc).astimezone()
print()
print(local_time.isoformat())
print()

