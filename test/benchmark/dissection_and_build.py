# This file is part of Scapy
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) Guillaume Valadon
# This program is published under a GPLv2 license

import time

from scapy.all import *
from scapy.modules.six.moves import range

if WINDOWS:
    route_add_loopback()

N = 10000
raw_packet = b'E\x00\x00(\x00\x01\x00\x00@\x11|\xc2\x7f\x00\x00\x01\x7f\x00\x00\x01\x005\x005\x00\x14\x00Z\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'

start = time.time()
for i in range(N):
    p = IP() / UDP() / DNS()
    assert raw(p) == raw_packet
print("Build - %.2fs" % (time.time() - start))

start = time.time()
for i in range(N):
    p = IP(raw_packet)
    assert DNS in p
print("Dissect - %.2fs" % (time.time() - start))

start = time.time()
for i in range(N):
    p = IP() / UDP() / DNS()
    s = raw(p)
    assert s == raw_packet
    p = IP(s)
    assert DNS in p
print("Build & dissect - %.2fs" % (time.time() - start))
