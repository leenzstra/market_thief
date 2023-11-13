import time
from requests import Session

from model import ProductModel

categories = [1, 36861, 36883, 36895, 36893, 36885, 36881, 36879, 36877, 36875, 36867, 36865, 16869, 16865, 16881, 16883, 16887, 16885, 16675, 17481, 17473, 17475, 17477, 16871, 16737, 16733, 16543, 16547, 16549, 27557, 4841, 4843, 4845, 4854, 17637, 17639, 4844, 17627, 17629, 17631, 4851, 4847, 4850, 4848, 4849, 17489, 17491, 17493, 17495, 4837, 4842, 27187, 18063, 17621, 17623, 17625, 4836, 17673, 18061, 4839, 16967, 4887, 4893, 4894, 4886, 4885, 4889, 4890, 4891, 4892, 4568, 4564, 4565, 4566, 4567, 4552, 16533, 16461, 16531, 4548, 4551, 16349, 16351, 16353, 16355, 16357, 16359, 16361, 13385, 4437, 4440, 4442, 4534, 16535, 16537, 4538, 4540, 4541, 4557, 4558, 4559, 4560, 4561, 4562, 16265, 4531, 16337, 4532, 4866, 4868, 4867, 4873, 4870, 17977, 4864, 4869, 17607, 4859, 4862, 4861, 4871, 4863, 7361, 5010, 5002, 4999, 26741, 5001, 5003, 5006, 5007, 5008, 5009, 7499, 7498, 7501, 7502, 7507, 7508, 7500, 7503, 7504, 7505, 7506, 7509, 17483, 35739, 7511, 17603, 17605, 37255, 37257, 37259, 37265, 37267, 37269, 37251, 37241, 37243, 7491, 37229, 7512, 7513, 7516, 7517, 7519, 27729, 7559, 7633, 16561, 16575, 16565, 16567, 16563, 16581, 16585, 16583, 7199, 7201, 7198, 7202, 7217, 7730, 7218, 7215, 7216, 7763, 7204, 7210, 7205, 7209, 7208, 7206, 7207, 7213, 7214, 7212, 7836, 7225, 7226, 7844, 7845, 7219, 7220, 7221, 7222, 7365, 35737, 16399, 16401, 16395, 16393, 16403, 16397, 16375, 16367,
              16371, 18739, 16383, 16381, 16387, 16389, 16373, 12791, 12783, 12785, 16151, 12787, 12793, 12775, 12769, 12771, 12773, 12767, 5277, 16181, 5279, 18433, 18437, 18435, 18123, 18345, 18339, 18343, 18341, 5273, 5275, 7157, 4875, 4883, 4879, 4880, 17169, 4876, 4882, 7764, 12437, 12439, 12541, 12695, 12751, 16143, 16145, 16147, 16149, 12697, 12443, 12547, 18615, 18489, 18491, 18487, 4460, 4462, 4463, 4464, 18485, 18481, 18483, 18479, 4467, 4461, 27991, 27987, 27997, 28001, 28035, 28019, 28015, 28011, 28009, 28033, 28049, 28037, 23521, 17915, 17909, 17911, 17931, 17933, 33001, 17929, 36983, 18105, 19675, 19677, 37025, 37027, 28371, 28373, 28375, 28377, 28381, 7878, 33047, 27773, 27819, 27821, 27831, 32909, 32875, 32877, 32879, 32959, 4526, 4507, 18083, 18099, 33037, 37357, 36823, 36821, 27559, 4335, 4336, 4337, 4341, 4343, 4323, 27633, 27641, 4363, 33507, 27643, 4350, 4351, 4353, 37191, 37199, 4325, 37195, 34749, 37183, 4272, 4208, 4320, 4374, 4373, 4372, 36209, 7636, 4371, 4346, 7771, 28513, 28517, 28521, 5108, 36817, 7521, 4360, 28483, 28485, 5177, 7663, 7687, 37303, 37301, 7815, 7710, 5142, 32985, 32989, 7761, 5145, 5146, 5233, 5148, 5128, 28641, 5087, 5083, 5086, 27775, 27133, 27135, 27143, 27145, 27155, 27165, 5131, 5099, 5105, 28595, 28601, 5181, 7767, 23285, 23287, 23289, 23293, 23291, 23187, 23191, 23193, 23195, 23199, 23235, 23237, 23239, 23241, 23243, 23245, 23247, 23249, 23251]

whitelist = ['moloko-syr-yaytsa', 'ovoshchi-i-frukty','bakaleya-sousy','myaso-ptitsa','sosiski-kolbasy-delikatesy','ryba-i-moreprodukty','sladosti-torty-pirozhnye','konservy-myod-varenye','chay-kofe-kakao','khleb-vypechka','napitki','chipsy-orekhi-sukhariki','zamorozhennye-produkty','']

class MagnitParser:
    def __init__(self, stockId=1, deviceId='d86dpcdvok') -> None:
        self.stockId = stockId
        client = Session()
        client.headers['User-Agent'] = 'Mozilla/5.0 (Linux; U; Linux i674 ) Gecko/20130401 Firefox/62.8'
        client.headers['X-Device-Id'] = deviceId
        client.headers['X-App-Version'] = '0.1.0'
        client.headers['X-Client-Name'] = 'magnit'
        client.headers['X-Client-Platform'] = 'Web'
        client.headers['X-Device-Tag'] = 'disabled'
        client.headers['X-Platform-Version'] = 'window.navigator.userAgent'
        client.headers['Origin'] = 'https://magnit.ru'
        self.client = client

    def total_products(self):
        url = 'https://web-gateway.middle-api.magnit.ru/v1/goods/filters'
        r = self.client.post(url, json={'categoryIDs': categories, 'includeForAdults': True,
                             "shopType": "1", "storeCodes": ["773797"], "filters": []})
        
        return r.json()['pagination']['totalCount']
    
    def fetch_categories(self):
        url = f'https://web-gateway.middle-api.magnit.ru/v2/goods/categories?StoreCode={self.stockId}'
        r = self.client.get(url)

        data = r.json()
        return [ctg for ctg in data if ctg['code'] in whitelist]
    
    def get_subcategory_ids(self, category: dict):
        def helper(category: dict) -> list[int]:
            ids = []
            for subctg in category['children']:
                ids += helper(subctg)
            ids.append(category['id'])
            return ids

        return helper(category)

    
    def fetch_products(self, category_ids: list, v=False, sleep_sec = 1) -> list:
        page = 1
        page_size = 100
        total_pages = 1
        products = []

        while page <= total_pages:
            url = 'https://web-gateway.middle-api.magnit.ru/v3/goods'
            r = self.client.post(url, json={"categoryIDs": category_ids, "includeForAdults": True, "onlyDiscount": False, "order": "desc", "pagination": {
                                "number": page, "size": page_size}, "shopType": "1", "sortBy": "price", "storeCodes": [str(self.stockId)], "filters": []})
            
            print(r.content)
            data = r.json()
            

            if len(data['goods']) == 0:
                if v: 
                    print('category', category_ids, 'no products')
                break

            total_pages = data['pagination']['totalPages']
            page += 1

            for p in data['goods']:
                if len(p['offers']):
                    price = str(p['offers'][0]['price']).replace(',','.')
                    products.append(
                        {'id': p['id'], 'name': p['name'], 'code': p['code'], 'price': float(price)})

            if v:
                print('url', url, len(products))

            time.sleep(sleep_sec)

        return products
    
    def start(self) -> list[ProductModel]:
        ctgs = self.fetch_categories()

        all_products = []

        time.sleep(1)
        for ctg in ctgs:
            if ctg['code'] not in whitelist:
                continue
            print(ctg['name'])
            ctg_ids = self.get_subcategory_ids(ctg)
            # print(ctg_ids)
            products = self.fetch_products(
                category_ids=ctg_ids, v=True, sleep_sec=0.5)
            data = [ProductModel(product_id=p['id'], name=p['name'], code=p['code'], category=ctg['name'],
                        category_code=ctg['code'], price=p['price']) for p in products]
            all_products += data

        return all_products