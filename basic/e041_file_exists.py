import sys
from pathlib import Path

if (len(sys.argv) > 1): 
	my_file = Path(sys.argv[1])
	if not my_file.is_file():
		raise ValueError('fichier non trouvé!')
else:
	raise ValueError('manque fichier!')
