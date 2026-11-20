def read_logs(filename):
    # Read logs from a file
    try:
        with open(filename,"r") as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print("Log file is not found")
        return None
    
def analyse_logs(logs):
    #Classify logs and calculate statistics.
    info = 0
    warning = 0
    error = 0
    unknown = 0

    total = len(logs)

    if total == 0:
        return 0, 0, 0, 0, 0, 0, 0, 0, 0

    for line in logs:
        if "INFO:" in line:
            info += 1
        elif "WARNING:" in line:
            warning += 1
        elif "ERROR:" in line:
            error += 1
        else:
            unknown += 1

    infopercentage = info * 100 / total
    warningpercentage = warning * 100 / total
    errorpercentage = error * 100 / total
    unknownpercentage = unknown * 100 / total

    return (total, info, warning, error, unknown,
            infopercentage, warningpercentage,
            errorpercentage, unknownpercentage)

def display_report(results):
    #Display the analysis report.
    total, info, warning, error, unknown, ip, wp, ep, up = results

    print("\n===== LOG ANALYSIS REPORT =====")
    print("TOTAL:", total)

    print(f"INFO:    {info} ({ip:.1f}%)")
    print(f"WARNING: {warning} ({wp:.1f}%)")
    print(f"ERROR:   {error} ({ep:.1f}%)")
    print(f"UNKNOWN: {unknown} ({up:.1f}%)")

    print("===============================")

reading=read_logs("server.log")
print(reading)
result=analyse_logs(reading)
print(result)
