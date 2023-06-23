import requests
import json


def get_data():
	import requests

	cookies = {
		'COMPARISON_INDICATOR': 'false',
		'HINTS_FIO_COOKIE_NAME': '2',
		'MVID_2_exp_in_1': '1',
		'MVID_ABC_TEST_WIDGET': '0',
		'MVID_AB_PROMO_DAILY': '1',
		'MVID_AB_SERVICES_DESCRIPTION': 'var2',
		'MVID_ADDRESS_COMMENT_AB_TEST': '2',
		'MVID_BLACK_FRIDAY_ENABLED': 'true',
		'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
		'MVID_CART_MULTI_DELETE': 'false',
		'MVID_CATALOG_STATE': '1',
		'MVID_CITY_ID': 'CityDE_30874',
		'MVID_FILTER_CODES': 'true',
		'MVID_FILTER_TOOLTIP': '1',
		'MVID_FLOCKTORY_ON': 'true',
		'MVID_GEOLOCATION_NEEDED': 'true',
		'MVID_GET_LOCATION_BY_DADATA': 'DaData',
		'MVID_GIFT_KIT': 'true',
		'MVID_IS_NEW_BR_WIDGET': 'true',
		'MVID_KLADR_ID': '5000004500000',
		'MVID_LAYOUT_TYPE': '1',
		'MVID_LP_SOLD_VARIANTS': '1',
		'MVID_NEW_ACCESSORY': 'true',
		'MVID_NEW_DESKTOP_FILTERS': 'true',
		'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
		'MVID_NEW_LK_OTP_TIMER': 'true',
		'MVID_NEW_MBONUS_BLOCK': 'true',
		'MVID_PROMO_CATALOG_ON': 'true',
		'MVID_REGION_ID': '1',
		'MVID_REGION_SHOP': 'S002',
		'MVID_SERVICES_MINI_BLOCK': 'var2',
		'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
		'MVID_TIMEZONE_OFFSET': '3',
		'MVID_WEBP_ENABLED': 'true',
		'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
		'PICKUP_SEAMLESS_AB_TEST': '2',
		'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
		'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
		'flacktory': 'no',
		'searchType2': '2',
		'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
		'BIGipServeratg-ps-prod_tcp80': '1208278026.20480.0000',
		'bIPs': '930512162',
		'BIGipServeratg-ps-prod_tcp80_clone': '1208278026.20480.0000',
		'wurfl_device_id': 'generic_web_browser',
		'MVID_GTM_BROWSER_THEME': '1',
		'deviceType': 'desktop',
		'MVID_CRM_ID': '0004996861',
		'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=',
		'ADRUM': 's=1654357391366&r=https%3A%2F%2Fwww.mvideo.ru%2F%3F0',
		'MVID_GUEST_ID': '20817507150',
		'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
		'__lhash_': 'ea4e80230881551bfa6c3fe778faddd5',
		'JSESSIONID': 'hGTNvBBM4nCznG3d7lmb25p3wcTTSB4p0ly175Tt12Fn9Xv4STDV!1827807850',
		'MVID_MCLICK': 'true',
		'MVID_MOBILE_FILTERS': 'true',
		'MVID_NEW_SUGGESTIONS': 'true',
		'MVID_SERVICES': '111',
		'MVID_ENVCLOUD': 'primary',
		'__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VhUhE7LVlrPEcbYEtjMBQzcl8UOQ1gfUQ8Lk1fEC9jD1lbFFZUfkldEnkJYVgvUV9gZQkhGjxtH2ZPWSZLWk1qJh8WfXMnVw8MXT9GbWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC9DaSVnTV0lRV1Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFtdzJEayVlSEsbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiNGWlR/Kx0WfXQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=pjz/dQ==',
		'__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VhUhE7LVlrPEcbYEtjMBQzcl8UOQ1gfUQ8Lk1fEC9jD1lbFFZUfkldEnkJYVgvUV9gZQkhGjxtH2ZPWSZLWk1qJh8WfXMnVw8MXT9GbWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC9DaSVnTV0lRV1Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFtdzJEayVlSEsbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiNGWlR/Kx0WfXQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=pjz/dQ==',
		'cfidsgib-w-mvideo': 'JWDmm+Awat9eht6ghN/71XQVGwOERqNduxSbnXqCwIKiajX6No0OUMTuWYrhoM+lM/gyrTdNQyD/Z67/4EItvmSBzYM3HHWlVqiFrsexPB+I6jXbJ3ck7f/dwcLMGKbZ3T80/5TMglSkPwcmtjHJTVBLpYkwW7KDst5Vb3U=',
		'cfidsgib-w-mvideo': 'JWDmm+Awat9eht6ghN/71XQVGwOERqNduxSbnXqCwIKiajX6No0OUMTuWYrhoM+lM/gyrTdNQyD/Z67/4EItvmSBzYM3HHWlVqiFrsexPB+I6jXbJ3ck7f/dwcLMGKbZ3T80/5TMglSkPwcmtjHJTVBLpYkwW7KDst5Vb3U=',
		'gsscgib-w-mvideo': 'a34Gdlrqxv1nj/P8zq1O9dbCvLCTcHKFASAR4a3Vgk0OFLtLuHI/ts7QxM0g3Qy3OVz/inY148WhlpOGMXGFJ2og0n3cPeXdEisDhKHXVVfA903AcrdAqELAYr2PKKjUtWKcE0v1PKvj8Dgf37h35ynB1r225XZv70y1mTNZ4qGgQKjCv+vX2HCSaxzUNSL9tQ8RnYx4WyODi4GXlZoPKw0/8KZP02Qxz16ZZyRon+BRsbV/y3PbNAJa1nl9qz8fHAeDurE=',
		'gsscgib-w-mvideo': 'a34Gdlrqxv1nj/P8zq1O9dbCvLCTcHKFASAR4a3Vgk0OFLtLuHI/ts7QxM0g3Qy3OVz/inY148WhlpOGMXGFJ2og0n3cPeXdEisDhKHXVVfA903AcrdAqELAYr2PKKjUtWKcE0v1PKvj8Dgf37h35ynB1r225XZv70y1mTNZ4qGgQKjCv+vX2HCSaxzUNSL9tQ8RnYx4WyODi4GXlZoPKw0/8KZP02Qxz16ZZyRon+BRsbV/y3PbNAJa1nl9qz8fHAeDurE=',
		'fgsscgib-w-mvideo': '0Sqkd19f37b3ea768b6a34ce025fd3a3ec06b901',
		'fgsscgib-w-mvideo': '0Sqkd19f37b3ea768b6a34ce025fd3a3ec06b901',
		'cfidsgib-w-mvideo': 'FrJ4i53XmmJ0eDwd4JUASM6jr63UhIS9g0R48ANBokTTvDOTq3FKaqOSrAXGFtwvib0nG0JgzA3DMFx00q9KjNyIB1+BumEfzQGyYjLJJ2OB8gxIzQ18waRfI26IHWxE8sP6aBSgDs0qQgvzOOWv2n1tsI7dWCHkKhq8Sb4=',
		'CACHE_INDICATOR': 'false',
		'mindboxDeviceUUID': '519db783-4ddc-4b5b-976d-40253f5986fb',
		'directCrm-session': '%7B%22deviceGuid%22%3A%22519db783-4ddc-4b5b-976d-40253f5986fb%22%7D',
		'ADRUM_BT': 'R:78|g:f9ffb5d6-5376-4ac4-af27-4ee136d876841119212',
	}

	headers = {
		'authority': 'www.mvideo.ru',
		'accept': 'application/json',
		'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
		# Requests sorts cookies= alphabetically
		# 'cookie': 'COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=2; MVID_2_exp_in_1=1; MVID_ABC_TEST_WIDGET=0; MVID_AB_PROMO_DAILY=1; MVID_AB_SERVICES_DESCRIPTION=var2; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_CART_MULTI_DELETE=false; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityDE_30874; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=5000004500000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=1; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=2; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; BIGipServeratg-ps-prod_tcp80=1208278026.20480.0000; bIPs=930512162; BIGipServeratg-ps-prod_tcp80_clone=1208278026.20480.0000; wurfl_device_id=generic_web_browser; MVID_GTM_BROWSER_THEME=1; deviceType=desktop; MVID_CRM_ID=0004996861; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOmZhbHNlLCJjb21wYXJpc29uIjpmYWxzZX0=; ADRUM=s=1654357391366&r=https%3A%2F%2Fwww.mvideo.ru%2F%3F0; MVID_GUEST_ID=20817507150; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; __lhash_=ea4e80230881551bfa6c3fe778faddd5; JSESSIONID=hGTNvBBM4nCznG3d7lmb25p3wcTTSB4p0ly175Tt12Fn9Xv4STDV!1827807850; MVID_MCLICK=true; MVID_MOBILE_FILTERS=true; MVID_NEW_SUGGESTIONS=true; MVID_SERVICES=111; MVID_ENVCLOUD=primary; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VhUhE7LVlrPEcbYEtjMBQzcl8UOQ1gfUQ8Lk1fEC9jD1lbFFZUfkldEnkJYVgvUV9gZQkhGjxtH2ZPWSZLWk1qJh8WfXMnVw8MXT9GbWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC9DaSVnTV0lRV1Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFtdzJEayVlSEsbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiNGWlR/Kx0WfXQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=pjz/dQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VhUhE7LVlrPEcbYEtjMBQzcl8UOQ1gfUQ8Lk1fEC9jD1lbFFZUfkldEnkJYVgvUV9gZQkhGjxtH2ZPWSZLWk1qJh8WfXMnVw8MXT9GbWUlLS1SKRIaYg9HV0VnXkZzXWcQREBNR0JzeC9DaSVnTV0lRV1Ja2xSVTd+YhZCRBgvSzk9bnBhDysYIVQ1Xz9BYUpKPTdYH0t1MDkzJCpFWnw2fXZ9NGt5PwtwC1cwL2gMcRVNPUFtdzJEayVlSEsbNR0KQ2hSVENdLRtJUBg5Mzk0ZnBXJ2BNXiNGWlR/Kx0WfXQfQU5EJ3VUNDpkdCIPaRMjZHhRP0VuWUZpdRUXQzwcew0qQ20tOmo=pjz/dQ==; cfidsgib-w-mvideo=JWDmm+Awat9eht6ghN/71XQVGwOERqNduxSbnXqCwIKiajX6No0OUMTuWYrhoM+lM/gyrTdNQyD/Z67/4EItvmSBzYM3HHWlVqiFrsexPB+I6jXbJ3ck7f/dwcLMGKbZ3T80/5TMglSkPwcmtjHJTVBLpYkwW7KDst5Vb3U=; cfidsgib-w-mvideo=JWDmm+Awat9eht6ghN/71XQVGwOERqNduxSbnXqCwIKiajX6No0OUMTuWYrhoM+lM/gyrTdNQyD/Z67/4EItvmSBzYM3HHWlVqiFrsexPB+I6jXbJ3ck7f/dwcLMGKbZ3T80/5TMglSkPwcmtjHJTVBLpYkwW7KDst5Vb3U=; gsscgib-w-mvideo=a34Gdlrqxv1nj/P8zq1O9dbCvLCTcHKFASAR4a3Vgk0OFLtLuHI/ts7QxM0g3Qy3OVz/inY148WhlpOGMXGFJ2og0n3cPeXdEisDhKHXVVfA903AcrdAqELAYr2PKKjUtWKcE0v1PKvj8Dgf37h35ynB1r225XZv70y1mTNZ4qGgQKjCv+vX2HCSaxzUNSL9tQ8RnYx4WyODi4GXlZoPKw0/8KZP02Qxz16ZZyRon+BRsbV/y3PbNAJa1nl9qz8fHAeDurE=; gsscgib-w-mvideo=a34Gdlrqxv1nj/P8zq1O9dbCvLCTcHKFASAR4a3Vgk0OFLtLuHI/ts7QxM0g3Qy3OVz/inY148WhlpOGMXGFJ2og0n3cPeXdEisDhKHXVVfA903AcrdAqELAYr2PKKjUtWKcE0v1PKvj8Dgf37h35ynB1r225XZv70y1mTNZ4qGgQKjCv+vX2HCSaxzUNSL9tQ8RnYx4WyODi4GXlZoPKw0/8KZP02Qxz16ZZyRon+BRsbV/y3PbNAJa1nl9qz8fHAeDurE=; fgsscgib-w-mvideo=0Sqkd19f37b3ea768b6a34ce025fd3a3ec06b901; fgsscgib-w-mvideo=0Sqkd19f37b3ea768b6a34ce025fd3a3ec06b901; cfidsgib-w-mvideo=FrJ4i53XmmJ0eDwd4JUASM6jr63UhIS9g0R48ANBokTTvDOTq3FKaqOSrAXGFtwvib0nG0JgzA3DMFx00q9KjNyIB1+BumEfzQGyYjLJJ2OB8gxIzQ18waRfI26IHWxE8sP6aBSgDs0qQgvzOOWv2n1tsI7dWCHkKhq8Sb4=; CACHE_INDICATOR=false; mindboxDeviceUUID=519db783-4ddc-4b5b-976d-40253f5986fb; directCrm-session=%7B%22deviceGuid%22%3A%22519db783-4ddc-4b5b-976d-40253f5986fb%22%7D; ADRUM_BT=R:78|g:f9ffb5d6-5376-4ac4-af27-4ee136d876841119212',
		'dnt': '1',
		'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/planshety-195/f/skidka=da',
		'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
		'x-set-application-id': '9df3f6b2-7703-47ab-89f1-49ddf71dcb40',
	}

	params = {
		'categoryId': '195',
		'offset': '0',
		'limit': '24',
		'filterParams': [
			'WyJza2lka2EiLCIiLCJkYSJd',
			'WyJ0b2xrby12LW5hbGljaGlpIiwiLTEyIiwiZGEiXQ==',
		],
		'doTranslit': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/listing',params=params, cookies=cookies, headers=headers).json()
	# print(response)
	products_ids = response.get('body').get('products')

	with open('1_products_ids.json', 'w') as file:
		json.dump(products_ids, file, indent=4, ensure_ascii=False)

	json_data = {
		'productIds': products_ids,
		'mediaTypes': [
			'images',
		],
		'category': True,
		'status': True,
		'brand': True,
		'propertyTypes': [
			'KEY',
		],
		'propertiesConfig': {
			'propertiesPortionSize': 5,
		},
		'multioffer': False,
	}

	response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()

	with open('2_items.json', 'w') as file:
		json.dump(response, file, indent=4, ensure_ascii=False)

	# print(len(response.get('body').get('products')))

	products_ids_str = ','.join(products_ids)

	params = {
		'productIds': products_ids_str,
		'addBonusRubles': 'true',
		'isPromoApplied': 'true',
	}

	response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()

	with open('3_prices.json', 'w') as file:
		json.dump(response, file, indent=4, ensure_ascii=False)

	item_prices = {}

	material_prices = response.get('body').get('materialPrices')

	for item in material_prices:
		item_id = item.get('price').get('productId')
		item_base_price = item.get('price').get('basePrice')
		item_sale_price = item.get('price').get('salePrice')
		item_bonus = item.get('bonusRubles').get('total')

		item_prices[item_id] = {
			'item_basePrice': item_base_price,
			'item_salePrice': item_sale_price,
			'item_bonus': item_bonus

	}

	with open('4_items_prices.json', 'w') as file:
		json.dump(item_prices, file, indent=4, ensure_ascii=False)


def get_result():


def main():
	get_data()


if __name__ == "__main__":
	main()