from netmiko import ConnectHandler, NetmikoTimeoutException, NetmikoAuthenticationException

cisco_device = {
    'device_type': 'cisco_ios',
    'host':   '10.10.10.40',
    'username': 'admin',
    'password': 'wrongpassword',
    'port' : 22,
    'secret': 'secret',
}

try:
    net_connect = ConnectHandler(**cisco_device)
    net_connect.enable()
    output = net_connect.send_command('show run')
    print(output)
    net_connect.disconnect()
except NetmikoTimeoutException:
    print('Connection timed out.')
except NetmikoAuthenticationException:
    print('Authentication failure.')
