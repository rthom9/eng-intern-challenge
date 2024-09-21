import sys

braille_to_eng = {
    "O.....": "a", "O.O...": "b", "OO....": "c", "OO.O..": "d", "O..O..": "e", "OOO...": "f",
    "OOOO..": "g", "O.OO..": "h", ".OO...": "i", ".OOO..": "j", "O...O.": "k", "O.O.O.": "l",
    "OO..O.": "m", "OO.OO.": "n", "O..OO.": "o", "OOO.O.": "p", "OOOOO.": "q", "O.OOO.": "r",
    ".OO.O.": "s", ".OOOO.": "t", "O...OO": "u", "O.O.OO": "v", ".OOO.O": "w", "OO..OO": "x",
    "OO.OOO": "y", "O..OOO": "z", "..OO.O": ".", "..O...": ",", "..O.OO": "?", "..OOO.": "!",
    "..OO..": ":", "..O.O.": ";", "....OO": "-", ".O..O.": "/", ".OO..O": "<", "O.O..O": "(",
    ".O.OO.": ")", "......": " "
}

braille_to_eng_num = {
    "O.....": "1", "O.O...": "2", "OO....": "3", "OO.O..": "4", "O..O..": "5", "OOO...": "6",
    "OOOO..": "7", "O.OO..": "8", ".OO...": "9", ".OOO..": "0"}

braille_to_eng_inst = {
    ".....O": "cap",
    ".O...O": "dec",
    ".O.OOO": "num"
}

eng_to_braille = {value: key for key, value in braille_to_eng.items()}
eng_to_braille_num = {value: key for key, value in braille_to_eng_num.items()}
eng_to_braille_inst = {value: key for key, value in braille_to_eng_inst.items()}

input_text_arr = sys.argv[1:]
print(input_text_arr)

# Determine if input_text is english or braille
lang = "braille"

if len(input_text_arr) > 1:
    lang = "eng"

for char in input_text_arr[0]:
    if char != "." and char != "O":
        lang = "eng"
        break

def trans_braille_to_eng(braille_str):
    braille_unit_arr = [braille_str[i:i+6] for i in range(0, len(braille_str), 6)]
    capitalize = "OFF"
    number = "OFF"
    decimal = "OFF"
    eng_string = ""
    print(braille_unit_arr)

    for braille_unit in braille_unit_arr:
        # If braille_unit is an instruction:
        if braille_unit in braille_to_eng_inst:
            if braille_to_eng_inst[braille_unit] == "cap":
                capitalize = "ON"
            elif braille_to_eng_inst[braille_unit] == "dec":
                decimal = "ON"
            elif braille_to_eng_inst[barille_unit] == "num":
                number = "ON"


        # if capital_follows, next 6 chars are a capital letter


    # if number follows, assume all following are numbers until next space


trans_braille_to_eng(input_text_arr[0])

