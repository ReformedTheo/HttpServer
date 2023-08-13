#importa as bibliotecas necessárias
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

#Define host name  e porta de entrada
hostName = "localhost"
serverPort = 6969


#Classe de iniciação do servidor
class MeuServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>teste</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p> Request: %s </p>" % self.path,"utf-8"))
        self.wfile.write(bytes(" Este é um exemplo de um servidor HTTP feito em python <p></p></body></html>", "utf-8"))
        
        
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MeuServer)
    print("Server started hhtp://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Server stopped.")
