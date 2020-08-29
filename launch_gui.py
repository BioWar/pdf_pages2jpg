from tkinter import filedialog
from tkinter import Tk, Label, Button, Entry
from pdf2image import convert_from_path

pdf_document = None
pages_count = None

def browseFiles():
	global pdf_document
	filename = filedialog.askopenfilename(initialdir = "/",
					      title = "Select PDF file",
					      filetypes = [("PDF document", "*.pdf")])
	label_file_explorer.configure(text="File choosen: " + filename)
	pdf_document = filename
	print(filename)

def convert():
	global pages_count, pdf_document
	pages = entry.get().split(",")
	print(type(pages[0]))
	output_path = filedialog.askdirectory()
	book_name = pdf_document.split('/')[-1]
	size = [(350, 500), (600, 900)]
	for page in pages:
		if page != 1:
			page_converted = convert_from_path(pdf_document,
						    dpi=500,
						    first_page=int(page),
						    last_page=int(page),
					    	    size=size[1],
					    	    use_pdftocairo=True)
		else:
			page_converted = convert_from_path(pdf_document,
							   dpi=500,
							   first_page=int(page),
							   last_page=int(page),
							   size=size[0],
							   use_pdftocairo=True)
		print(len(page_converted))
		page_converted[0].save(output_path + '/' + book_name + '_' + str(page), 'PNG')

window = Tk()
window.title('PDF2PNG')
window.geometry("500x500")
window.config(background="white")
label_file_explorer = Label(window,
			    text = "PDF2PNG",
			    width = 100, height = 4,
			    fg = "blue")

button_explorer = Button(window,
			 text = "Choose PDF",
			 command = browseFiles)

button_exit = Button(window,
		     text = "Exit",
		     command = exit)

label_convert = Label(window,
		      text = "Convert selected pages from PDF document to PNG",
		      width = 100, height = 4,
		      fg = "blue")

button_convert = Button(window,
			text = "Convert",
			command = convert)

label_entry_pages = Label(window,
			  text = "Select pages to convert. ',' is delimeter",
			  width = 100, height = 4,
			  fg = "blue")

entry = Entry(window, textvariable=pages_count)

entry.grid(column=1, row = 2)
label_file_explorer.grid(column = 1, row = 1)
button_explorer.grid(column = 1, row = 3)
button_exit.grid(column = 1, row = 4)
label_convert.grid(column = 1, row = 5)
button_convert.grid(column = 1, row = 6)
window.mainloop()
