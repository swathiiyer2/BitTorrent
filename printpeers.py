import decoder, ipaddress

binstring = decoder.testTorrent.peers
print(binstring)

peer_dict = {}

for n in range(0,len(binstring), 6):
    newIP = str(binstring[n]) + '.' + str(binstring[n+1])+'.'+str(binstring[n+2])+'.'+str(binstring[n+3])
    print(newIP)
=======
import decoder
import requests

bin_string = decoder.testTorrent.peers

peer_array = []

for n in range(0,len(bin_string), 6):
    array_string = ""
    array_string += str(bin_string[n]) + '.' + str(bin_string[n+1])+'.'+str(bin_string[n+2])+'.'+str(bin_string[n+3])
    array_string += ":" + str(bin_string[n + 4] * 256 + bin_string[n + 5])
    peer_array.append(array_string)

print(peer_array)
>>>>>>> origin/parsepeers
