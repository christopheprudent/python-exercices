# web solution
import re
text = '**//Python_Exercises// - 12. '
pattern = re.compile('[\W_]+')
print('effacement autre que alphanum dans "%s" : %s' %(text, pattern.sub('', text)))
