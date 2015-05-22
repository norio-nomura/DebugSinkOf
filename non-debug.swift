#!/usr/bin/env xcrun swift

class Counter {
    var number = 0
    func update(newValue: Int) {
        number = newValue
    }
}

let c = SinkOf<Int>(Counter().update)
c.put(128)
