import decoder
import connect

decoded = decoder.decodeFile("Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com] [mininova].torrent")
tracker = connect.Tracker(decoded.url, decoded.info_hash, decoded.left)
print("Peers: " + repr(tracker.tracker()))
print("info_hash: " + repr(decoded.info_hash))
print("peer_id: " + tracker.peer_id)
print("pstr: " + "BitTorrent protocol")





