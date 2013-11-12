import sublime, sublime_plugin
import re

# open console ctrl+`
# view.run_command("toggle_boolean")

# keep a list of boolean pairs such as True/False, YES/NO, true/false
# llok for next occurence of a boolean
# mark the boolean, select it, and toggle it

class Toggle_booleanCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# self.view.insert(edit, 0, "Hello, World!")
		# build set of boolean pairs
		pairs = {"true" : "false", "True" : "False", "TRUE" : "FALSE", "YES"  : "NO" }
		reverse_pairs = {v:k for k, v in pairs.items()}
		pairs.update(reverse_pairs)
		all_pairs = pairs

		# for x in all_pairs:
		# 	print(x + " : " + all_pairs[x])

		# locate current line 
		current_point = self.cursor_pos(self.view);
		current_word_region = self.view.word(current_point)
		current_word_begin = current_word_region.a
		current_line_region = self.view.line(current_point)
		current_pos_to_eol_region = sublime.Region(current_word_begin, current_line_region.b)
		print("looking at" + str(current_pos_to_eol_region))

		# iterate over words in current line
		# split by non-word charecters
		current_line_content = self.view.substr(current_pos_to_eol_region)
		words_in_line = re.split("\W+", current_line_content)

		for word in words_in_line:
			if word in all_pairs:
				search_result = self.view.find( "\<" + word + "\>", current_word_begin)
				if current_pos_to_eol_region.contains(search_result):
					key = word
					print("found " + key)
					inv_boolean = all_pairs[key]
					self.view.replace(edit, search_result, inv_boolean)
					break

	def cursor_pos(self, view):
		return view.sel()[0].b
