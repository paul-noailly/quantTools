import json
import socket
import logging
import time
import ssl



class JsonSocket(object):
    def __init__(self, config, port, encrypt = False):
        self._ssl = encrypt 
        if self._ssl != True:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket = ssl.wrap_socket(sock)
        self.conn = self.socket
        self._config = config
        self._timeout = None
        self._address = config['clients']['xtb']['connection']['adress']
        self._port = port
        self._max_conn_tries = config['clients']['xtb']['connection']['max_conn_tries']
        self._forced_delay_ms_between_requests = config['clients']['xtb']['connection']['forced_delay_ms_between_requests']
        self._decoder = json.JSONDecoder()
        self._receivedData = ''
        
        # logging
        self.logger = logging.getLogger("jsonSocket")
        FORMAT = '[%(asctime)-15s][%(funcName)s:%(lineno)d] %(message)s'
        logging.basicConfig(format=FORMAT)
        if config['clients']['xtb']['logging']['debug']:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.CRITICAL)
            

    def connect(self):
        for i in range(self._max_conn_tries):
            try:
                self.socket.connect( (self.address, self.port) )
            except socket.error as msg:
                self.logger.error("SockThread Error: %s" % msg)
                time.sleep(0.25);
                continue
            self.logger.info("Socket connected")
            return True
        return False

    def _sendObj(self, obj):
        msg = json.dumps(obj)
        self._waitingSend(msg)

    def _waitingSend(self, msg):
        if self.socket:
            sent = 0
            msg = msg.encode('utf-8')
            while sent < len(msg):
                sent += self.conn.send(msg[sent:])
                self.logger.info('Sent: ' + str(msg))
                time.sleep(self._forced_delay_ms_between_requests/1000)

    def _read(self, bytesSize=4096):
        if not self.socket:
            raise RuntimeError("socket connection broken")
        while True:
            char = self.conn.recv(bytesSize).decode()
            self._receivedData += char
            try:
                (resp, size) = self._decoder.raw_decode(self._receivedData)
                if size == len(self._receivedData):
                    self._receivedData = ''
                    break
                elif size < len(self._receivedData):
                    self._receivedData = self._receivedData[size:].strip()
                    break
            except ValueError as e:
                continue
        # self.logger.info('Received: ' + str(resp))
        return resp

    def _readObj(self):
        msg = self._read()
        return msg

    def close(self):
        self.logger.debug("Closing socket")
        self._closeSocket()
        if self.socket is not self.conn:
            self.logger.debug("Closing connection socket")
            self._closeConnection()

    def _closeSocket(self):
        self.socket.close()

    def _closeConnection(self):
        self.conn.close()

    def _get_timeout(self):
        return self._timeout

    def _set_timeout(self, timeout):
        self._timeout = timeout
        self.socket.settimeout(timeout)

    def _get_address(self):
        return self._address

    def _set_address(self, address):
        pass

    def _get_port(self):
        return self._port

    def _set_port(self, port):
        pass

    def _get_encrypt(self):
        return self._ssl

    def _set_encrypt(self, encrypt):
        pass

    timeout = property(_get_timeout, _set_timeout, doc='Get/set the socket timeout')
    address = property(_get_address, _set_address, doc='read only property socket address')
    port = property(_get_port, _set_port, doc='read only property socket port')
    encrypt = property(_get_encrypt, _set_encrypt, doc='read only property socket port')
    