#!/usr/bin/env python

import sys
import random

# This will explode us if we happen to get all 10 digits to be the same value. Hopefully that doesn't happen! :P
def randomize_counts(counts):
  for i in xrange(10):
    counts[i] = random.randint(0,9)

# Find a self describing 10 digit number such that pos 0 is a count of 0s, pos 1 is a count of 1s, etc
def main():
  hist = []
  counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  randomize_counts(counts)
  while True:
    new_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in counts:
      new_counts[i] += 1
    if counts == new_counts:
      print "We did it!"
      print counts
      sys.exit(0);
    counts = new_counts
    print counts
    for a in hist:
      if counts == a:
        print "loop!"
        randomize_counts(counts)
        hist = []
    hist.append(counts)
    if len(hist) > 5:
      hist = hist[1:]

if __name__ == '__main__':
  main()
