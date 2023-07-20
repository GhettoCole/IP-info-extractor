import requests
from tabulate import tabulate

class IPLocator:
    def __init__(self, ipAddress):
        self.ipAddress = ipAddress
    
    def get_location(self):
        try:
            url = f"https://freegeoip.app/json/{self.ipAddress}"
            response = requests.get(url)
            response.raise_for_status()  # Check for any request errors
            jsonFile = response.json()

            table_data = {
                "Region": jsonFile['region_name'],
                "Country Code": jsonFile['country_code'],
                "Latitude": jsonFile['latitude'],
                "Longitude": jsonFile['longitude'],
                "IP": jsonFile['ip'],
                "ZIP Code": jsonFile['zip_code'],
                "Time Zone": jsonFile['time_zone'],
                "Country Name": jsonFile['country_name'],
                "City": jsonFile['city']
            }

            table = tabulate([table_data], headers="keys", tablefmt="grid")
            print(table)

        except requests.exceptions.RequestException as e:
            print("Error: Unable to fetch data. Please check your internet connection.")
        except requests.exceptions.HTTPError as e:
            print("HTTP Error:", e)
        except requests.exceptions.JSONDecodeError as e:
            print("Error: Invalid JSON response from the server.")
        except KeyError as e:
            print("Error: Missing key in JSON response.")
        except Exception as e:
            print("Error:", e)

def main():
    ipAddr = input("Enter IP Address: ")
    try:
        ipLookup = IPLocator(ipAddr)
        ipLookup.get_location()
    except Exception as e:
        print("Error:", str(e))
    finally:
        print("""
        -->\tProgrammer: Given Lepita
        -->\tProject: Simple IP Lookup
        -->\tDate: November 2017
        -->\tDescription: Finds several information given an IP.
        """)

if __name__ == "__main__":
    main()
