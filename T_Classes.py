class TDictionary:
    t_dict = {}

    def __init__(self, *args):
        # print(' *** init', args)
        self.input = args[0]
        # self.upd_dict()

    def upd_dict(self, *args):
        # print(' *** upd:', self.input, ' input:', in_put, len(in_put))
        if len(args) > 0:
            self.input = args[0]
        if isinstance(self.input, dict):
            for key in self.input.keys():
                self.t_dict.update({key: self.input.get(key)})
        else:
            print("arg is not dict type, but", type(self.input), '::', self.input)
            return

    def print_dict(self):
        for key in self.t_dict:
            print("%s >>> %s" % (key, self.t_dict.get(key)))


def update_dict(input):
    print(' *** update', input)
    if isinstance(input, dict):
        for key in input.keys():
            TDictionary.t_dict.update({key: input.get(key)})    # ссылка на какой-то другой t_dict
    else:
        print("arg is not dict type, but", type(input), '::', input)
        return
