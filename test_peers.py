from peer import Peer
import pytest


info_hash = b'p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#'
peer_id = "RC0001rp7nl84gjs2n1k"

peer = Peer("address", "port", peer_id, info_hash, "torrent")

def test_handshake():
  h = peer.handshake()
  assert h == b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#RC0001rp7nl84gjs2n1k'


from connect import Tracker
from decoder import decodeFile as Decoder
from test_decode import d

#d = Decoder("tom.torrent")

infohash = d.info_hash
url = d.url
left = d.left

tracker = Tracker(url, infohash, left)
