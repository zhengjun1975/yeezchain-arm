#!/bin/bash
ADDRESS=`cat /root/.keys/names/Validator_0`
cd /rpc
python3 generator.py --source $ADDRESS --target $ADDRESS &
