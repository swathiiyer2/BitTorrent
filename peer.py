import socket

class Peer:

  def __init__(self, address, info_hash, peer_id, torrent):
    self.address = address
    self.peer_id = peer_id
    self.torrent = torrent
    self.info_hash = info_hash
    self.pstr = "BitTorrent protocol"

    self.choked = True
    self.choking = True
    self.bitfield = None

  def connect(self):
    self.connection = socket.socket()
    self.connection.settimeout(0.5)
    try:
      self.connection.connect(self.address)
    except socket.timeout:
      print(self.address + " timed out")
    except socket.error:
      print(self.address + " socket error")
    except:
      raise Exception
    self.connection.send(self.handshake())

    try:
      response = self.connection.recv(64)
      assert self.check_response(response)
    except AssertionError:
      print(self.address + " bad response")
    except:
      raise Exception

  def handshake(self):
    h = b''.join([b'\x13', self.pstr.encode('ascii'), b'\x00\x00\x00\x00\x00\x00\x00\x00', self.info_hash, self.peer_id.encode('ascii')])
    return h

  def check_response(response):
    return True
