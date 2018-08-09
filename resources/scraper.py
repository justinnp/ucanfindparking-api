from bs4 import BeautifulSoup
import requests
import lxml

def get_avail():
    names = ['Garage A', 'Garage B', 'Garage C', 'Garage D', 'Garage H', 'Garage I', 'Garage Libra']
    maxes = [1623, 1259, 1852, 1241, 1284, 1231, 1007]

    req = requests.get('http://secure.parking.ucf.edu/GarageCount/')
    soup = BeautifulSoup(req.text, 'lxml')
    garages = soup.find('table')

    availabilities_in_tags = soup.find_all('strong')
    mappy = {}

    for i in range(0, 7):
        # I want to store all the numbers from the tags in a map
        g = {}
        curr =int(availabilities_in_tags[i].string)
        g['current'] = curr
        g['max'] = maxes[i]
        percent = curr / maxes[i] * 100
        percent = round(percent if percent < 100 else 100, 2)
        g['percentage_avail'] = percent
        g['percentage_full'] = round(100 - percent, 2)
        mappy[names[i]] = g

    return mappy
