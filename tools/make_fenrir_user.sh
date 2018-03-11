#!/bin/bash

# This script checks for, and creates if needed, the fenrirscreenreader user.

# find out if the input group exists, if not, create it
grep ^input: /etc/group &> /dev/null || {
    groupadd --system input
    echo 'KERNEL=="event*", NAME="input/%k", MODE="660", GROUP="input"' >> /etc/udev/rules.d/99-input.rules
}

# Add fenrirscreenreader
id fenrirscreenreader &> /dev/null || useradd -N -g input -s /bin/nologin  fenrirscreenreader
