#!/bin/sh

echo 0 > ~/.config/hypr/monitor_configs/mode

hyprctl keyword monitor eDP-1, highres, 0x0, 1
