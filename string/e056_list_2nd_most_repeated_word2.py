# -*- coding: utf-8 -*-

from operator import itemgetter

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # sort on count value (item 1 of tuple)
    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    # sort on count value (item 1 of tuple), and word value (item 0 of tuple)
    #counts_x = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]))
    counts_x = sorted(counts.items(), key=itemgetter(1, 0))
    
    print(counts_x)
    return counts_x[-2]
 
print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))

