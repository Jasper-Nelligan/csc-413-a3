"""
Starts practice mode and communicates with the Arduino to light up the LEDs
"""

import mido
from midi_to_note_sequence import midi_to_note_sequence

def start_practice_mode(midi_file_path, use_right_hand, use_left_hand):
    if not use_right_hand and not use_left_hand:
        print("Both hands cannot be disabled. Exiting...")
        return

    noteSequence = midi_to_note_sequence(midi_file_path, use_right_hand, use_left_hand)
    currentBeat = 0
    print(noteSequence)

    # Connect to the keyboard
    keyboard_port = -1

    try:
        keyboard_port = mido.get_input_names()[0]
    except IndexError:
        print("No MIDI keyboard found. Exiting...")
        exit()

    with mido.open_input(keyboard_port) as inport:
        print("Listening for MIDI messages...")
        current_notes = []

        for message in inport:
            note, velocity = -1, -1
            try:
                _, _, note, velocity, _ = str(message).split()
            except ValueError:
                # Ignore messages that are not note_on
                continue

            note = int(note.split("=")[1])
            velocity = int(velocity.split("=")[1])

            if velocity > 0:
                current_notes.append(note)
            else:
                current_notes.remove(note)

            if current_notes == noteSequence[currentBeat]:
                currentBeat += 1

if __name__ == "__main__":
    start_practice_mode("../Interstellar Main Theme.mid", use_right_hand=False, use_left_hand=True)