def on_gesture_shake():
    basic.show_icon(IconNames.SURPRISED)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    basic.show_string("Jimmy")
basic.forever(on_forever)
