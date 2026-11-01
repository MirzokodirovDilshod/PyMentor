# PyMentor
# Create an algorthm that finds anagramm
def anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())
    pass
# anagram is a thinga word, phrase, or name formed by rearranging the letters of another\
# E.g:
# "evil" = "vile"
# "a gentleman" = "elegant man"
# "silent" = "listen"
# and so on.
# In this code we sort the given inputs whether it's text or number or anything else
# SO this code can find if there difference or not.
