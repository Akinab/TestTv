def details ():
    Description = "Test TV"
    Date = "05-19-23"
    print ("\nDescription: {}\nDate: {}".format (Description , Date))
    
details ()

class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1

    def get_channel(self):
        return self.channel
    
    def set_channel(self, channel):
        self.channel = channel

    def get_volume_level(self):
        return self.volume_level
    
    def set_volume_level(self, volume_level):
        self.volume_level = volume_level


class TestTV:
    def __init__(self):
        self.tv1 = TV()
        self.tv2 = TV()

    def run(self):
        self.tv1.set_channel(30)
        self.tv1.set_volume_level(3)
        self.tv2.set_channel(3)
        self.tv2.set_volume_level(2)

        print("\ntv1's channel is", self.tv1.get_channel(), "and volume level is", self.tv1.get_volume_level())
        print("\ntv2's channel is", self.tv2.get_channel(), "and volume level is", self.tv2.get_volume_level())
