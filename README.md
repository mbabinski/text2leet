This tool rapidly converts a single string or file containing strings into leetspeak (1337spe@k), a dialect common in gaming, chat rooms, and user passwords. Strings input into text2leet will have their characters replaced with all common leetspeak characters. The output word list will contain all possible combinations (Cartesian product) of replaced characters. The character substitutions were generally based on https://simple.wikipedia.org/wiki/Leet.

CAUTION: this tool can quickly generate large output files! Lengthy input strings or word lists canquickly result in a large number of output permutations. An input string of 'hello' with default options yields an output file with 12,852 possible permutations, taking up 126 KB of disk space. An input string of 'hellohello' yields an output file with 165,173,904 permutations taking up 2.76 GB of disk space. So use carefully! Consider using the -sl or --short-list option to reduce the size of the output.

CLI EXAMPLES:
> python text2leet.py inputstring output_file.txt -sc st
> python text2leet.py fluffy pet_name_word_list.txt -sl
