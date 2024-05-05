class TV:
    """TV class with the following attributes:"""
    def __init__(self, channel: int = 1, volume: int = 1, on: bool = False):
        """Sets the initial values of the TV object."""
        self.channel = channel
        self.volume = volume
        self.is_on = on

    def turn_on(self):
        """Turns the TV on by setting the is_on attribute to True."""
        self.is_on = True

    def turn_off(self):
        """
        Turns the TV off by setting the is_on attribute to False.
        Also resets the channel and volume to their default values.
        """
        self.is_on = False
        self.channel = 1
        self.volume = 1
        
    def get_channel(self):
        """
        Returns the current channel if the TV is on. 
        If the TV is off, it returns a message indicating that the TV is off.
        """     
        if self.is_on:
            return self.channel
        else:
            return 1
    
    def get_volume(self):
        """
        Returns the current volume if the TV is on. 
        If the TV is off, it returns a message indicating that the TV is off.
        """
        if self.is_on:
            return self.volume
        else:
            return 1
        
    def set_channel(self, new_channel):
        """
        Sets the TV to a new channel if the TV is on and the new channel is within the valid range (1-120).
        If the TV is off or the new channel is not within the valid range, print a message.
        """
        if not isinstance(new_channel, int):
            print("Input only integers. Please enter an integer between 1 and 120.")
        
        else:
            if self.is_on:
                if 1 <= new_channel <= 120:
                    self.channel = new_channel
                else:
                    print("Invalid channel number. Please enter a number between 1 and 120.")

    def set_volume(self, new_volume):
        """
        Sets the TV to a new volume if the TV is on and the new volume is within the valid range (1-100).
        If the TV is off or the new volume is not within the valid range, print a message.
        """
        if not isinstance(new_volume, int):
            print("Input only integers. Please enter an integer between 1 and 7.")
        
        else:
            if self.is_on:
                if 1 <= new_volume <= 7:
                    self.volume = new_volume
                else:
                    print("Invalid volume number. Please enter a number between 1 and 7.")

    def channel_up(self):
        """Inceases the channel by 1 if the TV is on and the channel is not at the maximum(120)."""
        if self.is_on:
            if self.channel != 120:
                self.channel += 1
            else:
                print("Invalid channel number. Please enter a number between 1 and 120.")

    def channel_down(self):
        """Decreases the channel by 1 if the TV is on and the channel is not at the minimum(1)."""
        if self.is_on:
            if self.channel != 1:
                self.channel -= 1
            else:
                print("Invalid channel number. Please enter a number between 1 and 120.")

    def volume_up(self):
        """Increases the volume by 1 if the TV is on and the volume is not at the maximum(7)."""
        if self.is_on:
            if self.volume != 7:
                self.volume += 1
            else:
               print("Volume is at the maximum. Cannot increase further.")

    def volume_down(self):
        """Decreases the volume by 1 if the TV is on and the volume is not at the minimum(1)."""
        if self.is_on:
            if self.volume != 1:
                self.volume -= 1
            else:
                print("Volume is at the minimum. Cannot decrease further.")