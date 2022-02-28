#!/bin/bash
wget https://speed.hetzner.de/100MB.bin
rm -rf 100MB.bin
./loop.sh
