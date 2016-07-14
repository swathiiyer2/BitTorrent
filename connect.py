import requests
from bcoding import bencode, bdecode
from random import choice
from string import ascii_lowercase, digits

class Tracker():
  def __init__(self, url, info_hash, left, uploaded=0, downloaded=0):
    self.announce_url = url
    self.info_hash = info_hash
    self.uploaded = uploaded
    self.downloaded = downloaded
    self.left = left

    
  def make_params(self):
    self.peer_id = self.make_id()
    port = "9999"
    return {
      "info_hash": self.info_hash,
      "peer_id": self.peer_id,
      "port": port,
      "uploaded": self.uploaded,
      "downloaded": self.downloaded,
      "left": self.left}

  
  def tracker(self):
    params_dict = self.make_params()
    r = requests.get(self.announce_url, params=params_dict)
    self.response = bdecode(r.content)
    bin_string = self.response['peers']
    peer_array = []
    for n in range(0,len(bin_string), 6): 
        array_string = ""
        array_string += str(bin_string[n]) + '.' + str(bin_string[n+1])+'.'+str(bin_string[n+2])+'.'+str(bin_string[n+3])
        array_string += ":" + str(bin_string[n + 4] * 256 + bin_string[n + 5]) 
        peer_array.append(array_string) 
    return peer_array
    
  def make_id(self):
    id = "RC0001"
    for _ in range(14):
      id+= choice(list(ascii_lowercase + digits))
    return id
    
    
