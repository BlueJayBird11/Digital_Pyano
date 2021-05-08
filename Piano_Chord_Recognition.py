def bigFunk(a, b, c):
    def chordReader(x, y, z, final_list):
        # value is the sum of x, y and z's indices
        value = final_list.index(x) + final_list.index(y) + final_list.index(z)

        # This calculates the lowest note being played 'A' being the local minimum and 'G#' being the local maximum
        if organizer.index(x) < organizer.index(y) and organizer.index(x) < organizer.index(z):
            leadingNoteLow = x
        if organizer.index(y) < organizer.index(x) and organizer.index(y) < organizer.index(z):
            leadingNoteLow = y
        if organizer.index(z) < organizer.index(x) and organizer.index(z) < organizer.index(y):
            leadingNoteLow = z

        # This calculates the highest note being played 'A' being the local minimum and 'G#' being the local maximum
        if organizer.index(x) > organizer.index(y) and organizer.index(x) > organizer.index(z):
            leadingNoteHigh = x
        if organizer.index(y) > organizer.index(x) and organizer.index(y) > organizer.index(z):
            leadingNoteHigh = y
        if organizer.index(z) > organizer.index(x) and organizer.index(z) > organizer.index(y):
            leadingNoteHigh = z

        # This calculates the middle note out of the three being played
        if (organizer.index(x) < organizer.index(y) and organizer.index(x) > organizer.index(z))\
           or organizer.index(x) > organizer.index(y) and organizer.index(x) < organizer.index(z):
            leadingNoteMid = x
        if (organizer.index(y) < organizer.index(x) and organizer.index(y) > organizer.index(z))\
           or organizer.index(y) > organizer.index(x) and organizer.index(y) < organizer.index(z):
            leadingNoteMid = y
        if (organizer.index(z) < organizer.index(x) and organizer.index(z) > organizer.index(y))\
            or organizer.index(z) > organizer.index(x) and organizer.index(z) < organizer.index(y):
            leadingNoteMid = z
        k = organizer.index(leadingNoteHigh) - organizer.index(leadingNoteLow)
    ##    return(value)
    ##    return(k)
    ##    return(organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid))
        
        if (value == 11 or value == 14):
            if ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 4):
                return("{} Major Chord".format(leadingNoteMid))
            elif ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 3):
                return("{} Major Chord".format(leadingNoteLow))
            elif ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 5):
                return("{} Major Chord".format(leadingNoteHigh))
                
        elif value == 10 or value == 13:
            if ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 4):
                return("{} minor chord".format(leadingNoteLow))
            elif ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 3):
                return("{} Minor Chord".format(leadingNoteMid))
            elif ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 5):
                return("{} Minor Chord".format(leadingNoteHigh))
                
        elif value == 12:
            if final_list.index(y) == 4:
                return("{} Augmented Chord".format(leadingNoteLow))
            elif final_list.index(y) == 3:
                return("{} Diminished Chord".format(leadingNoteLow))
                
        elif value == 9 or value == 15:
            if ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 3) and\
               ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteLow)) == 6):
                return ("{} Diminished Chord".format(leadingNoteLow))
            elif ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteMid)) == 3) and\
                 ((organizer.index(leadingNoteHigh) - organizer.index(leadingNoteLow)) == 9):
                return("{} Diminished Chord".format(leadingNoteMid))
        else:
            return("not recognized")
    ##        else:
    ##            return("{} Diminished Chord".format(leadingNoteHigh))


    # creates an empy list whGich will have the x, y, and z values added to them 
    my_list = []

    # Asks for user input for which key they would like to play and sets them equal to a respective variable
    # Example (x = F), (y = G), (z = D)
##    x = input("pick a Key ").upper()
##
##    y = input("pick a Key ").upper()
##
##    z = input("pick a Key ").upper()
    x = a
    y = b
    z = c


    # appends values associated with x, y, and z to the list declared at the beginning
    my_list.append(x)
    my_list.append(y)
    my_list.append(z)

    # Example of what 'my_list' should look like at this point "['F', 'G', 'D']"
    # return(my_list)

    # This appends every key that is in an octive
    my_list = ['F', 'G', 'D', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    ##my_list.append("C")
    ##my_list.append("C#")
    ##my_list.append("D")
    ##my_list.append("D#")
    ##my_list.append("E")
    ##my_list.append("F")
    ##my_list.append("F#")
    ##my_list.append("G")
    ##my_list.append("G#")
    ##my_list.append("A")
    ##my_list.append("A#")
    ##my_list.append("B")

    # Example of what 'my_list' should look like at this point is listed in the line below
    # '['F', 'G', 'D', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']'
    # return(my_list)

    # At this point we take a set of 'my list', this insures that the variables (x, y, z) will still
    # be present in the set, the excess values will be thrown out as a set can only contain unique values
    conversion = set(my_list)

    # Example of what 'conversion' should look like at this point is listed in the line below
    # '{'B', 'A', 'D#', 'G', 'A#', 'E', 'C#', 'F#', 'D', 'F', 'C', 'G#'}'
    # return(conversion)

    # this simply organizes 'coversion' in alphabetical order, it also simultaneously converts the set back into a list
    organizer = sorted(conversion)

    # Example of what 'organizer' should look like at this point is listed in the line below
    # '['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']'
    # return(organizer)

    # These two lists are simply place holder lists which will be used to organize the list in a manner according to the first input
    final_list = []
    list2 = []

    # This will break the current filled list 'organizer' in to two seperate lists. One list will befilled with the str values which indeces is equal to or greater than
    # the initial x variables index within the list. The other list will be made up of those points which did not meet the given criteria.
    for i in range(len(organizer)):
        if i >= organizer.index(x):
            final_list.append(organizer[i])
        else:
            list2.append(organizer[i])

    # Example of what 'final_list' should look like at this point is listed in the line below
    # '['F', 'F#', 'G', 'G#']'
    # return(final_list)

    # Example of what 'list2' should look like at this point is listed in the line below
    # '['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']'
    # return(list2)

    # This algorithm will simply append each value in 'list2' the end of 'final_list'
    for i in range(len(list2)):
        final_list.append(list2[i])

    # Example of what 'final_list' should look like at this point is listed in the line below
    # ['F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E']
    # return("Final list {}".format(final_list))
    return chordReader(x, y, z, final_list)
