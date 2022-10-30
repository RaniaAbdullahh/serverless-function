from http.server import BaseHTTPRequestHandler
from urllib import parse 

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path   #/api/aloha?name="Rania"
        print('hiiiiiiii',s)
        url_components=parse.urlsplit(s)
        query_string_list=parse.parse_qsl(url_components.query) 
        print(query_string_list)
        my_dictionary= dict(query_string_list)

        

        name= my_dictionary.get('name', False)
        if name :
            message=f'Hello {name}'
        else :
            message="Hello Stranger"



        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()    

        self.wfile.write(message.encode())
        return