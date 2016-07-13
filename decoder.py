from bcoding import bencode, bdecode
from pprint import pprint
from hashlib import sha1
from string import ascii_lowercase, digits
from random import choice
import requests


class decodeFile():
  def __init__(self, inputURL):
    self.inputURL = inputURL
    self.decodeFile()
    self.tracker()

  def decodeFile(self):
    f = open(self.inputURL, "rb")
    d = bdecode(f.read())
    self.url = d['announce']
    self.info = d['info']
    self.reencoded = bencode(self.info)

  def tracker(self):
    info_hash = sha1(self.reencoded).digest()
    peer_id = self.make_id()
    port = "9999"
    uploaded = "0"
    downloaded = "0"
    left = str(self.info['files'][1]['length'])
    request_hash = {
      "info_hash": info_hash,
      "peer_id": peer_id,
      "port": port,
      "uploaded": uploaded,
      "downloaded": downloaded,
      "left": left}
    r = requests.get(self.url, params=request_hash)

    print(r.content)

  def make_id(self):
    id = "RC0001"
    for _ in range(14):
      id+= choice(list(ascii_lowercase + digits))
    return id
    

      

testTorrent = decodeFile("Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com] [mininova].torrent")

