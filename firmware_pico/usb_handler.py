
import usb.core
import usb.util

inep = None
outep = None


def init_usb():
    global inep, outep

    # find our device
    dev = usb.core.find(idVendor=0xaffe, idProduct=0x0404)
    #dev = usb.core.find(idVendor=0x0000, idProduct=0x0001)
    # was it found?
    if dev is None:
        raise ValueError('Device not found')

    # get an endpoint instance
    cfg = dev.get_active_configuration()
    intf = cfg[(0, 0)]

    outep = usb.util.find_descriptor(
        intf,
        # match the first OUT endpoint
        custom_match= \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_OUT)

    inep = usb.util.find_descriptor(
        intf,
        # match the first IN endpoint
        custom_match= \
            lambda e: \
                usb.util.endpoint_direction(e.bEndpointAddress) == \
                usb.util.ENDPOINT_IN)

    assert inep is not None
    assert outep is not None

packet_counter=0;
read_size=512;

def continous_read():
    global packet_counter;
    while True:
        from_device = inep.read(read_size)
        #read_str = ''.join([chr(x) for x in from_device])
        #for i in range(0,read_size,64):
        #    read_str = ''.join('{:02x}'.format(x) for x in from_device[i : i+4])
        #    print(read_str)
        packet_counter +=1;

        #if read_str == "lalala this is a tst ;=) I will just fill the buffer to a length":
        #    packet_counter +=1;
        #else:
        #    print("read string does not match excepted!")

