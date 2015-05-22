#!/usr/bin/env xcrun swift

public struct DebugSinkOf<T> : SinkType {
    typealias Element = T

    let putElement: (T) -> ()

    /// Construct an instance whose `put(x)` calls `putElement(x)`
    public init(_ putElement: (T) -> ()) {
        self.putElement = putElement
    }

    /// Construct an instance whose `put(x)` calls `base.put(x)`
    public init<S : SinkType where S.Element == T>(var _ base: S) {
        self.putElement = {base.put($0)}
    }

    /// Write `x` to this sink.
    public func put(x: T) {
        putElement(x)
    }
}

class Counter {
    var number = 0
    func update(newValue: Int) {
        number = newValue
    }
}

let c = DebugSinkOf<Int>(Counter().update)
c.put(128)
