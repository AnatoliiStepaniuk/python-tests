import json
import requests

# curl -X POST https://api.converter.tektelic-dev.com/decode -d '{"type":"TEK_HOME_BASE","port":10,"hex":"0468140100ff08040005"}'
URL = 'https://api.converter.tektelic-dev.com/decode'


def test_humidity():
    payload = {"type": "TEK_HOME_BASE", "port": 10, "hex": "0468140100ff08040005"}
    resp = requests.post(URL, json.dumps(payload))
    body = json.loads(resp.text)
    assert resp.status_code == 200
    assert body["port"] == 10
    assert body["relative_humidity"] == 10


test_humidity()