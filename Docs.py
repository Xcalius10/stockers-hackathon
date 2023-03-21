from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import streamlit as st

# Function to convert PDF to text
def convert_pdf_to_txt(file_path):
    # Create a resource manager to manage PDF resources
    resource_manager = PDFResourceManager()
    
    # Create a string buffer to store the text
    text_buffer = StringIO()
    
    # Create a text converter
    text_converter = TextConverter(resource_manager, text_buffer, laparams=LAParams())
    
    # Create a PDF interpreter
    pdf_interpreter = PDFPageInterpreter(resource_manager, text_converter)
    
    # Open the PDF file
    with open(file_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            pdf_interpreter.process_page(page)
            
    # Get the text from the buffer
    text = text_buffer.getvalue()
    
    # Close the buffer
    text_buffer.close()
    
    # Return the text
    return text

# Get the content of the PDF file
pdf_content = convert_pdf_to_txt("pdf.pdf")

# Show the content of the PDF file in Streamlit
st.write("Content of the PDF file:")
st.write(pdf_content)