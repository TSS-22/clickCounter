from pynput import mouse

class CounterMamen:
    i = 0

def on_click(x, y, button, pressed):
    if pressed:
        CounterMamen.i += 1
    print(CounterMamen.i)
    

with mouse.Listener(on_click=on_click) as listener:
    listener.join()
    
listener = mouse.Listener(on_click=on_click)
listener.start()