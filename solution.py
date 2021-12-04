# import socket module
from socket import *
# In order to terminate the program


def webServer(port=13331):
  serversocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serversocket.bind(('', port))
  serversocket.listen(1)
  print('The server is ready to server:', port)

  while True:
    connectionsocket, addr = serversocket.accept()

    try:
      try:
        message = connectionsocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        f.close()
        response = 'HTTP/1.1 200 OK \r\n\r\n'
        connectionsocket.send(response.encode())
        for i in range(0, len(outputdata)):
          connectionsocket.send(outputdata[i].encode())
          print ('Got the page:', filename)
        connectionsocket.close()

      except IOError:
        print ('IOError')
        Didnotfind = 'HTTP/1.1 404 Not Found\r\n\r\n'
        connectionsocket.send(Didnotfind.encode())
        print ('404 NOT FOUND THE PAGE')
        outputdata = '404 NOT FOUND THE PAGE'
        for i in range(0, len(outputdata)):
          connectionsocket.send(outputdata[i].encode())
        connectionsocket.close()
    except (ConnectionResetError, BrokenPipeError):
      pass
  serversocket.close()
  sys.exit()
if __name__ == "__main__":
  webServer(13331)
