def on_forever():
    basic.show_number(input.temperature())
    basic.pause(1000)
    basic.clear_screen()
basic.forever(on_forever)
