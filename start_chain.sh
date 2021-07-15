#!/bin/bash
FAIL_LOG=" Failed! Please Get Valid License File with "
export YEEZ=./yeez

while true
do
  RET=`$YEEZ --version`
  if [[ $RET == *$FAIL_LOG* ]]; then
    echo $RET
  else
    $YEEZ spec -v1 | $YEEZ configure -s- --empty-blocks 5s | $YEEZ start -c- &
    break
  fi
  sleep 10
done
