#!/bin/bash
./start_chain.sh
sleep 10
./transaction_generator.sh
sleep 10
./start_explorer.sh
