import os
import datetime

print("="*50)
print(" Simple Network Scanner ")
print("="*50)

target = input("Enter target IP or domain: ")

print("\nScanning Target:", target)
print("Time:", datetime.datetime.now())
print("-"*50)

filename = "scan_result.txt"

command = f"nmap -sV {target} > {filename}"

os.system(command)

print("\nScan Complete!")
print("Results saved in:", filename)
print("="*50)
