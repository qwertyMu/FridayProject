import requests

def get_geolocation(ip_address):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_address}')
        data = response.json()

        if data['status'] == 'fail':
            print(f'Unable to find geolocation for IP address: {ip_address}')
            return None

        return data
    except Exception as e:
        print(f'Error occurred: {e}')
        return None

def main():
    ip_address = input('Enter an IP address: ')
    geolocation_data = get_geolocation(ip_address)

    if geolocation_data:
        print(f"IP Address: {ip_address}")
        print(f"Country: {geolocation_data['country']}")
        print(f"Region: {geolocation_data['regionName']}")
        print(f"City: {geolocation_data['city']}")
        print(f"ZIP: {geolocation_data['zip']}")
        print(f"Latitude: {geolocation_data['lat']}")
        print(f"Longitude: {geolocation_data['lon']}")
        print(f"ISP: {geolocation_data['isp']}")
    else:
        print("Geolocation data not found.")

if __name__ == '__main__':
    main()

