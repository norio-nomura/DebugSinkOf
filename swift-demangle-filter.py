#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# usage: swift-demangle-filter.py [-h] [-o <outfile>] [<file> <options>]
#
# Read swift assembly, demangle Swift Symbol and output it.
#
# positional arguments:
#   <file> <options>  If <file> has .swift, compile it with <options>; or read
#                     (<file> or <stdin>) as assembly.
#
# optional arguments:
#   -h, --help        show this help message and exit
#   -o <outfile>      write output to <outfile>
#
import sys, re, argparse
from subprocess import Popen, PIPE

# build parser
parser = argparse.ArgumentParser(description="Read swift assembly, demangle Swift Symbol and output it.")
group = parser.add_mutually_exclusive_group(required=False)
parser.add_argument('-o', default=sys.stdout, type=argparse.FileType('wb', 0),
                    help='write output to <outfile>', metavar='<outfile>')
parser.add_argument('source', nargs='?', default=sys.stdin, type=argparse.FileType('r'),
                    help='If <file> has .swift, compile it with <options>; or read (<file> or <stdin>) as assembly.', metavar='<file> <options>')
(args, moreArgs) = parser.parse_known_args()

# prepare assembly
if args.source.name.endswith('.swift'):
  x = ['xcrun', '-sdk', 'macosx', 'swiftc', '-emit-assembly']
  x.extend(moreArgs)
  x.append(args.source.name)
  assembly = Popen(x, stdout=PIPE).communicate()[0].splitlines(True)
else:
  assembly = args.source

# run filter
demangledSymbols = {}
reSymbol = re.compile('([_@]?_[_a-zA-Z0-9]+)')

for line in assembly:
  symbols = set(reSymbol.findall(line))
  for symbol in symbols:
    demangledSymbol = demangledSymbols.get(symbol)
    if not demangledSymbol:
      demangledSymbol = Popen(['xcrun', 'swift-demangle', '-compact', symbol.replace('@','_')], stdout=PIPE).communicate()[0].splitlines()[0]
      if symbol.endswith(demangledSymbol): # demangle failed
        demangledSymbol = symbol
      demangledSymbols[symbol] = demangledSymbol
    line = line.replace(symbol, demangledSymbol)
  args.o.write(line)
