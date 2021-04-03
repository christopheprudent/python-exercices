def add_tag(tag, value):
	# web soution
	return "<%s>%s</%s>" % (tag, value, tag)
	return '<' + tag + '>' + value + '</' + tag + '>'

print(add_tag('i', 'Python'))
print(add_tag('b', 'Python Tutorial'))
