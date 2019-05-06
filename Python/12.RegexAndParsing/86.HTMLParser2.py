# data.strip() removes leading and trailing whitespaces.
# print(">>> Data\n", data) will add \r in between
# use print(">>> Data", data, sep='\n')
# or print(">>> Data")
# print(data)

from html.parser import HTMLParser
class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split('\n'))
        if number_of_line>1:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data) # print on the same line 


html_string = ''
for i in range(int(input())):
    html_string += input().rstrip()+'\n'

parser = CustomHTMLParser()    
parser.feed(html_string)
parser.close()
