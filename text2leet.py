#!/usr/bin/python
# -*- coding: UTF-8 -*-

# text2leet.py

# import required modules
import sys, os, argparse, itertools

# tool description
desc = """This tool rapidly converts a single string or file containing strings
into leetspeak (1337spe@k), a dialect common in gaming, chat rooms, and user
passwords. Strings input into text2leet will have their characters replaced
with all common leetspeak characters. The output word list will contain all
possible combinations (Cartesian product) of replaced characters. The character 
substitutions were generally based on https://simple.wikipedia.org/wiki/Leet.
------------------------------------------------------------------------------
CAUTION: this tool can quickly generate large output files! Lengthy input
strings or word lists canquickly result in a large number of output permutations.
An input string of 'hello' with default options yields an output file with
12,852 possible permutations, taking up 126 KB of disk space. An input
string of 'hellohello' yields an output file with 165,173,904 permutations
taking up 2.76 GB of disk space. So use carefully! Consider using the -sl or
--short-list option to reduce the size of the output.
------------------------------------------------------------------------------
CLI EXAMPLES:
> python text2leet.py inputstring output_file.txt -sc st
> python text2leet.py fluffy pet_name_word_list.txt -sl"""

# parse arguments
parser = argparse.ArgumentParser(description=desc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("input", help="Input word or word list", type=str)
parser.add_argument("output", help="Output file containing leetspeak permutations")
parser.add_argument("-sc", "--skip-characters", help="Input characters to skip (these will not be converted)")
parser.add_argument("-sl", "--short-list", help="Uses a reduced list of substitutions to improve performance", action="store_true")
args = parser.parse_args()

# create the dictionary of substitutions (source: https://simple.wikipedia.org/wiki/Leet)
allSubs = {"a": ["A", "a", "4", "/-\\", "/_\\", "@", "/\\"],
           "b": ["B", "b", "8", "|3", "13", "|}", "|:", "|8", "18", "6", "|B", "|8", "lo", "|o", "j3"],
           "c": ["C", "c" "<", "{", "[", "("],
           "d": ["D", "d", "|)", "|}", "|]", "|>"],
           "e": ["E", "e", "3"],
           "f": ["F", "f", "|=", "ph", "|#"],
           "g": ["G", "g", "[,", "-,", "[+", "6", "C-"],
           "h": ["H", "h", "#", "4", "|-|", "[-]", "{-}", "}-{", "}{", "|=|", "[=]", "{=}", "/-/", "(-)", ")-(", ":-:", "I+I"],
           "i": ["I", "i", "1", "|", "!", "9"],
           "j": ["J", "j", "_|", "_/", "_7", "_)", "_]", "_}"],
           "k": ["K", "k", "|<", "1<", "l<", "|{", "l{"],
           "l": ["L", "l", "|_", "|", "1", "]["],
           "m": ["M", "m", "44", "|\/|", "^^", "/\/\\", "/X\\", "[]\/][", "[]V[]", "][\\//][", "(V)", "//.", ".\\\\", "N\\\\"],
           "n": ["N", "n", "|\|", "/\/", "/V", "][\\]["],
           "o": ["O", "o" "0", "()", "[]", "{}", "<>", "oh"],
           "p": ["P", "p", "|o", "|O", "|>", "|*", "|D", "/o", "[]D", "|7"],
           "q": ["Q", "q" "O_", "9", "(,)", "0,", "kw"],
           "r": ["R", "r", "|2", "12", ".-", "|^", "l2"],
           "s": ["S", "s", "5", "$", "z", "Z"],
           "t": ["T", "t", "7", "+", "'|'", "`|`"],
           "u": ["U", "u", "|_|", "\_\\", "/_/", "\_/", "(_)", "[_]", "{_}"],
           "v": ["V", "v", "\/"],
           "w": ["W", "w", "\/\/", "(/\)", "\^/", "|/\|", "\X/", "\\'", "'//", "VV", "vv", "\_|_/", "\\//\\//", "\V/"],
           "x": ["X", "x", "%", "*", "><", "}{", ")("],
           "y": ["Y", "y", "`/"],
           "z": ["Z", "z", "2", "5", "7_", ">_", "(/)"],
           " ": [" ", "_", "-", "."]}

smallSubs = {"a": ["A", "a", "4", "@"],
           "b": ["B", "b", "8", "13"],
           "c": ["C", "c" "<"],
           "d": ["D", "d"],
           "e": ["E", "e", "3"],
           "f": ["F", "f", "ph"],
           "g": ["G", "g", "6"],
           "h": ["H", "h", "#"],
           "i": ["I", "i", "1", "!"],
           "j": ["J", "j"],
           "k": ["K", "k", "|<"],
           "l": ["L", "l", "1"],
           "m": ["M", "m", "44"],
           "n": ["N", "n", "|\|"],
           "o": ["O", "o" "0", "()", "oh"],
           "p": ["P", "p", "|o", "|O"],
           "q": ["Q", "q" "O_"],
           "r": ["R", "r", "|2", "12"],
           "s": ["S", "s", "5", "$", "z", "Z"],
           "t": ["T", "t", "7", "+"],
           "u": ["U", "u", "|_|"],
           "v": ["V", "v", "\/"],
           "w": ["W", "w", "\/\/", "VV", "vv"],
           "x": ["X", "x", "><"],
           "y": ["Y", "y", "`/"],
           "z": ["Z", "z", "2", "5"],
           " ": [" ", "_", "-", "."]}

# create raw variables for the arguments
inputVal = args.input
outputVal = args.output
if args.skip_characters:
    skipChars = args.skip_characters
else:
    skipChars = ""
if args.short_list:
    subDict = smallSubs
else:
    subDict = allSubs

# validate input
if os.path.exists(inputVal):
    # come back later and add support for file input
    pass
else:
    pass

# create the lists of characters to create permutations
chars = (subDict[char.lower()] if (char in subDict.keys() and char not in skipChars) else char for char in inputVal)
results = ("".join(element) for element in itertools.product(*chars))

# write results to output file
with open(outputVal, "w") as output_file:
    for item in results:
        output_file.write(item + "\n")
    output_file.close()
