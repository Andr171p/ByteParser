import json


class TestProtocol:
    @staticmethod
    def parse(data: bytes) -> dict:
        packet = {
            'num_pack': data[0],
            'type_message': data[1],
            'imei': data[2:17].decode('utf-8'),
            'datetime': int.from_bytes(data[17:21], byteorder='little'),
            'lat': float.fromhex(data[21:25].hex()),
            'lon': float.fromhex(data[25:29].hex())}

        if packet['type_message'] == 2:
            packet['code_msg'] = data[29]

        return packet


inputs = [
    b'\x00\x01869586748696585\xfa\x12\xedfc.VB\xaaEB',
    b'\x01\x01869586748696585\t\x15\xedf\x1b/VBBEB',
    b'\x02\x02869586748696585+\x15\xedf\x9e/VB\xbe_EB\x03'
]
result = {
    'data': []
}
for inp in inputs:
    result['data'].append(TestProtocol.parse(data=inp))

with open('result.json', 'w', encoding='utf-8') as file:
    _json = json.dumps(result, indent=4, ensure_ascii=False)
    json.dump(_json, file)