import connect
import pytest

url = "http://tracker.mininova.org/announce"
info_hash =  "p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#"
left = 8

tracker = connect.Tracker(url, info_hash, left)

def test_request_hash():
  params_dict = tracker.make_params();
  assert params_dict['downloaded'] ==  0
  assert params_dict['info_hash'] == 'p\xff\xeeh_\x14\x93BHd\xab\x1b\xe5I\x1b\x8f\xdc3^#'
  assert params_dict['left'] == 8
  assert len(params_dict['peer_id']) == 20
  assert params_dict['port'] == '9999'
  assert params_dict['uploaded'] == 0
