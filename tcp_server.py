import socket
import socketserver
import logging

def main():
    LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename="C:\\Users\\Admin\\Desktop\\tcpserver.log", level=logging.DEBUG,format=LOG_FORMAT)
    logger=logging.getLogger()

    host='127.0.0.1'
    port = 5000
    #socket creation
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket created!")
    logger.info("socket created!")

    #binding connection
    s.bind((host,port))
    logger.info("Binded the host with port 5000")
    #listening on port 5000
    s.listen(1)
    print("waiting for clients")
    conn, addr = s.accept()


if __name__ == "__main__":
    main()