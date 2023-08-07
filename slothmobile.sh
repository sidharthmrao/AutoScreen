#!/bin/sh

echo 0 > mode

wlr-randr \
	--output eDP-1 --mode 1920x1080 --pos 0,0 --transform normal \
