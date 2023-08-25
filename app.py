import music21 as m
from typing import List,Set

note_dict={
    "e":["F4","F4#","G4","G4#","A4","A4#","B4","C5","C5#","D5","D5#","E5","F5","F5#","G5","G5#","A5","A5#","B5","C6"],
    "B":["C4","C4#","D4","D4#","E4","F4","F4#","G4","G4#","A4","A4#","B4","C5","C5#","D5","D5#","E5","F5","F5#","G5"],
    "G":["G3#","A3","A3#","B3","C4","C4#","D4","D4#","E4","F4","F4#","G4","G4#","A4","A4#","B4","C5","C5#","D5","D5#"],
    "D":["D3#","E3","F3","F3#","G3","G3#","A3","A3#","B3","C4","C4#","D4","D4#","E4","F4","F4#","G4","G4#","A4","A4#"],
    "A":["A2#","B2","C3","C3#","D3","D3#","E3","F3","F3#","G3","G3#","A3","A3#","B3","C4","C4#","D4","D4#","E4","F4"],
    "E":["F2","F2#","G2","G2#","A2","A2#","B2","C3","C3#","D3","D3#","E3","F3","F3#","G3","G3#","A3","A3#","B3","C4"],
}

def _get_note(n):
    string,fret=n.split(".")
    string=list(note_dict.keys())[int(string)-1]
    if int(fret) > 0:
        return note_dict[string][int(fret)-1]
    else:
        return string

def compose_score(notes:List[Set]) -> m.stream.base.Stream:
    """
    1. Get notes
    2. Add notes and duration to score
    
    Expected format: notes = List[Set("string.fret",duration)]
    Eg. notes_for_C=[("5.3",0.5),("5.5",0.5),("4.2",0.5),("4.5",0.5),("3.2",0.5),("3.5",0.5),("2.3",0.5),("2.5",0.5),("1.3",0.5),("1.5",0.5),("1.8",2)]

    """
    i=m.instrument.Guitar()
    streamx = m.stream.Stream(instrument=i)

    for note_and_duration in notes:
        notex,durationx=note_and_duration
        notex_=_get_note(notex)
        notex=m.note.Note(notex_)
        notex.duration=m.duration.Duration(durationx)
        streamx.append(notex)
    return streamx