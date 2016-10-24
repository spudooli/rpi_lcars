# Read and process data from files

# Return lines of text
def readtxt(filename):
    lines = []
    with open(filename, mode='r') as infile:
        lines = infile.read().splitlines() 

    return lines;

# Return CSV pairs
def readcsv(filename):
    lines = []
    with open(filename, mode='r') as infile:
        for line in infile.readlines():
            l,name = line.strip().split(',')
            lines.append((l,name))

    return lines;

# Return a dictionary with ip/status for given list index
def get_ip_status(sourcelist, index):
    ipstatus = {}
    ipaddr = str(sourcelist[index])[2:13]
    status = str(sourcelist[index])[18:-2]
    ipstatus = {"ip": ipaddr, "status": status}
    return ipstatus;
