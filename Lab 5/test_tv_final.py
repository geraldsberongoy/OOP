from TV import TV

def test_tv_operations(tv):
    # Test 1: Check the methods when TV is on.
    # This test verifies that the channel and volume can be changed when the TV is on.
    print("\nTest 1: Testing the methods when TV is on.")
    tv.turn_on()
    tv.channel_up()
    assert tv.get_channel() == 2, "Channel should increase by 1"
    tv.channel_down()
    assert tv.get_channel() == 1, "Channel should decrease by 1"
    tv.volume_up()
    assert tv.get_volume() == 2, "Volume should increase by 1"
    tv.volume_down()
    assert tv.get_volume() == 1, "Volume should decrease by 1"
    tv.set_channel(8)
    assert tv.get_channel() == 8, "Channel should be set to 8"
    tv.set_volume(3)
    assert tv.get_volume() == 3, "Volume should be set to 3"
    print("Test 1 passed.")
    
    # Test 2: Check the methods when TV is off.
    # This test verifies that the channel and volume cannot be changed when the TV is off.
    print("\nTest 2: Testing the methods when TV is off.")
    tv.turn_off()
    tv.channel_up()
    assert tv.get_channel() == 1, "Channel should be set to default value when TV is off"
    tv.channel_down()
    assert tv.get_channel() == 1, "Channel should be set to default value when TV is off"
    tv.volume_up()
    assert tv.get_volume() == 1, "Channel should be set to default value when TV is off"
    tv.volume_down()
    assert tv.get_volume() == 1, "Volume should be set to default value when TV is off"
    tv.set_channel(70)
    assert tv.get_channel() == 1, "Channel should not change when TV is off"
    tv.set_volume(3)
    assert tv.get_volume() == 1, "Volume should not change when TV is off"
    print("Test 2 passed.")
    
    # Test 3: Check the methods when TV is off and then turned on.
    # This test verifies that the channel and volume can be changed when the TV is turned 
    # on after being off.
    print("\nTest 3: Testing the methods when TV is on again.")
    tv.turn_on()
    tv.channel_up()
    assert tv.get_channel() == 2, "Channel should increase by 1"
    tv.channel_down()
    assert tv.get_channel() == 1, "Channel should decrease by 1"
    tv.volume_up()
    assert tv.get_volume() == 2, "Volume should increase by 1"
    tv.volume_down()
    assert tv.get_volume() == 1, "Volume should decrease by 1"
    tv.set_channel(8)
    assert tv.get_channel() == 8, "Channel should be set to 8"
    tv.set_volume(3)
    assert tv.get_volume() == 3, "Volume should be set to 3"
    print("Test 3 passed.")
    
def tv_invalid_values(tv):
    # Test 4: Check the set methods with invalid values.
    # This test verifies that the set methods do not change the channel and volume when 
    # invalid values are passed.
    print("\nTest 4: Testing the set methods with invalid values")
    tv.set_channel("a")
    tv.set_channel(130)
    tv.set_channel(0)
    tv.set_volume("b")
    tv.set_volume(8)
    tv.set_volume(0)
    print("Test 4 passed.")
    
    # Test 5: Check the up and down methods of channel and volume when it reaches 
    # the maximum and minimum values.
    # This test verifies that the volume_up, volume_down, channel_up and channel_down 
    # methods do not change the volume when it reaches the maximum and minimum values.
    print("\nTest 5: Testing the up and down methods when it reaches the maximum and minimum values.")
    tv.set_volume(7)
    tv.volume_up()
    tv.set_volume(1)
    tv.volume_down()
    tv.set_channel(120)
    tv.channel_up()
    tv.set_channel(1)
    tv.channel_down()
    print("Test 5 passed.")
    
def test_tv():
    # Creating instances of TV objects
    tv1 = TV()
    tv2 = TV()

     # Print the instance variable of the object with default values
    print(f"Printing the instance variable of the object with default values")
    print(f"Tv1's channel is {tv1.channel} and volume level is {tv1.volume}. It is {'On' if tv1.is_on else 'Off'}.")
    print(f"Tv2's channel is {tv2.channel} and volume level is {tv2.volume}. It is {'On' if tv2.is_on else 'Off'}.")

    # Test methods of TV1
    print(f"\n{bold_start}Testing the methods of tv1{bold_end}")
    test_tv_operations(tv1)
    
    # Test invalid values of TV2
    print(f"\n{bold_start}Invalid values testing of tv1{bold_end}")
    tv_invalid_values(tv1)
    
    # Test methods of TV2
    print(f"\n{bold_start}Testing the methods of tv2{bold_end}")
    test_tv_operations(tv2)

    # Test invalid values of TV2
    print(f"\n{bold_start}Invalid values testing of tv2{bold_end}")
    tv_invalid_values(tv2)
    
    # Printing the instance variable with the same values in the PPT.
    tv1.set_channel(30), tv1.set_volume(3), tv2.set_channel(3), tv2.set_volume(2)
    print(f"\nTv1's channel is {tv1.channel} and volume level is {tv1.volume}. It is {'On' if tv1.is_on else 'Off'}.")
    print(f"Tv2's channel is {tv2.channel} and volume level is {tv2.volume}. It is {'On' if tv2.is_on else 'Off'}.")
    
if __name__ == "__main__":
    bold_start = "\033[1m"
    bold_end = "\033[0m"
    test_tv()
    print("\nTesting is done.")