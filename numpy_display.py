# Petter Strandmark 2014.

ip = None
try:
	# Will only work from within IPython.
	ip = get_ipython()
except NameError:
	pass

if ip is not None:
	def array2html(A):
		html = '<table>'
		for row in A:
			html += "<tr>"
			for elem in row:
				html += "<td>" + str(elem) + "</td>"
			html += "</tr>"
		html += '</table>'
		return html

	html_formatter = ip.display_formatter.formatters['text/html']
	html_formatter.for_type_by_name('numpy', 'ndarray', array2html)
