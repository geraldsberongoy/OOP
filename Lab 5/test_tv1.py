from TV import TV

def test_tv():
    
    # \033[1m starts bold, \033[0m resets to normal
    bold_start = "\033[1m"
    bold_end = "\033[0m"

    # Case 1
    # Creating instances of TV objects
    print(f"\n{bold_start}Case 1:{bold_end} Creating instances of TV objects")
    tv1 = TV(30, 8, True)
    tv2 = TV(0, 2, True)
    
    # Print the instance variable of the object
    print(f"Tv1's channel is {tv1.channel} and volume level is {tv1.volume}. It is {'On' if tv1.is_on else 'Off'}.")
    print(f"Tv2's channel is {tv2.channel} and volume level is {tv2.volume}. It is {'On' if tv2.is_on else 'Off'}.")

    # Case 2
    # Testing operations with TV1   
    print(f"\n{bold_start}Case 2:{bold_end} Testing operations with TV1")
    tv1.show()
    tv1.channel_up()
    tv1.channel_down()
    tv1.volume_up()
    tv1.volume_down()
    tv1.set_channel(70)
    tv1.set_volume(3)
    print(tv1.get_channel())
    print(tv1.get_volume())

    # Case 3
    # Testing the methods when TV1 is off.
    print(f"\n{bold_start}Case 3:{bold_end} Testing the methods when TV1 is off.")
    tv1.turn_off()
    tv1.channel_up()
    tv1.channel_down()
    tv1.volume_up()
    tv1.volume_down()
    tv1.set_channel(8)
    tv1.set_volume(3)
    print(tv1.get_channel())
    print(tv1.get_volume())
    
    # Case 4
    # Testing TV1 after turning it on.
    print(f"\n{bold_start}Case 4:{bold_end} Testing TV1 after turning it on again")
    tv1.turn_on()
    tv1.show()
    tv1.channel_up()
    tv1.channel_down()
    tv1.volume_up()
    tv1.volume_down()
    tv1.set_channel(30)
    tv1.set_volume(3)
    print(tv1.get_channel())
    print(tv1.get_volume())
    
    # Case 5
    # Testing instance method of TV2
    print(f"\n{bold_start}Case 5:{bold_end} Testing instance method of TV2")
    tv2.show()
    tv2.channel_up()
    tv2.channel_down()
    tv2.volume_up()
    tv2.volume_down()
    tv2.set_channel(120)
    tv2.set_volume(2)
    print(tv2.get_channel())
    print(tv2.get_volume())

    # Case 6
    # Testing the methods when TV2 is off.
    print(f"\n{bold_start}Case 6:{bold_end} Testing instance method of TV2 when it is off")
    tv2.turn_off()
    tv2.channel_up()
    tv2.channel_down()
    tv2.volume_up()
    tv2.volume_down()
    tv2.set_channel(12)
    tv2.set_volume(5)
    print(tv2.get_channel())
    print(tv2.get_volume())
    
    # Case 7
    # Testing TV2 after turning it on.
    print(f"\n{bold_start}Case 7:{bold_end} Testing TV2 after turning it on again")
    tv2.turn_on()
    tv2.show()
    tv2.channel_up()
    tv2.channel_down()
    tv2.volume_up()
    tv2.volume_down()
    tv2.set_channel(3)
    tv2.set_volume(2)
    print(tv2.get_channel())
    print(tv2.get_volume())
    
    # Case 8
    # Testing the set methods with invalid values
    print(f"\n{bold_start}Case 8:{bold_end} Testing the set methods with invalid values")
    tv1.show()
    tv1.set_channel(130)
    tv1.set_channel(0)
    tv1.set_volume(8)
    tv1.set_volume(0)
    tv2.show()
    tv2.set_channel(130)
    tv2.set_channel(0)
    tv2.set_volume(8)
    tv2.set_volume(0)
    
    # Case 9
    # Testing the channel_up and channel_down methods when it reaches the maximum and minimum values.
    print(f"\n{bold_start}Case 9:{bold_end} Testing the channel_up and channel_down methods when it reaches the maximum and minimum values.")
    print("TV1"), tv1.show()
    tv1.set_channel(120)
    tv1.channel_up()
    print(tv1.get_channel())
    tv1.set_channel(1)
    tv1.channel_down()
    print(tv1.get_channel())
    print("TV2"), tv2.show()
    tv2.set_channel(120)
    tv2.channel_up()
    print(tv2.get_channel())
    tv2.set_channel(1)
    tv2.channel_down()
    print(tv2.get_channel())
    
    # Case 10
    # Final Test
    print(f"\n{bold_start}Case 10:{bold_end} Final Test to print the instance variables of the object same as the expected output in the ppt.")
    print(f"Tv1's channel is {tv1.channel} and volume level is {tv1.volume}. It is {'On' if tv1.is_on else 'Off'}.")
    print(f"Tv2's channel is {tv2.channel} and volume level is {tv2.volume}. It is {'On' if tv2.is_on else 'Off'}.")

if __name__ == "__main__":
    test_tv()
    print("\nTesting is done.")