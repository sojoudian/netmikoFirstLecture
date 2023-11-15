from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.20',
    'username': 'admin',
    'password': 'password',
    'port' : 22,
    'secret': 'secret',
}

net_connect = ConnectHandler(**cisco_device)
net_connect.enable()

# Sending configuration commands
config_commands = ['int loopback 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print(output)

net_connect.disconnect()
