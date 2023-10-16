import os


class generator_Client():
    def __init__(self):
        if os.path.exists('/etc/openvpn/share/client.conf'):
            print('file exists')
        else:
            print('Generator Client file ok!')
            with open('/etc/openvpn/share/client.conf', 'w') as create_file:
                create_file.write(self.generator_client())
                create_file.close()

    def generator_client(self):
        generator = """##############################################
# Sample client-side OpenVPN 2.0 config file #
# for connecting to multi-client server.     #
#                                            #
# This configuration can be used by multiple #
# clients, however each client should have   #
# its own cert and key files.                #
#                                            #
# On Windows, you might want to rename this  #
# file so it has a .ovpn extension           #
##############################################
client

dev tun

proto udp

float

remote {server} {port}

resolv-retry infinite

nobind

persist-key
persist-tun

ca {ca_file}
cert {client_crt}
key {client_key}

remote-cert-tls server

cipher AES-256-GCM

verb 3"""
        return generator


if __name__ == "__main__":
    print('')
else:
    generator_Client