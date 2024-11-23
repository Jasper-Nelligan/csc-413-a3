import aubio
import numpy as np

# Path to your PCM WAV file
audio_file = "output.wav"

# Set consistent buffer size and hop size
BUFFER_SIZE = 512  # Must match the hop size used in pitch detection
HOP_SIZE = BUFFER_SIZE

# Initialize aubio source (audio file reader)
samplerate = 0  # Use 0 to auto-detect samplerate
audio_source = aubio.source(audio_file, samplerate, BUFFER_SIZE)
samplerate = audio_source.samplerate

# Initialize pitch detection with matching hop size
pitch_detector = aubio.pitch("default", BUFFER_SIZE, HOP_SIZE, samplerate)
pitch_detector.set_unit("Hz")
pitch_detector.set_silence(-40)  # Ignore silence below -40 dB

print(f"Processing audio file: {audio_file}")

while True:
    samples, read = audio_source()  # Read a buffer of audio samples
    if len(samples) < BUFFER_SIZE:  # Handle the end of the file
        break
    
    pitch = pitch_detector(samples)[0]  # Detect pitch for the buffer
    
    if pitch > 0:  # If a pitch is detected
        # Convert frequency to MIDI note
        midi_note = 69 + 12 * np.log2(pitch / 440.0)
        piano_note = round(midi_note)  # Round to the nearest MIDI note
        print(f"Pitch: {pitch:.2f} Hz, Note: {piano_note}")

