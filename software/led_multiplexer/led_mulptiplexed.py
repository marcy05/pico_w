import machine
import utime

select_list = [(0,0,0,0),
               (1,0,0,0),
               (0,1,0,0),
               (1,1,0,0),
               (0,0,1,0),
               (1,0,1,0),
               (0,1,1,0),
               (1,1,1,0),
               (0,0,0,1),
               (1,0,0,1),
               (0,1,0,1),
               (1,1,0,1),
               (0,0,1,1),
               (1,0,1,1),
               (0,1,1,1),
               (1,1,1,1)]


s0 = machine.Pin(16, machine.Pin.OUT)
s1 = machine.Pin(17, machine.Pin.OUT)
s2 = machine.Pin(18, machine.Pin.OUT)
s3 = machine.Pin(19, machine.Pin.OUT)
sig = machine.Pin(20, machine.Pin.OUT)

led_status = [False]*16

def toggle(channel: int):
    global led_status
    if led_status[channel] == False:
        led_status[channel] = True
        sig.value(True)
        print("Enabled channel: {}".format(channel))
    else:
        led_status[channel] = False
        sig.value(False)
        print("Disabled channel: {}".format(channel))

def enabler(channel: int, signal: bool):
    global select_list, s0, s1, s2, s3
    if channel < 16:
        s0.value(select_list[channel][0])
        s1.value(select_list[channel][1])
        s2.value(select_list[channel][2])
        s3.value(select_list[channel][3])
        toggle(channel)
        print("{}, {}, {}, {}".format(select_list[channel][0], select_list[channel][1], select_list[channel][2], select_list[channel][3]))
        #print(select_list[channel])
    else:
        print("Impossible to select channel: {}. Out of ragne".format(channel))
    
def init():
    for channel in range(0, 16):
        s0.value(select_list[channel][0])
        s1.value(select_list[channel][1])
        s2.value(select_list[channel][2])
        s3.value(select_list[channel][3])
        sig.value(False)
    
init()
while True:
#    for i in range(11, 16, 1):
#        enabler(i, True)
#        utime.sleep(3)
    enabler(15, True)
    utime.sleep(1)
    print("\n")

    