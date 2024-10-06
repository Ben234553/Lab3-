#!/usr/bin/env python3
'''Lab 3 Part 4: Free Disk Space on Root Directory'''
# Author ID: 123236218

import subprocess

def free_space():
    # Launch the Linux command and capture the output
    process = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Get the command output and errors (if any)
    output, error = process.communicate()
    
    # Ensure the output is in utf-8 and remove newline characters
    if output:
        return output.decode('utf-8').strip()
    else:
        return error.decode('utf-8').strip()

if __name__ == '__main__':
    print(f"Free space on root: {free_space()}")
