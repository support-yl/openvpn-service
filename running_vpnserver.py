import os
import operation
import command.conf as run
import installation_services

if __name__ == "__main__":
    while True:
        if os.path.exists('/etc/openvpn/server.conf'):
            print('server file exists')
            for command_re in os.popen("wc -l /etc/openvpn/server.conf | awk -F \" \" {'print $1'}", "r"):
                if command_re > '1':
                    if os.path.exists('/usr/lib/systemd/system/vpn-server.service'):
                        print('start openvpn server')
                        os.system('systemctl daemon-reload')
                        os.system('systemctl restart vpn-server.service')
                        exit(0)
                    else:
                        os.system('echo "{0}" > /usr/lib/systemd/system/vpn-server.service'.\
                                  format(run.conver().convert(open('environments/linux_server').read())))
                        print('create vpn service')
                else:
                    print('update service file')
                    operation.generator(True)

        else:
            if os.path.exists('/etc/openvpn'):
                print('Create New server file')
                os.system('touch /etc/openvpn/server.conf')
            else:
                print('recreate service')
                installation_services.install_vpnserver()
                operation.generator(False)
