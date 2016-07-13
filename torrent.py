

class Torrent():

  def __init__(self, info):
    self.uploaded = 0
    self.downloaded = 0
    self.length = info['files'][1]['length']
    self.left = self.length - self.downloaded
