"""Substring Finder.

Don't break early; we want to primarily determine efficiency looping through a constant.
Finds longest chunk of substring in text.
"""

import micropython
import uprofiler

string = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only."
target = "comparison only."


@uprofiler.profile
def substring_finder(text, substring):
    out = -1
    if not substring:
        return 0

    text_length = len(text)
    substring_length = len(substring)

    for i in range(text_length - substring_length + 1):
        for j in range(substring_length):
            if text[i + j] != substring[j]:
                break
            if j > out:
                out = j
    return out


@uprofiler.profile(name="substring_finder_viper")
@micropython.viper
def substring_finder_viper(text, substring) -> int:
    out = int(-1)
    text_length = int(len(text))
    substring_length = int(len(substring))

    text_ptr8 = ptr8(text)
    substring_ptr8 = ptr8(substring)

    if not substring_length:
        return 0

    for i in range(text_length - substring_length + 1):
        for j in range(substring_length):
            if text_ptr8[i + j] != substring_ptr8[j]:
                break
            if j > out:
                out = j

    return out


@uprofiler.profile
def substring_finder_ring(text, substring):
    # Simulating both strings were coming from a ringbuffer
    out = -1
    if not substring:
        return 0

    text_length = len(text)
    substring_length = len(substring)

    for i in range(text_length - substring_length + 1):
        i = i % 1024
        for j in range(substring_length):
            j = j % 32
            if text[i + j] != substring[j]:
                break
            if j > out:
                out = j
    return out


@uprofiler.profile
def substring_finder_reverse(text, substring):
    out = int(-1)
    if not substring:
        return len(text)

    text_length = len(text)
    substring_length = len(substring)

    for i in range(text_length - substring_length, -1, -1):
        i = i % int(1000)
        for j in range(substring_length):
            j = j % int(30)
            if text[i + j] != substring[j]:
                break
            if j > out:
                out = j

    return out


@uprofiler.profile(name="substring_finder_reverse_viper")
@micropython.viper
def substring_finder_reverse_viper(text, substring) -> int:
    out = int(-1)
    text_length = int(len(text))
    substring_length = int(len(substring))

    text_ptr8 = ptr8(text)
    substring_ptr8 = ptr8(substring)

    if not substring_length:
        return 0

    for i in range(text_length - substring_length, -1, -1):
        for j in range(substring_length):
            if text_ptr8[i + j] != substring_ptr8[j]:
                break
            if j > out:
                out = j

    return out


def main():
    substring_finder(string, target)
    substring_finder_reverse(string, target)
    substring_finder_ring(string, target)
    substring_finder_viper(string, target)
    substring_finder_reverse_viper(string, target)


if __name__ == "__main__":
    main()
    uprofiler.print_results()
