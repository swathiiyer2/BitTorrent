import peer
import pytest


info_hash = b'p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#'
peer_id = "RC0001rp7nl84gjs2n1k"

peer = peer.Peer("address", peer_id, info_hash)

def test_handshake():
  h = peer.handshake()
  assert h == b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#RC0001rp7nl84gjs2n1k'
  
