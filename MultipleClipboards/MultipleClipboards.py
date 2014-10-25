import sublime, sublime_plugin

class MultipleClipboards(sublime_plugin.TextCommand):
	def __init__(self, view):
		self.view = view
		self.entries = {}

	def run(self, edit, action, index):
		region = self.view.sel()[0]
		if action == 'copy' and region.size() > 0:
			self.entries[index] = self.view.substr(region)
		elif action == 'paste' and index in self.entries:
			for r in self.view.sel():
				self.view.erase(edit, r)
				self.view.insert(edit, r.begin(), self.entries[index])
