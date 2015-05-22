# `DebugSinkOf`

Using two Swift sources
- Code using `SinkOf` is [non-debug.swift](non-debug.swift)
- Code using `DebugSinkOf` instead of `SinkOf` is [debug.swift](debug.swift)

Generating SIL codes using [swift-demangle-filter.py](https://gist.github.com/norio-nomura/121ef3eacbc6dda87dad)

for [non-debug.swift](non-debug.swift)
- Output using `-emit-sil -Onone` is [non-debug-Onone.sil](non-debug-Onone.sil)
- Output using `-emit-sil -O` is [non-debug-O.sil](non-debug-O.sil)

for [debug.swift](debug.swift)
  - Using `-emit-sil -Onone` is [debug-Onone.sil](debug-Onone.sil)
  - Using `-emit-sil -Onone` is [debug-O.sil](debug-O.sil)

Diffs
- Between [non-debug-Onone.sil](non-debug-Onone.sil) and [debug-Onone.sil](debug-Onone.sil) is [here](diff-between-non-debug-Onone-and-debug-Onone.diff)
- Between [non-debug-O.sil](non-debug-O.sil) and [debug-O.sil](debug-O.sil) is [here](diff-between-non-debug-O-and-debug-O.diff)
