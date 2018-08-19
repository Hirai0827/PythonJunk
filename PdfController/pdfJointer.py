from PyPDF2 import PdfFileWriter, PdfFileReader
output = PdfFileWriter()
while True:
    path = input("結合するpdfを選択してください(実行の場合は「do」キャンセルは「end」)")
    
    if path == "do":
        mergedName = input("保存名を入力してください")
        outputStream = open(mergedName + "-merged.pdf", "wb")
        output.write(outputStream)
        outputStream.close()
        
        break
    elif path == "end":
        break
    else:
        
        try :
            input1 = PdfFileReader(open(path, "rb"))
            output.appendPagesFromReader(input1)
            print("選択されたファイルを結合しました")
        except:
            print("そのようなファイルは存在しません")