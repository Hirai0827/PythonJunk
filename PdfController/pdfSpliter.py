from PyPDF2 import PdfFileWriter, PdfFileReader

input1 = PdfFileReader(open("prove.pdf", "rb"))
for i in range(input1.getNumPages()): 
    output = PdfFileWriter()
    page = input1.getPage(i)
    output.addPage(page)
    outputStream = open("document-output"+str(i)+".pdf", "wb")
    output.write(outputStream)
    outputStream.close()