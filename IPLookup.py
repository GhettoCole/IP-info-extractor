from json import loads
from urllib.request import urlopen
from prettytable import PrettyTable

class IPLocator:
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
    
    def getLocation(self):
        # request a json file using Freegeoip API
        request = urlopen("https://freegeoip.net/json/"+str(self.ipAddress)).read().decode("utf-8")
        jsonFile = loads(request)

        region = jsonFile['region_name']
        countryCode = jsonFile['country_code']
        latitude = jsonFile['latitude']
        longitude = jsonFile['longitude']
        ipAddr = jsonFile['ip']
        zipCode = jsonFile['zip_code']
        timeZone = jsonFile['time_zone']
        countryName = jsonFile['country_name']
        city = jsonFile['city']

        table = PrettyTable()
        table.field_names = [
            "Region", "Country Code", "Latitude",
            "Longitude", "IP", "ZIP Code", "Time Zone",
            "Country Name", "City"
            ]
        table.add_row(
            [
                region, countryCode, latitude, longitude,
                ipAddr, zipCode, timeZone, countryName, city
                ]
            )
        table.align = "r"
        print(table)

def main():
    ipAddr = input("Enter IP Address:   ")
    try:
        ipLookup = IPLocator(ipAddr)
        ipLookup.getLocation()
    except Exception as e:
        print("Error:   ", str(e))
    finally:
        print("""
        -->\tProgrammer:  Given Lepita
        -->\tProject: Simple IP Lookup
        -->\tDate: November 2017
        -->\tDescription: Finds several information given an IP.
        """)

if __name__ == "__main__":
    main()