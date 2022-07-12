class Thought:
    def __init__(self, name, weight_things, *things):
        self.name = name
        self.weight_things = weight_things
        self.things = list(things)
        self.count = 0

    def overturn(self, weight_body):
        if self.count == 0:
            self.weight_things = self.weight_things * weight_body
        else:
            self.weight_things = self.weight_things // weight_body
            self.count = 0

    def add_topic(self, think):
        self.things.append(think)


if __name__ == '__main__':
    th = Thought('Jack', 20)
    # th.add_topic('job')
    # print(th)
    # th.overturn(3)
    # print(th)
    # th.overturn(11)
    # print(th)
    # th.overturn(4)
    # print(th)
