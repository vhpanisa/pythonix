#!/usr/pkg/bin/python2.7
# chmod: change permissions of given path

import sys
import os
import argparse

def _chp(path,mod):
  if mod.isdigit():
    mod = int(mod,8)
  elif mod.count('+') == 1 or mod.count('=') == 1:
    print('Invalid mask')
    return
    if '+' in mod and '=' in mod:
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    elif '+' in mod:
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    elif '=' in mod:
        pass
        pass
        pass
        pass
        pass
        pass
        pass
    else:
        print('Invalid mask')
        return
  else:
    print('Invalid mask')
    return
  os.chmod(path, mod)

def changep(path, mod, recursive=False):
  if recursive and os.path.isdir(path):
    for x in os.listdir(path):
      changep(x, mod, recursive=recursive)
  else:
    _chp(path, mod)


def main(argv):

  parser = argparse.ArgumentParser()

  parser.add_argument('-r', action='store_true',
    help='Remove recursively')
  parser.add_argument('-R', action='store_true',
    help='Remove recursively')
  parser.add_argument('args', nargs=argparse.REMAINDER)

  argv = parser.parse_args()

  if argv.R:
    argv.r = True

  if len(argv.args) == 0:
    print('Usage: chmod [-r] mode path')
    exit(0)

  changep(argv.args[1], argv.args[0], recursive=argv.r)

if __name__ == '__main__':
  main(sys.argv)
