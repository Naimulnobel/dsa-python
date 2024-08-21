import time
import json
import random
def update_timestamps(sn, json_data):
    current_timestamp = int(time.time())
    
    # Update the 'sn' field in 'devID'
    if 'devID' in json_data and 'sn' in json_data['devID']:
        json_data['devID']['sn'] = sn
    
    # Update the 'ts' field
    if 'ts' in json_data:
        json_data['ts'] = current_timestamp
    
    # Update the 'errC' list
    if 'errC' in json_data:
        for err in json_data['errC']:
            if 'ts' in err:
                err['ts'] = current_timestamp
    
    # Update the 'Cook' list
   
    
    return json.dumps(json_data)

# Example usage:
json_data = {
        "devID": {
            "sn": 'saint000000213',
            "FW": "1v01",
            "pt": "2",
            "mc": "0x01",
            "sid": "89185002210602354603",
            "loc": "24.3637282, 42.232323, 2.89",
            "Ip": {
                "IpAddress": "49.182.140.130"
            }
        },
        "ts": int(time.time()),
        "stat": {
            "Vg": str(random.randint(100, 200)),
            "Ag": "10",
            "BatV": str(round(random.uniform(1, 5), 1)),
            "STL": "5x4x2",
            "stvcnt":"3"
        },
        "errC":[
            {
            "ts":"1664313161",
            "err":"2"
            },
            {
            "ts":"1664313161",
            "err":"4"
            },
            {
            "ts":"1664313161",
            "err":"1"
            },
            {
            "ts":"1664313161",
            "err":"4"
            }
        ],
        # "errC": "232",
        "Cook": [
            {
                "pan": "L",
                "onT": 1711991985,
                "offT": 1711992305,
                "pwr": 1200,
                "pwrC" : 20.5,
                
            },
            {
                "pan": "R",
                "onT": 1711990205,
                "offT": 1711992005,
                "pwr": 800,
                "pwrC" : 16,
               
            },
            {
                "pan": "R",
                "onT": 1711992905,
                "offT": 1711993205,
                "pwr": 1800,
                "pwrC" : 22.5,
                
            },
            {
                "pan": "L",
                "onT": 1711992965,
                "offT": 1711993265,
                "pwr": 1400,
                "pwrC" : 21,
                
            },
            {
                "pan": "R",
                "onT": 1711994700,
                "offT": 1711995480,
                "pwr": 1000,
                "pwrC" : 19,
                
            },
            {
                "pan": "L",
                "onT": 1711994400,
                "offT": 1711995900,
                "pwr": 600,
                "pwrC" : 14,
                
            }
        ],
        "status":"connected",
        "GSMsignalStrength":"89"
}

# Update the timestamps
updated_json = update_timestamps('saint000000213', json_data)
print(updated_json)