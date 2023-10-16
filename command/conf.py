import yaml


class conver():
    def configure(self, info):
        return yaml.load(info, yaml.FullLoader)

    def convert(self, configure):
        conf = [int(x) for x in configure.split(', ')]
        info = ''
        for conv_conf in conf:
            info += chr(conv_conf)
        return info


if __name__ == "__main__":
    print('')
else:
    conver()