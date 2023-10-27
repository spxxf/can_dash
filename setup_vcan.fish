#!/usr/bin/env fish

sudo socat -u TCP-LISTEN:28600,reuseaddr,fork SYSTEM:'socat - /dev/$argv',nofork

