#Import dependency to read a .mid file. RECOMMENDED - mido documentation
import mido

#Enter path of file 
path_name_of_mid_file = "/Users/adityatatwawadi/Desktop/Projects/Python/JohnLocke2021/FurElise.mid"

#Compute stuff
class ComputeParsons:

    def __init__(self):
        pass

    def midi_to_parsons(midifile, limit=13, offset=0):   

        """
        Takes a midi file path, outputs a string
        """

        #Info to be added to empty variable string parsons
        global parsons
        count = 0
        parsons = ""

        #Reads midifile - a mid file is a series of 8-bit bytes
        for message in mido.MidiFile(midifile):

            if "note_on" in str(message) and offset == 0:

                if parsons == "":
                    # initialise list
                    prev = message.note
                    parsons += "*"

                #comparison to determine u d or r (As per Parson's Code)
                elif message.note > prev:
                    parsons += "u"
                    prev = message.note
                elif message.note < prev:
                    parsons += "d"
                    prev = message.note
                elif message.note == prev:
                    parsons += "r"
                    prev = message.note

                #increment count
                count += 1
                if count >= limit:
                    break

            elif "note_on" in str(message):
                offset -= 1

        return(f"The Parson's code for the file you have inputted with the path {path_name_of_mid_file} is {parsons}")

    def contour(code):

        """
        Creates a contor image using the Parson's code
        Output: UI display
        """
        
        #Not needed - only for individual file testing
        if code[0] != "*":
            raise ValueError("Parsons Code must start with '*'")

        #Initialize an empty dictionary
        contour_dict = {}
        pitch = 0
        index = 0

        max_pitch = 0
        min_pitch = 0

        contour_dict[(pitch, index)] = "*"

        for character in code:
            if character == "r":
                index += 1
                contour_dict[(pitch, index)] = "-"

                index += 1
                contour_dict[(pitch, index)] = "*"
            elif character == "u":
                index += 1
                pitch -= 1
                contour_dict[(pitch, index)] = "/"

                index += 1
                pitch -= 1
                contour_dict[(pitch, index)] = "*"

                if pitch < max_pitch:
                    max_pitch = pitch
            elif character == "d":
                index += 1
                pitch += 1
                contour_dict[(pitch, index)] = "\\"

                index += 1
                pitch += 1
                contour_dict[(pitch, index)] = "*"

                if pitch > min_pitch:
                    min_pitch = pitch

        for pitch in range(max_pitch, min_pitch+1):
            line = [" " for _ in range(index + 1)]
            for pos in range(index + 1):
                if (pitch, pos) in contour_dict:
                    line[pos] = contour_dict[(pitch, pos)]


            print("".join(line))

    def save_parsons():

        """
        Saves Parson's code to a txt file so webscrape.py can access it
        """

        #Writes code to a txt file
        with open("parson.txt", 'w') as f:
            f.write(parsons)

print(ComputeParsons.midi_to_parsons(path_name_of_mid_file))
ComputeParsons.contour(parsons)
ComputeParsons.save_parsons()