import mido

# List all available MIDI devices
print("Available MIDI Input Ports:")
print(mido.get_input_names())

# Connect to the keyboard (replace with your keyboard's port name)
keyboard_port = mido.get_input_names()[0]  # Assuming the first one is the DGX-230
with mido.open_input(keyboard_port) as inport:
    print("Listening for MIDI messages...")
    for message in inport:
        print(message)  # Prints MIDI messages sent from the keyboard
