import re

def findIPAddresses(text):
    ipPattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    return re.findall(ipPattern, text)

# Test the Regular Expression
if __name__ == "__main__":
    # testing using different ip addresses 
    testText = "The IP address is 192.168.32.1. Another one is 10.0.0.1. 10.03.23.0 0.0.0.0"
    ipAddresses = findIPAddresses(testText)
    # print found result
    print("IP Addresses found:", ipAddresses)
