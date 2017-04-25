import ssl
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 443

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
        def do_GET(self):
		print "got request"
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                self.wfile.write("<!DOCTYPE html> <html><head><title>Text Input Control</title></head><body><form>First name:  <input type=\"text\" name=\"first_name\" /><br>Last name:  <input type=\"text\" name=\"last_name\" /><br>User ID :  <input type=\"text\" name=\"user_id\" /><br>Password:  <input type=\"password\" name=\"password\" /> <input type=\"submit\" value=\"Submit\"> </form> </body> </html>")
                return

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER
        server.socket = ssl.wrap_socket (server.socket,
        keyfile='www.example.com.key.pem',
        certfile='www.example.com.cert.pem',ca_certs ='ca-chain.cert.pem', server_side=True)
	print server.socket
        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()











