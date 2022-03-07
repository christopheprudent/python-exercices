import re

sample = 'The quick brown fox jumps over the lazy dog.'
to_search = 'fox'
m = re.search(to_search, sample)
if m:
    print('recherche "%s" dans (%s) trouvée aux positions (début, fin)=(%d, %d)' % (to_search, sample, m.start(), m.end()))
