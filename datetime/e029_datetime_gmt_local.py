# web solution
import time
print('Format: %a, %d %b %Y %I:%M:%S %p %Z')
print("  GMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
print("Local: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z"))
