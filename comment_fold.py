import sublime
import sublime_plugin


def char_at(view, point):
    return view.substr(sublime.Region(point, point + 1))


def is_space(view, point):
    return char_at(view, point).isspace()


def is_newline(view, point):
    return char_at(view, point) == "\n"


class CommentFoldCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.find_by_selector("-comment")
        fold_regions = []

        for region in regions:
            a, b = region.begin(), region.end()
            # keep new line before the fold
            if is_newline(view, a):
                a += 1
            # keep the indent before next comment
            while is_space(view, b - 1):
                b -= 1
                if is_newline(view, b):
                    break
            # if it is still a valid fold, add it to the list
            if a < b:
                fold_regions.append(sublime.Region(a, b))

        view.fold(fold_regions)


class CommentUnfoldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		regions = self.view.find_by_selector("-comment")
		self.view.unfold(regions)
