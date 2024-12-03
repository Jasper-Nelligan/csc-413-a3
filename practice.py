"""
Starts practice mode and communicates with the Arduino to light up the LEDs

Arguments:
    midi_file_path: The path to the MIDI file to practice
    use_right_hand: Whether to use the right hand
    use_left_hand: Whether to use the left hand
    use_dynamics: Whether to use dynamics
"""

import mido
from midi_to_note_sequence import midi_to_note_sequence
import serial
import time

def start_practice_mode(midi_file_path, use_right_hand, use_left_hand, use_dynamics):
    print("Booting up serial connections, please wait...")
    serial_right_hand = serial.Serial('COM4', 9600)
    serial_left_hand = serial.Serial('COM5', 9600)
    time.sleep(2)

    if not use_right_hand and not use_left_hand:
        print("Both hands cannot be disabled. Exiting...")
        return

    note_sequence = midi_to_note_sequence(midi_file_path, use_right_hand, use_left_hand)
    current_beat = 0

    # Connect to the keyboard
    keyboard_port = -1

    try:
        keyboard_port = mido.get_input_names()[0]
    except IndexError:
        print("No MIDI keyboard found. Exiting...")
        exit()
    

    if use_right_hand:
        serial_right_hand.write("p".encode())
        time.sleep(2)
        serial_right_hand.write("b".encode())
        time.sleep(2)

    if use_left_hand:
        serial_left_hand.write("p".encode())
        time.sleep(2)
        serial_left_hand.write("b".encode())
        time.sleep(2)

    with mido.open_input(keyboard_port) as inport:
        print("Listening for MIDI messages...")
        current_notes = []

        for message in inport:
            if current_beat >= len(note_sequence):
                break

            played_note, velocity = -1, -1
            try:
                _, _, played_note, velocity, _ = str(message).split()
            except ValueError:
                # Ignore messages that are not note_on
                continue

            played_note = int(played_note.split("=")[1])
            velocity = int(velocity.split("=")[1])
            
            if velocity > 0:
                if not use_dynamics:
                    current_notes.append(played_note)
                elif note_sequence[current_beat][1] - 20 <= velocity <= note_sequence[current_beat][1] + 20:
                    current_notes.append(played_note)
            else:
                try:
                    current_notes.remove(played_note)
                except ValueError:
                    pass

            if set(current_notes) == set(note_sequence[current_beat][0]):
                current_beat += 1
                current_notes = []
                # todo conditional send
                if use_right_hand:
                    serial_right_hand.write("b".encode())
                if use_left_hand:
                    serial_left_hand.write("b".encode())

        serial_right_hand.close()
        serial_left_hand.close()