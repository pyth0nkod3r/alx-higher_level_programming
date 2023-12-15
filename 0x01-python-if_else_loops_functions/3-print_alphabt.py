#!/usr/bin/python
for alphabet in range(97, 123):
    if chr(alphabet) == 'q' or chr(alphabet) == 'e':
        continue
    print("".join(chr(alphabet)), end='')