import iperf3 

client = iperf3.Client()
client.server_hostname = '192.168.1.113'
client.port = 37707
result = client.run()
speed = result.sent_Mbps

print(speed)

min_speed = 50 # mbit/s

def test_speed():
    assert speed >= min_speed, "can't use connection"
    return "connection well"
