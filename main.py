from solver import getSudoku
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse


hostName = "localhost"
serverPort = 8080

def getParam(p):
    try:
        #print(p)
        params = p.split("/?")[1].split("&")
        d = dict()
        for param in params:
            key = param.split("=")[0]
            val = param.split("=")[1]
            d[key] = val
        return d.get('level','easy')
    except (IndexError):
        print('err')

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        level = getParam(self.path)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(bytes(getSudoku(level), "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")