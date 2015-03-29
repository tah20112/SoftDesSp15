"""
Convert input file to Pig Latin
and print the result.

Usage:

python latin.py [filename]

Prints out the text in Pig Latin
"""


def process_text(filename):
    """Print out given file in Pig Latin"""

    fp = open(filename)
    for line in fp:
        for word in line.split():
            # Process into Pig Latin
            #print word
            pass

    fp.close()
    print "I just processed", filename


if __name__ == "__main__":

    print "I've been called from the command line"
    import sys
    filename = sys.argv[1]
    process_text(filename)