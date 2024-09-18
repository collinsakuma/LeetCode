from collections import Counter

class Solution:
    def minimumTeachings(self, n, languages, friendships):
        # set of languages
        languages = [set(l) for l in languages]

        dont_speak = set() # set of languages that each person donest speak

        # loop through friendship pairs
        for u, v in friendships:
            # -1 to set the index of each person
            u = u - 1
            v = v - 1
            # if person speaks the other language continue
            if languages[u] & languages[v]: continue
            # add the person to the dont speak lanaguage if they do not
            dont_speak.add(u)
            dont_speak.add(v)

        languages_count = Counter()

        for f in dont_speak:
            for l in languages[f]:
                languages_count[l] += 1

        return 0 if not dont_speak else len(dont_speak) - max(list(languages_count.values()))