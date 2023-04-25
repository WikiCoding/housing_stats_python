from flask import Flask
from bs4_Class import FindData

app = Flask(__name__)

@app.route('/')
def home_page():
    return '<h1>Hello!</h1>

@app.route('/stats')
def get_stats():
    vng = FindData('Vila Nova de Gaia - Imovirtual')
    vng_prices = []
    vng_prices_page1 = vng.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/vila-nova-de-gaia/?search%5Bregion_id%5D=13&search'
        '%5Bsubregion_id%5D=195&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in vng_prices_page1:
        vng_prices.append(price)
    count_vng = 2
    while count_vng <= 2:
        prices_other_pages = vng.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/?search%5Bregion_id%5D=13&search'
            f'%5Bsubregion_id%5D=190&nrAdsPerPage=72&page={count_vng}', 'li', 'offer-item-price')
        for price in prices_other_pages:
            vng_prices.append(price)
        count_vng += 1

    vng_data = vng.stats(vng_prices)

    porto = FindData('Porto - Imovirtual')
    porto_prices = []
    porto_prices_page1 = porto.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/porto/?search%5Bregion_id%5D=13&search%5Bsubregion_id%5D=190&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in porto_prices_page1:
        porto_prices.append(price)
    count_porto = 2
    while count_porto <= 4:
        prices_other_pages = porto.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/?search%5Bregion_id%5D=13&search'
            f'%5Bsubregion_id%5D=190&nrAdsPerPage=72&page={count_porto}', 'li', 'offer-item-price')
        for price in prices_other_pages:
            porto_prices.append(price)
        count_porto += 1
    porto_data = porto.stats(porto_prices)

    aveiro = FindData('Aveiro - Imovirtual')
    aveiro_prices = []
    aveiro_prices_page1 = aveiro.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/aveiro/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=1&search%5Bsubregion_id%5D=5&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in aveiro_prices_page1:
        aveiro_prices.append(price)
    count_aveiro = 2
    while count_aveiro <= 1:
        prices_other_pages = aveiro.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/aveiro/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=1&search%5Bsubregion_id%5D=5&nrAdsPerPage=72&page={count_aveiro}',
            'li', 'offer-item-price')
        for price in prices_other_pages:
            aveiro_prices.append(price)
        count_aveiro += 1
    aveiro_data = aveiro.stats(aveiro_prices)

    aveiro_dist = FindData('Aveiro District - Imovirtual')
    aveiro_dist_prices = []
    aveiro_dist_prices_page1 = aveiro_dist.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/aveiro/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=1&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in aveiro_dist_prices_page1:
        aveiro_dist_prices.append(price)
    count_aveiro_dist = 2
    while count_aveiro_dist <= 1:
        prices_other_pages = aveiro_dist.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/aveiro/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=1&search%5Bsubregion_id%5D=5&nrAdsPerPage=72&page={count_aveiro_dist}',
            'li', 'offer-item-price')
        for price in prices_other_pages:
            aveiro_dist_prices.append(price)
        count_aveiro_dist += 1
    aveiro_dist_data = aveiro_dist.stats(aveiro_dist_prices)

    braga = FindData('Braga - Imovirtual')
    braga_prices = []
    braga_prices_page1 = braga.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/braga/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=3&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in braga_prices_page1:
        braga_prices.append(price)
    count_braga = 2
    while count_braga <= 1:
        prices_other_pages = braga.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=3&nrAdsPerPage=72&page={count_braga}',
            'li', 'offer-item-price')
        for price in prices_other_pages:
            braga_prices.append(price)
        count_braga += 1
    braga_data = braga.stats(braga_prices)

    braga_dist = FindData('Braga District - Imovirtual')
    braga_dist_prices = []
    braga_dist_prices_page1 = braga_dist.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/braga/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=3&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in braga_dist_prices_page1:
        braga_dist_prices.append(price)
    count_braga_dist = 2
    while count_braga_dist <= 2:
        prices_other_pages = braga_dist.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=3&nrAdsPerPage=72&page={count_braga_dist}',
            'li', 'offer-item-price')
        for price in prices_other_pages:
            braga_dist_prices.append(price)
        count_braga_dist += 1
    braga_dist_data = braga_dist.stats(braga_dist_prices)

    viana_dist = FindData('Viana do Castelo District - Imovirtual')
    viana_dist_prices = []
    viana_dist_prices_page1 = viana_dist.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/viana-do-castelo/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=16&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in viana_dist_prices_page1:
        viana_dist_prices.append(price)
    count_viana_dist = 2
    while count_viana_dist <= 1:
        prices_other_pages = braga_dist.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=3&nrAdsPerPage=72&page={count_viana_dist}',
            'li', 'offer-item-price')
        for price in prices_other_pages:
            viana_dist_prices.append(price)
        count_viana_dist += 1
    viana_dist_data = viana_dist.stats(braga_dist_prices)

    lisboa = FindData('Lisboa - Imovirtual')
    lisboa_prices = []
    lisboa_prices_page1 = lisboa.find_prices(
        'https://www.imovirtual.com/arrendar/apartamento/lisboa/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=11&search%5Bsubregion_id%5D=153&nrAdsPerPage=72',
        'li', 'offer-item-price')
    for price in lisboa_prices_page1:
        lisboa_prices.append(price)
    count_lisboa = 2
    while count_lisboa <= 9:
        prices_other_pages = lisboa.find_prices(
            f'https://www.imovirtual.com/arrendar/apartamento/?search%5Border%5D=filter_float_price%3Aasc&search%5Bregion_id%5D=11&search%5Bsubregion_id%5D=153&nrAdsPerPage=72&page={count_lisboa}',
            'li', 'offer-item-price')
        for price in prices_other_pages:
            lisboa_prices.append(price)
        count_lisboa += 1
    lisboa_data = lisboa.stats(lisboa_prices)

    data_list = [
        vng_data, porto_data, aveiro_data, aveiro_dist_data, braga_data, braga_dist_data, viana_dist_data, lisboa_data
    ]

    return data_list

if __name__ == "__main__":
    app.run(debug=True)  # do the same as working with nodemon
