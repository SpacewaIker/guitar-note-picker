from random import randint

NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
STRINGS = ['E', 'A', 'D', 'G', 'B', 'e']


def pick_note(raw=False, strings=STRINGS,
              notes=NOTES):
    '''Picks a note on a certain string of a guitar.
        A&P:
            raw:
                bool, if the note and string must be returned in raw or not
            notes:
                list of str, list of notes to choose from
            strings:
                list of str, list of strings to choose form'''

    note = notes[randint(0, 11)]
    string = strings[randint(0, 5)]

    if raw:
        return (note, string)
    else:
        return '{0} on the {1} string'.format(note, string)


def pick_note_answer(note_string, raw=False):
    '''Returns the fret(s) on which the note is.
        A&P:
            note_string:
                tuple of 2 str, note and string on which to find the note
            raw:
                bool, if the function should return the raw value or not'''

    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    index = notes.index(note_string[1].upper())
    fret = 0

    while notes[index] != note_string[0]:
        fret += 1
        if index == 11:
            index = 0
        else:
            index += 1

    fret = [fret, fret + 12]

    if raw:
        return fret
    else:
        for i in [0, 1]:
            if fret[i] == 0:
                fret[i] = 'open string'
            elif fret[i] == 1:
                fret[i] = '1st fret'
            elif fret[i] == 2:
                fret[i] = '2nd fret'
            elif fret[i] == 3:
                fret[i] = '3rd fret'
            else:
                fret[i] = '{}th fret'.format(fret[i])

        return '{0} is on the {1} and on the {2} of the {3} string'.format(
            note_string[0], fret[0], fret[1], note_string[1]
        )


if __name__ == "__main__":
    from time import sleep
    var = pick_note(raw=True)
    print('{0} on the {1} string'.format(var[0], var[1]))
    sleep(15)
    print(pick_note_answer(var))

hey = 'hello'
