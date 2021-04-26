from pydub import AudioSegment

rip = AudioSegment.from_wav("Notes/Piano/pianoRip.wav")
def getNotes(octive = 0):
    num = 0
    for i in range(0, 12*1*4000, 4000):
        #newAudio = rip[((octive*12*4000)+i):((octive*12*4000)+(i)+4000)]
        newAudio = rip[((octive*12*4000)+i):((octive*12*4000)+(i)+10)]

        newAudio.export('Notes/Piano/{}.wav'.format(num), format="wav")
        num+=1