from __future__ import print_function
import sys
import libvirt
import csv
import datetime as dt
import time

domNames = ["java11", "java8"]  # vm names
measuramentTime = 5   # in seconds
measuramentInterval = 2  # in seconds

numberMeasuraments = round(measuramentTime / measuramentInterval)
conn = libvirt.open('qemu:///system')
if conn == None:
    print('Failed to open connection to qemu:///system', file=sys.stderr)
    exit(1)

dom = []
for x in domNames:
    dom.append(conn.lookupByName(x))
    if dom == None:
        print('Failed to find the domain '+domName, file=sys.stderr)
        exit(1)

with open('benchmark.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    rowToWrite = []
    for i in range(len(domNames)):
        rowToWrite.extend([domNames[i],"","","","","","","",""])
    writer.writerow(rowToWrite)

    rowToWrite = []
    for i in domNames:
        headers = ["Measurament Time(ns)", "Cpu time(ns)", "System time(ns)", "User time(ns)", "Memory allocated(B)", "Memory Unused(B)", "Memory available(B)", "Memory usable(B)", "Disk caches(B)"]
        rowToWrite.extend(headers)
    writer.writerow(rowToWrite)

    for n in range(numberMeasuraments):
        rowToWrite = []
        for vm in dom:
            statsCpu = vm.getCPUStats(True)
            statsMem = vm.memoryStats()
            rowToWrite.append(str(dt.datetime.now().time())[0:8])
            rowToWrite.extend([str(statsCpu[0]['cpu_time']), str(statsCpu[0]['system_time']), str(statsCpu[0]['user_time'])])
            for name in statsMem:
                if name in ["actual", "unused", "available", "usable", "disk_caches"]:
                    rowToWrite.append(statsMem[name])
        writer.writerow(rowToWrite)
        time.sleep(measuramentInterval)
conn.close()
exit(0)
