class TV:
    """TV class with the following attributes:"""
    def __init__(self, channel: int = 1, volume: int = 1, on: bool = False):
        """Sets the initial values of the TV object."""
        # Default values if the TV is on and the values are out of range
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
            print("Out of range volume level. Assigning the volume to default volume (1).")

    def turn_on(self):
        """Turns the TV on by setting the is_on attribute to True."""
        self.is_on = True
        print("TV is now ON.")

    def turn_off(self):
        """
        Turns the TV off by setting the is_on attribute to False.
        Also resets the channel and volume to their default values.
        """
        self.is_on = False
        self.channel = 0
        self.volume = 0
        print("TV is now OFF. Channel and volume have been reset.")

    def get_channel(self):
        """
        Returns the current channel if the TV is on. 
        If the TV is off, it returns a message indicating that the TV is off.
        """     
        if self.is_on:
            return self.channel
        else:
            return "TV is OFF. Turn it on to get the channel."
    
    def get_volume(self):
        """
        Returns the current volume if the TV is on. 
        If the TV is off, it returns a message indicating that the TV is off.
        """
        if self.is_on:
            return self.volume
        else:
            return "TV is OFF. Turn it on to get the volume."
        
    def set_channel(self, new_channel):
        """
        Sets the TV to a new channel if the TV is on and the new channel is within the valid range (1-120).
        If the TV is off or the new channel is not within the valid range, it prints an appropriate message.
        """
        if self.is_on:
            if 1 <= new_channel <= 120:
                self.channel = new_channel
                print(f"Channel set to {self.channel}.")
            else:
                print(f"Invalid channel. Please choose a channel between 1 and 120. The channel retains ({self.channel}).")
        else:
            print("TV is OFF. Turn it on to change the channel.")

    def set_volume(self, new_volume):
        """
        Sets the TV to a new volume if the TV is on and the new volume is within the valid range (1-100).
        If the TV is off or the new volume is not within the valid range, it prints an appropriate message.
        """
        if self.is_on:
            if 1 <= new_volume <= 7:
                self.volume = new_volume
                print(f"Volume set to {self.volume}.")
            else:
                print(f"Invalid volume. Please choose a volume between 1 and 7. The volume level retains ({self.volume}).")
        else:
            print("TV is OFF. Turn it on to change the volume.")

    def channel_up(self):
        """Inceases the channel by 1 if the TV is on and the channel is not at the maximum(120)."""
        if self.is_on:
            if self.channel == 120:
                print(f"Channel is at the maximum({self.channel}). Cannot increase further.")
            else:
                self.channel += 1
                print(f"Channel increased to {self.channel}.")
        else:
            print("TV is OFF. Turn it on to change the channel.")

    def channel_down(self):
        """Decreases the channel by 1 if the TV is on and the channel is not at the minimum(1)."""
        if self.is_on:
            if self.channel == 1:
                print(f"Channel is at the minimum({self.channel}). Cannot decrease further.")
            else:
                self.channel -= 1
                print(f"Channel decreased to {self.channel}.")  
        else:
            print("TV is OFF. Turn it on to change the channel.")

    def volume_up(self):
        """Increases the volume by 1 if the TV is on and the volume is not at the maximum(7)."""
        if self.is_on:
            if self.volume == 7:
                print(f"Volume is at the maximum({self.volume}). Cannot increase further.")
            else:
                self.volume += 1
                print(f"Volume increased to {self.volume}.")
        else:
            print("TV is OFF. Turn it on to change the volume.")

    def volume_down(self):
        """Decreases the volume by 1 if the TV is on and the volume is not at the minimum(1)."""
        if self.is_on:
            if self.volume == 1:
                print(f"Volume is at the minimum({self.volume}). Cannot decrease further.")
            else:
                self.volume -= 1
                print(f"Volume decreased to {self.volume}.")
        else:
            print("TV is OFF. Turn it on to change the volume.")
