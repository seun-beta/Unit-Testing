
class Fish:

    def __init__(self, first_name, last_name='Fish', skeleton='bone',
                 eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def swim(self):
        return "The fish is swimming."

    def swim_backwards(self):
        return "The fish can swim backwards."


class Trout(Fish):
    def __init__(self, water='freshwater'):
        self.water = water
        super().__init__(self)


class Clownfish(Fish):

    def live_with_anemone(self):
        print("The clownfish coexists with sea anemone")


class Shark(Fish):

    def __init__(self, first_name, last_name='Shark', skeleton='cartilage',
                 eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
