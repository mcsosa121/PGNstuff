import openpyxl
import urllib
import urllib2
import re

wb = openpyxl.load_workbook('pgn.xlsx')
s = wb.get_sheet_by_name('Sheet1')
names = []
for cell in s.columns[2]:
    names.append(cell.value)
count = 1
for cell in s.columns[10]:
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', cell.value)
    if len(urls) == 2:
        HTTP_client = urllib2.build_opener()
        url = urls[0]
        data = HTTP_client.open(url)
        with open (names[count]+'.pdf','wb') as f:
            f.write(data.read())
        count = count + 1
    else:
        print "Error"
