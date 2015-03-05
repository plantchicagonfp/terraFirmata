#!/usr/bin/python 
# Copyright (c) 2012, Fabian Affolter <fabian@affolter-engineering.ch>
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of the pyfirmata team nor the names of its contributors
#   may be used to endorse or promote products derived from this software
#   without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pyfirmata
import time

# set localtime output to read in human language
localtime = time.asctime( time.localtime(time.time()) )

# Adjust that the port match your system, see samples below:
# On Linux: /dev/tty.usbserial-A6008rIF, /dev/ttyACM0, 
# On Windows: \\.\COM1, \\.\COM2
PORT = '/dev/ttyUSB0'

# Definition of the analog pin
PINS = ( 0,1,2,3)

# Creates a new board 
board = pyfirmata.ArduinoMega(PORT)
print "Setting up the connection to the board ..."
it = pyfirmata.util.Iterator(board)
it.start()

# Start reporting for defined pins
for pin in PINS:
    board.analog[pin].enable_reporting()

# Loop for reading the input. 5 reads
for i in range(1, 6):
    print "\nRead %i :" % i
    print localtime
    with open('out.txt', 'a') as txt_out:
        txt_out.write("\nRead %i , " % i)
        txt_out.write(localtime)
    for pin in PINS:
        print "Analog Pin %i : %s" % (pin, board.analog[pin].read() )
        with open('out.txt', 'a') as txt_out:
            txt_out.write(' , ')
            txt_out.write("Analog Pin %i : %s" % (pin, board.analog[pin].read() ))

    board.pass_time(1)

board.exit()
