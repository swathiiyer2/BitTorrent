from bcoding import bencode, bdecode


class decodeFile():
  def __init__(self, torrent):
    self.inputURL = torrent
    self.decodeFile()

  def decodeFile(self):
    f = open(self.inputURL, "rb")
    d = bdecode(f.read())
    self.url = d['announce']
    self.info = d['info']
