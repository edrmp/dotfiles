from i3pystatus import Status

status = Status()

status.register("clock", format="%Y-%m-%d %H:%M")

status.register("load")

status.register("keyboard_locks")

status.register("xkblayout", layouts=["us","us intl"])


status.run()
