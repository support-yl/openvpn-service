import re
import yaml
import generator_client


class generator():
    def __init__(self, bool_parameter, path='/etc/openvpn/server.conf'):
        if bool_parameter:
            update = open(path, 'w')
            update.write(self.configure_info())
            update.close()
            print('Update server file OK!')
        else:
            create = open(path, 'w')
            create.write(self.configure_info())
            create.close()
            print('create server file OK!')

    def configure_info(self):
        list = ['port', 'proto', 'dev', 'dh', 'server']
        comment_configure = {'port': {'comment': 'PLease Input service port max 65535, default 1194',
                                      'default': '1194'},
                             'proto': {'comment': 'PLease Setting service transfer proto udp/tcp, default udp',
                                       'default': 'udp'},
                             'dev': {'comment': 'PLease Input vpn server type tun/tap, default tun',
                                     'default': 'tun'},
                             'dh': {'comment': 'PLease Setting dh file Path, default in server directory',
                                    'default': '/etc/openvpn/server/dh.pem'},
                             'server': {'comment': 'Please Setting service address pool, default network segment 10.8.0.0/24',
                                        'default': '10.8.0.0 255.255.255.0'}}
        dicta = {'float': '',
                 'ca': '/etc/openvpn/server/ca.crt',
                 'cert': '/etc/openvpn/server/issued/server.crt',
                 'key': '/etc/openvpn/server/private/server.key',
                 'topology': 'subnet',
                 'ifconfig-pool-persist': '/var/log/openvpn/ipp.txt',
                 'client-config-dir': '/etc/openvpn/ccd',
                 'client-to-client': '',
                 'keepalive': '10 120',
                 'cipher': 'AES-256-GCM',
                 'persist-key': '',
                 'persist-tun': '',
                 'status': '/var/log/openvpn/openvpn-status.log',
                 'log-append': '/var/log/openvpn/openvpn.log',
                 'verb': '3',
                 'explicit-exit-notify': '1'}
        print("Note! if you want to undo operation Please input 'q'.")
        for input_info in list:
            try:
                print(comment_configure[input_info]['comment'])
                info = input('Please input {0}\n:'.format(input_info))
                if info == comment_configure[input_info]['default'] or info == '':
                    dicta[input_info] = comment_configure[input_info]['default']
                if info != comment_configure[input_info]['default'] and re.sub(' +', '', info) != '':
                    dicta[input_info] = info
                if re.sub(r' +', '', dicta[input_info].lower()) == 'q' or re.sub(r' +', '', dicta[input_info].lower()) == 'exit':
                    exit(0)
            except:
                exit(0)
        generator_client.generator_Client()
        return '{0}'.format(yaml.dump(dicta)).replace(':', '').replace("'", "")


if __name__ == "__main__":
    print('')
else:
    generator