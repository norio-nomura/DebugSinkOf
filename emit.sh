#!/bin/sh

# swift-demangle-filter.py comes from https://gist.github.com/norio-nomura/121ef3eacbc6dda87dad

./swift-demangle-filter.py debug.swift -emit-sil -O -o debug-O.sil
./swift-demangle-filter.py debug.swift -emit-sil -Onone -o debug-Onone.sil
./swift-demangle-filter.py non-debug.swift -emit-sil -O -o non-debug-O.sil
./swift-demangle-filter.py non-debug.swift -emit-sil -Onone -o non-debug-Onone.sil
diff -u non-debug-Onone.sil debug-Onone.sil>diff-between-non-debug-Onone-and-debug-Onone.diff
diff -u non-debug-O.sil debug-O.sil>diff-between-non-debug-O-and-debug-O.diff
