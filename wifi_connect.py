def do_connect(ESSID,password):
    import network
    network.WLAN(network.AP_IF).active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ESSID, password)
        while not sta_if.isconnected():
            pass
        print("network config:", sta_if.ifconfig())
