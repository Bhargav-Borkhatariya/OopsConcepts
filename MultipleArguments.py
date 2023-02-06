class MultipleArguments():

    def AddingList(self, *args):
        global List1
        List1 = []

        for obj in args:
            List1.append(obj)
        
        return print(List1)

objects = MultipleArguments()
objects.AddingList('hey', 'good', 'morning', ',', "What's", 'up', 112)
