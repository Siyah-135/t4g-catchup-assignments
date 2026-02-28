#!/bin/bash
Name="Hasiyatu Ismail"
echo "Hello, my name is $Name"

echo "current date and time : $(date)"

mkdir -p session_logs

LOGFILE="session_logs/$(date +%Y-%m-%d).log"

echo "Name: $Name" >> $LOGFILE
echo "Still practicing till I become a pro." >> $LOGFILE
 echo "setup complete!"

