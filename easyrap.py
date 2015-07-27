#! /usr/bin/env python

from textstat.textstat import textstat
import re

raw_input("Please copy the lyrics to the two text files song1 and song 2. \nWhen complete hit enter to analyze.")
print ""

try:
    f = open('song1.txt')
    f_read = str(f.read())
    cleaned = re.sub("[\(\[].*?[\)\]]", "", f_read)
    if textstat.dale_chall_readability_score(cleaned) < 5:
        print "Song #1 | Dale Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | " + "Easily understood by 4th-grade students or lower."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned) < 6:
        print "Song #1 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | # of Difficult Words: " + str(textstat.difficult_words(cleaned))
        print "Song #1 | " + "Easily understood by 5th-grade and 6th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned) < 7:
        print "Song #1 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | # of Difficult Words: " + str(textstat.difficult_words(cleaned))
        print "Song #1 | " + "Easily understood by 7th-grade and 8th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned) < 8:
        print "Song #1 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | # of Difficult Words: " + str(textstat.difficult_words(cleaned))
        print "Song #1 | " + "Easily understood by 9th-grade and 10th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned) < 9:
        print "Song #1 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | # of Difficult Words: " + str(textstat.difficult_words(cleaned))
        print "Song #1 | " + "Easily understood by 11th-grade and 12th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned) < 10:
        print "Song #1 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | # of Difficult Words: " + str(textstat.difficult_words(cleaned))
        print "Song #1 | " + "Easily understood by college students."
        f.close()
    else:
        print "Song #1 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned))
        print "Song #1 | # of Difficult Words: " + str(textstat.difficult_words(cleaned))
        print "Song #1 | " + "Easily understood by college graduates."
        f.close()
    print "---------------------------------"

    f2 = open('song2.txt')
    f2_read = str(f2.read())
    cleaned2 = re.sub("[\(\[].*?[\)\]]", "", f2_read)

    if textstat.dale_chall_readability_score(cleaned2) < 5:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by 4th-grade students or lower."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned2) < 6:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by 5th-grade and 6th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned2) < 7:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by 7th-grade and 8th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned2) < 8:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by 9th-grade and 10th-grade students."
        f.close()
    elif textstat.dale_chall_readability_score(cleaned2) < 9:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by 11th-grade and 12th-grade students."

        f.close()
    elif textstat.dale_chall_readability_score(cleaned2) < 10:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by college students."
        f.close()
    else:
        print "Song #2 | Dale-Chall Score: " + str(textstat.dale_chall_readability_score(cleaned2))
        print "Song #2 | # of Difficult Words: " + str(textstat.difficult_words(cleaned2))
        print "Song #2 | " + "Easily understood by college graduates."
        f.close()
    print ""
    print "Keep in mind when using rap lyrics, many rappers use slang which can skew the results, especially the number of diffcult words."

except:
    print "Failed to open and read song1.txt and song2.txt. Did you paste your songs in there?"
    print "Are you high?"

