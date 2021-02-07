input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Surprised)
})
basic.forever(function on_forever() {
    basic.showString("Jimmy")
})
