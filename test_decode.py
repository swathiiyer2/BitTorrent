import pytest
import decoder

d = decoder.decodeFile("Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com] [mininova].torrent")

def test_url():
  assert d.url ==  "http://tracker.mininova.org/announce"

def test_info():
  assert type(d.info) == dict

def test_info_hash():
  assert d.info_hash == "p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#"


