import pikepdf
import streamlit as st
from pypdf import PdfWriter
from pdf2docx import Converter

st.title("Secured Simple PDF merger and Word Converter ")

def main():

    option = st.selectbox('Merge or Convert PDF Here', ('Merge PDF','Convert PDF into Word'))

    if option == 'Merge PDF':
        uploaded_files = st.file_uploader("Files will be merged in the order of selection", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename: ",uploaded_file.name)

        merge=st.button("Merge")

        if merge:
            merger = PdfWriter()
            for pdf in uploaded_files:
                merger.append(pdf)
                merger.write("Merged_PDF.pdf")

            with open("Merged_PDF.pdf", "rb") as f:
                PDFbyte = f.read()

            st.download_button(label="Download PDF",
                               data=PDFbyte,
                               file_name="Merged_PDF.pdf",
                               mime='application/octet-stream')

    if option == 'Convert PDF into Word':
        pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        if pdf_file is not None:
            # Save uploaded PDF file
            with open("uploaded_file.pdf", "wb") as f:
                f.write(pdf_file.getbuffer())

            # Convert PDF to Word
            word_file = "Converted Word.docx"
            cv = Converter("uploaded_file.pdf")
            cv.convert(word_file, start=0, end=None)
            cv.close()

            # Download Word file
            with open(word_file, "rb") as f:
                result = f.read()
            st.download_button(
                "Download Converted File", data=result, file_name=word_file
            )


if __name__ == '__main__':
    main()
