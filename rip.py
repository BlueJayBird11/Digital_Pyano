from pydub import AudioSegment

# get the main wave file to rip the notes from
rip = AudioSegment.from_wav("Notes/Piano/pianoRip.wav")

## Gets 12 different wav files based on the given octave
#   A new note is played every 4 seconds, starting at A
#   so using AudioSegment from pydub, you can get all 12
#   notes as wave of an octave from the equation used.
def getNotes(octive = 2):
    num = 0
    for i in range(0, 12*1*4000, 4000):
        # the equation used, trust me, there was much thought
        # as well as trial and error
        newAudio = rip[((octive*12*4000)+i):((octive*12*4000)+(i)+500)]

        # exports every new wave file over the old ones
        newAudio.export('Notes/Piano/{}.wav'.format(num), format="wav")
        num+=1
