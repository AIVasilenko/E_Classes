import os.path

AppConfig = {}


class FlConfig:
    def __init__(self, path):
        self.path = path
        self.abspath = os.path.abspath(path)
        print(' ** ', self.abspath)

    def read_config(self):
        try:
            with open(self.abspath) as fp:
                print(' ** working on ', self.abspath)
                for line in fp:
                    if not line.startswith('#'):
                        line = line.replace('\n', '')
                        body = line.split('#')  # eliminate possible comment
                        body = body[0].split(':')  # extract key and value
                        AppConfig.update({body[0]: body[1]})
        except FileNotFoundError as nf:
            print("%s: %s" % (nf.strerror, self.abspath))

    def get_config(self):
        if len(AppConfig) == 0:
            print("Empty config")
            return
        for key in AppConfig.keys():
            print("%s --> %s" % (key, AppConfig.get(key)))
            # print("{} ==> {}".format(key, AppConfig.get(key)))


class Parallel:  # from python.pdf, 9.7.2 Классы-помощники
    def __init__(self, *args):
        self.__args = args
        print('args:', self.__args)

    def __getitem__(self, item):
        # print(item, '::', list(map(lambda s, i=item: s[i], self.__args)))
        return list(map(lambda s, i=item: s[i], self.__args))
