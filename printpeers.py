import decoder
import connect

decoded = decoder.decodeFile("Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com] [mininova].torrent")
tracker = connect.Tracker(decoded.url, decoded.info_hash, decoded.left)
pstr = 'BitTorrent protocol'

print("Peers: " + repr(tracker.tracker()))
print("info_hash: " + repr(decoded.info_hash))
print("peer_id: " + tracker.peer_id)
print("pstr: " + pstr)

def save_packet_to(fname, data):
  with open(fname, 'wb') as f:
    f.write(data)

print(repr(tracker.peer_id))
handshake = b''.join([b'\x13', pstr.encode('ascii'), b'\x00\x00\x00\x00\x00\x00\x00\x00', decoded.info_hash, tracker.peer_id.encode('ascii')])
print(handshake)

save_packet_to('/tmp/packet.raw', handshake)
