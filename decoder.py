from bcoding import bencode, bdecode
from hashlib import sha1


class decodeFile():
  def __init__(self, torrent):
    self.inputURL = torrent
    self.decodeFile()

  def decodeFile(self):
    f = open(self.inputURL, "rb")
    d = bdecode(f.read())
    self.url = d['announce']
    self.info = d['info']
    self.info_hash = sha1(bencode(self.info)).digest()
    self.left = str(self.info['files'][1]['length'])
