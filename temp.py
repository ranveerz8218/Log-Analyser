def analyse_logs(logs):
    info = 0
    warning = 0
    error = 0
    unknown = 0
    total=0 
    for line in logs:
        total+=1
        if "INFO:" in line :
            info+=1
        elif "ERROR:" in line:
            error+=1
        elif "WARNING:" in line:
            warning+=1
        else:
            unknown+=1
    if total == 0:
        return 0,0,0,0,0,0,0,0,0
    infopercentage = info*100/total
    warningpercentage = warning*100/total
    errorpercentage = error*100/total
    unknownpercentage = unknown*100/total
    return total,info,warning,error,unknown,infopercentage,warningpercentage,errorpercentage,unknownpercentage
     

logs = [
    "INFO: Server started",
    "ERROR: Connection failed",
    "WARNING: High memory usage",
    "INFO: User logged in",
    "SOMETHING: Unknown event",
    "ERROR: File not found",
    "WARNING: Disk space low",
    "INFO: Backup completed"
]
total,info,warning,error,unknown,infopercentage,warningpercentage,errorpercentage,unknownpercentage = analyse_logs(logs)
print("TOTAL:",total)

print(f"INFO: {info}({infopercentage:.1f}%)")
print(f"ERROR: {error}({errorpercentage:.1f}%)")
print(f"WARNING: {warning}({warningpercentage:.1f}%)")
print(f"UNKNOWN: {unknown}({unknownpercentage:.1f}%)")
