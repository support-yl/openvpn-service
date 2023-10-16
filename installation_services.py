import os
import socket


class install_vpnserver():
    def __init__(self):
        hostname = socket.gethostname()
        installed_step = {
                          # 1: 'apt-get update -y && apt-get install tree net-tools -y',
                          # 2: 'apt-get install openvpn easy-rsa -y',
                          1: 'yum update -y && yum install tree net-tools epel-release screen -y && yum update -y && yum makecache -y',
                          2: 'yum install openvpn easy-rsa -y',
                          3: 'export easy_dir=`find /usr/share/ -name easyrsa` && cp -R `echo ${easy_dir%/*}` /etc/easy-rsa',
                          4: 'cd /etc/easy-rsa && tree && ./easyrsa init-pki && tree',
                          5: "cd /etc/easy-rsa && tree && echo 'installed ca private password, Please Input New private password On white board' && ./easyrsa build-ca",
                          6: "echo 'init success'",
                          7: 'cd /etc/easy-rsa && echo {0} | ./easyrsa gen-req server nopass'.format(hostname),
                          8: 'tree /etc/openvpn && echo create server.key in openvpn/server directory',
                          9: 'cd /etc/easy-rsa && ./easyrsa sign-req server server',
                          10: 'cd /etc/easy-rsa && ./easyrsa gen-dh && ./easyrsa gen-crl',
                          11: 'cd /etc/easy-rsa/pki && openvpn --genkey --secret ta.key',
                          12: 'cd /etc/easy-rsa/pki && {0}'.format(' && '.join(['cp /etc/easy-rsa/pki/ta.key /etc/openvpn/server/',
                                                                                'cp /etc/easy-rsa/pki/ca.crt /etc/openvpn/server/',
                                                                                'cp /etc/easy-rsa/pki/crl.pem /etc/openvpn/server/',
                                                                                'cp /etc/easy-rsa/pki/dh.pem /etc/openvpn/server/',
                                                                                'cp -r /etc/easy-rsa/pki/issued /etc/openvpn/server/',
                                                                                'cp -r /etc/easy-rsa/pki/private /etc/openvpn/server/'])),
                          # 13: 'zcat /usr/share/doc/openvpn/examples/sample-config-files/server.conf.gz | sudo tee /etc/openvpn/server.conf > /dev/null && mkdir /etc/openvpn/ccd'
                          13: 'mkdir -p /etc/openvpn/ccd && mkdir -p /var/log/openvpn && mkdir -p /etc/openvpn/share'
                         }
        comment_step = {
                        1: 'system update',
                        2: 'installed packages',
                        3: 'echo Note! Created easy-rsa directory',
                        4: '',
                        5: '',
                        6: '',
                        7: 'Create Server file',
                        8: 'Moving Server file to openvpn directory',
                        9: 'identification server',
                        10: 'Create server dh and crl file',
                        11: '',
                        12: 'Update openvpn/server directory',
                        13: 'Generate Server file'
                        }

        for step in installed_step:
            print(comment_step[step])
            for command in os.popen(installed_step[step], 'r'):
                print(command)
            print(step, 'End')
        return None


if __name__ == "__main__":
    print('')
else:
    install_vpnserver