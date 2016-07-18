import socket

class Peer:

  def __init__(self, address, port, info_hash, peer_id, torrent):
    #if you pass the address and port in as a tuple the socket throws an error
    #but when you don't combine them until the connection it seems to work
    self.address = address
    self.port = port
    self.peer_id = peer_id
    self.torrent = torrent
    self.info_hash = info_hash
    self.pstr = "BitTorrent protocol"

    self.choked = True
    self.choking = True
    self.bitfield = None

  def connect(self):
    #I think I have the correct handshake, but the connection times out
    self.connection = socket.socket()
    self.connection.settimeout(0.5)
    try:
      self.connection.connect((self.address, self.port))
    except socket.timeout:
      print(self.address + " timed out")
    except socket.error:
      print(self.address + " socket error")
    
    self.connection.send(self.handshake())
    
    try:
      response = self.connection.recv(64)
      assert self.check_response(response)
    except AssertionError:
      print(self.address + " bad response")
    

  def handshake(self):
    h = b''.join([b'\x13', self.pstr.encode('ascii'), b'\x00\x00\x00\x00\x00\x00\x00\x00', self.info_hash, self.peer_id.encode('ascii')])
    return h

  def check_response(response):
    #This should check that their handshake returns the correct hash
    return True
