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

def start_practice_mode(midi_file_path, use_right_hand, use_left_hand, use_dynamics):
    if not use_right_hand and not use_left_hand:
        print("Both hands cannot be disabled. Exiting...")
        return

    noteSequence = midi_to_note_sequence(midi_file_path, use_right_hand, use_left_hand)
    currentBeat = 0

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
                if not use_dynamics:
                    current_notes.append(note)
                elif noteSequence[currentBeat][1] - 20 <= velocity <= noteSequence[currentBeat][1] + 20:
                    current_notes.append(note)
            else:
                try:
                    current_notes.remove(note)
                except ValueError:
                    pass

            if current_notes == noteSequence[currentBeat][0]:
                currentBeat += 1

if __name__ == "__main__":
    start_practice_mode("../Interstellar Main Theme.mid", use_right_hand=True, use_left_hand=True, use_dynamics=True)