import time
from requests import Session

from model import ProductModel

whitelist = ['voda-soki-napitki', 'chay-kofe-sladosti',
             'bakaleya', 'konditerskie_izdeliya', 'hlebnaya-vypechka', 'ryba-ikra-moreprodukty', 'zamorozhennye-produkty', 'orehi-suhofrukty-sneki', 'ovoschi-frukty-zelen-griby-yagody', 'kolbasnye-izdeliya', 'ptica-myaso', 'syry', 'moloko-syr-yayca', 'alkogol']


class AshanParser():
    def __init__(self, stockId = 1) -> None:
        self.stockId = stockId
        self.client = Session()
        self.client.headers.update(
            {'User-Agent': 'Mozilla/5.0 (Linux; U; Linux i674 ) Gecko/20130401 Firefox/62.8'})


    def fetch_categories(self):
        r = self.client.get(
            f'https://www.auchan.ru/v1/categories?max_depth=1&merchant_id={self.stockId}')

        categories = []

        for i, ctg in enumerate(r.json()):
            category = {'name': ctg['name'], 'code': ctg['code'], 'children': []}

            for j, subctg in enumerate(ctg['items']):
                subcategory = {
                    'name': subctg['name'], 'code': subctg['code'], 'count': subctg['activeProductsCount']}
                category['children'].append(subcategory)

            categories.append(category)

        return categories


    def fetch_products(self, category, per_page=100, sleep_sec=1, v=False):
        page = 1
        num_parsed = 0
        total_count = 0

        products = []
        ids = set()

        while num_parsed == 0 or num_parsed < total_count:
            url = f'https://www.auchan.ru/v1/catalog/products?merchantId={
                self.stockId}&page={page}&perPage={per_page}'
            r = self.client.post(url, json={"filter": {"category": category, }, },)
            data = r.json()
            total_count = data['activeRange']
            num_parsed += len(data['items'])
            if total_count - num_parsed < per_page:
                per_page = total_count - num_parsed

            page += 1
            if v:
                print('url', url, 'total', total_count)

            for item in data['items']:
                if item['id'] not in ids:
                    products.append(
                        {'id': item['id'], 'name': item['title'], 'code': item['code'], 'price': item['price']['value']})
                    ids.add(item['id'])

            time.sleep(sleep_sec)

        return products


    def fetch_product_details(self):
        url = 'https://www.auchan.ru/v1/catalog/product-detail?code=syr_rossiyskiy_rovenki&merchantId=1'

    def start(self) -> list[ProductModel]:
        ctgs = self.fetch_categories()

        all_products = []

        time.sleep(1)
        for ctg in ctgs:
            if ctg['code'] not in whitelist:
                continue
            print(ctg['name'])
            products = self.fetch_products(category=ctg['code'], v=True, sleep_sec=0.3)
            data = [ProductModel(product_id=p['id'], name=p['name'], code=p['code'], category=ctg['name'],
                        category_code=ctg['code'], price=p['price']) for p in products]
            all_products += data

        return all_products
            
