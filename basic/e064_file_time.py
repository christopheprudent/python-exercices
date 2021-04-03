import sys
import os.path, time

if (len(sys.argv) > 1): 
	from pathlib import Path
	my_file = Path(sys.argv[1])
	if not my_file.is_file():
		raise ValueError('fichier non trouvé!')
	else:
		print("Last modified: %s" % time.ctime(os.path.getmtime(sys.argv[1])))
		print("Created: %s" % time.ctime(os.path.getctime(sys.argv[1])))
else:
	raise ValueError('manque fichier!')
