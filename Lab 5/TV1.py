class TV:
    def __init__(self, channel: int = 1, volume: int = 1, on: bool = False):
        # Default values
        self.channel = 1
        self.volume = 1
        self.is_on = on

        # Set channel if within valid range
        if 1 <= channel <= 120:
            self.channel = channel
        else:
            print("Out of range channel. Assigning the channel to default channel (1).")
        
        # Set volume if within valid range
        if 1 <= volume <= 7:
            self.volume = volume
        else:
            print("Out of range volume level. Assigning the channel to default volume (1).")

    def show(self):
        if self.is_on:
            print(f"Channel: {self.channel}, Volume: {self.volume}, Power Status: {'On' if self.is_on else 'Off'}")
        else:
            print("TV is OFF. Turn it on to show the details.")

    def turn_on(self):
        self.is_on = True
        print("TV is now ON.")

    def turn_off(self):
        self.is_on = False
        print("TV is now OFF.")

    def get_channel(self):
        if self.is_on:
            return self.channel
        else:
            return "TV is OFF. Turn it on to get the channel."
    
    def get_volume(self):
        if self.is_on:
            return self.volume
        else:
            return "TV is OFF. Turn it on to get the volume."
        
    def set_channel(self, new_channel):
        if self.is_on:
            if 1 <= new_channel <= 120:
                self.channel = new_channel
                print(f"Channel set to {self.channel}.")
            else:
                print(f"Invalid channel. Please choose a channel between 1 and 120. The channel retains ({self.channel}).")
        else:
            print("TV is OFF. Turn it on to change the channel.")

    def set_volume(self, new_volume):
        if self.is_on:
            if 1 <= new_volume <= 7:
                self.volume = new_volume
                print(f"Volume set to {self.volume}.")
            else:
                print(f"Invalid volume. Please choose a volume between 1 and 7. The volume level retains ({self.volume}).")
        else:
            print("TV is OFF. Turn it on to change the volume.")

    def channel_up(self):
        if self.is_on:
            if self.channel == 120:
                print(f"Channel is at the maximum({self.channel}). Cannot increase further.")
            else:
                self.channel += 1
                print(f"Channel increased to {self.channel}.")
        else:
            print("TV is OFF. Turn it on to change the channel.")

    def channel_down(self):
        if self.is_on:
            if self.channel == 1:
                print(f"Channel is at the minimum({self.channel}). Cannot decrease further.")
            else:
                self.channel -= 1
                print(f"Channel decreased to {self.channel}.")  
        else:
            print("TV is OFF. Turn it on to change the channel.")

    def volume_up(self):
        if self.is_on:
            self.volume += 1
            print(f"Volume increased to {self.volume}.")
        else:
            print("TV is OFF. Turn it on to change the volume.")

    def volume_down(self):
        if self.is_on:
            self.volume -= 1
            print(f"Volume decreased to {self.volume}.")
        else:
            print("TV is OFF. Turn it on to change the volume.")
