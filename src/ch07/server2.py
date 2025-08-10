from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = {
            'name': 'masuda tomoaki',
            'age': 55,
            'country': 'Japan',
            'message': 'Hello, world!'
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        data = json.loads(post_data.decode('utf-8'))

        # print('name = ' + data['name'] )
        # print('age = ' + str(data['age']) )
        # print('job = ' + data['job'] )
        # response = {
        #    'received': f"Your name is {data['name']}."
        # }

        # 配列を読み込む
        for item in data:
            print ('id = ' + str(item['id']))
            print('name = ' + item['name'] )
            print('age = ' + str(item['age']) )

        response = {
           'received': f"data count is {len(data)}."
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()