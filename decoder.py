from bencode import bencode, bdecode
import requests
from pprint import pprint
from hashlib import sha1

class decodeFile():

	def __init__(self, inputURL):
		self.inputURL = inputURL
		self.decodeFile()
		self.tracker()

	def decodeFile(self):
		f = open(self.inputURL, "rb")
		d = bdecode(f.read())
		#print d
		#print d['announce']
		self.url = d['announce']
		self.info = d['info']
		#print ("self.info", self.info)
		self.reencoded = bencode(self.info)
		#print "+++++++++++++++"
		#print self.reencoded
		#print "+++++++++++++++"

	def tracker(self):
		info_hash = str(sha1(self.reencoded))
		peer_id = "-UM1870-%92%a5Y%04e_%22%d2w%1a%87%23"
		port = "9999"
		uploaded = "0"
		downloaded = "0"
		left = str(self.info['files'][1]['length'])
		requestString = (self.url + 
			'?info_hash=' + info_hash + 
			"&peer_id=" + peer_id + 
			"&port=" + port + 
			"&uploaded=" + uploaded +
			"&downloaded=" + downloaded +
			"&left=" + left)
		print ("rq", requestString)
		r = requests.get(requestString)

		print r.status_code

testTorrent = decodeFile("Marcus Williams.Miles.Davis.Marcus.Miller.Live.In.Paris.[mp3_192k].[www.mywpmusic.com] [mininova].torrent")

