start = int(raw_input("Starting #: "))
end = int(raw_input("Ending #: "))

for i in range(start, (end + 1)):
    if start < end:
        print i
    else:
        print "Starting number cannot be greater than ending number!"
        break