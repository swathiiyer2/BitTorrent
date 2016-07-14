import pytest
import decoder

d = decoder.decodeFile("Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com] [mininova].torrent")

def test_url():
  assert d.url ==  "http://tracker.mininova.org/announce"

def test_info():
  assert type(d.info) == dict

i = {'files': [{'length': 291, 'path': ['Distributed by Mininova.txt']},
  {'length': 7254786,
   'path': ['Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com].zip']}],                                                                   
 'name': 'Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com]',                                                                             
 'piece length': 1048576,
 'pieces': b'\xf0.U\xf8\xe6\xc5KM\xb6\n:\x9d\xd3\xa6\xcf\xfa\xce~\x9f\xce\xd7zjN\xb4\x9a\xf8\xdc8TC\xf3\x0f\x8fok\xf4\xc9\xc7R\x9d\x04\xf8\x19\xa6r\xd7\xe2\xc1\xa9r\x9d(L\xa6o"\x1ak\xbf$\xe6\x14\xc5\xa6\xe9N\x0b\x18\x1d\xd9\xfbc\nDj\xc7n>7\x97y\xec5?I\x1c\xf0\xf3\x81\x80\x07\xb8\x98\xfc\x93\x9f\x154\xe8\x87HQ\xd8\xfc\xc6\x9bwO\x84\xec\x10\xf7\x9d\xf9\xcb\xd6\xc55\xb6\xe3\xcd}H\xd9\xf2\xfe\x19\xabs\xe8\xc7XMR+w'}

def test_info2():
  assert d.info == i


