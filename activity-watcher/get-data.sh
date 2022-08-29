#!/usr/bin/env bash
SOURCE=$1
TARGET=$2
sqlite3 -batch -header -separator "ء"\
    "${SOURCE}" \
    "select * from events where datetime(ROUND(starttime/1000000000), 'unixepoch', 'localtime') >= datetime('now', '-1 month', 'start of month', 'localtime') and datetime(ROUND(starttime/1000000000), 'unixepoch', 'localtime') < datetime('now', 'start of month', 'localtime')" \
    > "${TARGET}"
