import sublime
import sublime_plugin


class CommentFoldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.find_by_selector("-comment")
		self.view.fold(regions)

class CommentUnfoldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.find_by_selector("-comment")
		self.view.unfold(regions)
