"""
Converts a MIDI file to a note sequence list
"""

import mido

def process_track(track):
    events = []
    absolute_time = 0
    for msg in track:
        absolute_time += msg.time # Accumulate delta time to get absolute time
        if msg.type in ["note_on"] and msg.velocity > 0:
            event = {
                "time": absolute_time,
                "note": msg.note,
                "velocity": msg.velocity if msg.type == "note_on" else 0,
            }

            events.append(event)

    return events

def midi_to_note_sequence(midi_file_path):
    midi_file = mido.MidiFile("../Interstellar Main Theme.mid")

    right_hand_events = []
    left_hand_events = []
    
    # Process each track in the MIDI file
    right_hand_events = process_track(midi_file.tracks[0])
    left_hand_events = process_track(midi_file.tracks[1])

    # Merge and align events by time
    all_events = sorted(right_hand_events + left_hand_events, key=lambda x: x["time"])

    # Create note sequence list
    noteSequenceDict = {}
    for event in all_events:
        if event['time'] not in noteSequenceDict:
            noteSequenceDict[event['time']] = []
        noteSequenceDict[event['time']].append(event['note'])
    noteSequence = [noteSequenceDict[time] for time in sorted(noteSequenceDict.keys())]
    return noteSequence