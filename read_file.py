def credentialsRead(filename):
    file = open(filename,"r")
    f = file.read()
    f = f.split("\n")
    credentials = []
    for line in f:
        credentials.append(line)
    file.close()
    return credentials
