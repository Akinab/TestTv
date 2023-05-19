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

