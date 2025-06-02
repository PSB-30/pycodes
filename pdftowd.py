#Scope of this project is limited for converting pdf to word

from pdf2docx import Converter #we are using the Converter class


old_pdf="pythoncheck.pdf"
new_doc="new.docx"

obj=Converter(old_pdf)
obj.convert(new_doc)
obj.close()