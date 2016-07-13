import decoder, ipaddress

binstring = decoder.testTorrent.peers
print(binstring)

peer_dict = {}

for n in range(0,len(binstring), 6):
    newIP = str(binstring[n]) + '.' + str(binstring[n+1])+'.'+str(binstring[n+2])+'.'+str(binstring[n+3])
    print(newIP)
