import tkinter as tk
from tkinter import filedialog


class Menubar:

	def __init__(self, parent):

		font_specs = ("Arial", 12)

		menubar = tk.Menu(parent.master, font = font_specs)
		parent.master.config(menu = menubar)

		file_dropdown = tk.Menu(menubar, font = font_specs, tearoff = 0, fg = 'orange')
		file_dropdown.add_command(label = 'Create File', command = parent.create_file, accelerator='Ctrl+N')
		file_dropdown.add_command(label = 'Open File', command = parent.open_file, accelerator='Ctrl+O')
		file_dropdown.add_command(label = 'Store File', command = parent.store_file, accelerator='Ctrl+S')
		file_dropdown.add_command(label = 'Store File as', command = parent.store_file_as, accelerator='Ctrl+Shift+S')
		file_dropdown.add_separator()
		file_dropdown.add_command(label = 'Quit', command = parent.master.destroy)

		menubar.add_cascade(label = "File", menu = file_dropdown)


class Statusbar:

	def __init__(self, parent):
		
		font_specs = ("Arial", 10)

		self.status = tk.StringVar()
		self.status.set('EnDe - 1.0 Poorna Venkata Sai')

		label = tk.Label(parent.textarea, textvariable = self.status, fg = 'blue', bg = 'lightgrey', anchor = 'sw', font = font_specs)
		label.pack(side = tk.BOTTOM, fill = tk.BOTH)

	def update_status(self, *args):
		if isinstance(args[0], bool):
			self.status.set('File Updated Successfully.')
		else:
			self.status.set('EnDe - 1.0 Poorna Venkata Sai')

class EnDe:

	def __init__(self, master):
		
		master.title('Untitled - EnDe Editor')
		master.geometry('800x500')

		font_specs = ("consolas", 16)

		self.master = master
		self.filename = None

		self.textarea = tk.Text(master, font = font_specs, fg = 'green')
		self.scroll = tk.Scrollbar(master, command = self.textarea.yview)
		self.textarea.configure(yscrollcommand = self.scroll.set)
		self.textarea.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
		self.scroll.pack(side = tk.RIGHT, fill = tk.Y)

		self.menubar = Menubar(self)
		self.statusbar = Statusbar(self)

		self.bind_shortcuts()

	def set_window_title(self, name = None):
		if name:
			self.master.title(name + ' - EnDe Editor')
		else:
			self.master.title('Untitled - EnDe Editor')
		

	def create_file(self, *args):
		self.textarea.delete(1.0, tk.END)
		self.filename = None
		self.set_window_title(self.filename)

	def open_file(self, *args):
		self.filename = filedialog.askopenfilename(defaultextension = '*.txt', filetypes = [('Text Files','*.txt'), ('All FIles','*.*')])

		if self.filename:
			self.textarea.delete(1.0, tk.END)

			with open(self.filename, 'r') as f:
				self.textarea.insert(1.0, f.read())

			self.set_window_title(self.filename)


	def store_file(self, *args):
		if self.filename:
			
			try:
				textarea_content = self.textarea.get(1.0, tk.END)
				with open(self.filename,'w') as f:
					f.write(textarea_content)
				self.statusbar.update_status(True)

			except Exception as e:
				print(e)

		else:
			self.store_file_as()

	def store_file_as(self, *args):
		
		try:
			create_file = filedialog.asksaveasfilename(initialfile = 'Untitled.txt', defaultextension = '*.txt', filetypes = [('Text Files','*.txt'), ('All FIles','*.*')])

			textarea_content = self.textarea.get(1.0, tk.END)
			with open(create_file,'w') as f:
				f.write(textarea_content)

			self.statusbar.update_status(True)
			self.filename = create_file
			self.set_window_title(self.filename)

		except Exception as e:
			print(e)

	def bind_shortcuts(self):
		self.textarea.bind('<Control-n>', self.create_file)
		self.textarea.bind('<Control-o>', self.open_file)
		self.textarea.bind('<Control-s>', self.store_file)
		self.textarea.bind('<Control-S>', self.store_file_as)
		self.textarea.bind('<Key>', self.statusbar.update_status)


if __name__ == '__main__':
	master = tk.Tk()
	ed = EnDe(master)
	master.mainloop()
