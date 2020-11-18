#!/bin/sh
Xvfb :99 -ac -screen 0 ${SCREEN_HEIGHT}x${SCREEN_WIDTH}x${SCREEN_COLOUR_DEPTH} & nice -n 10 x11vnc 2>&1 & robot ${ROBOT_TESTS_FOLDER}