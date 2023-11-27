from typing import Self, Optional, Dict, Any
from requests import get, Session
from requests.models import Response
from eljur.utils import *
from eljur.rules import Rules

class Eljur(object):
	def __init__(self: Self, vendor: str, login: Optional[str] = None, password: Optional[str] = None, token: Optional[str] = None, devkey: str = '9235e26e80ac2c509c48fe62db23642c', domain: str = 'https://api.eljur.ru/api') -> None:
		headers: Dict[str, str] = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
			'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
			'Content-Type': 'application/json'
		}

		data: Dict[str, str] = {
			'devkey': devkey,
			'vendor': vendor,
			'login': login,
			'password': password,
			'out_format': 'json'
		}

		if (login is None and password is None) and token is None:
			raise ValueError('Arguments did not passed')

		self.devkey: str = devkey
		self.vendor: str = vendor

		self.session: Session = Session(base_url=f'{domain}/')
		self.session.headers = headers

		if token is not None:
			self.token: str = token
			return

		response: Response = get(f'{domain}/auth', headers=headers, json=data)

		if response.status_code != 200 or response.json()['response']['error'] is not None:
			raise ValueError('Arguments are not valid')

		self.token: str = response.json()['response']['result']['token']

	def call(self: Self, method: str, data: Dict[str, str] = {}) -> Optional[Dict[str, Any]]:
		data.update({
			'devkey': self.devkey,
			'vendor': self.vendor,
			'auth_token': self.token,
			'out_format': 'json'
		})

		response: Response = self.session.get(method, json=data)

		if response.status_code != 200 or response.json()['response']['error'] is not None:
			return None

		return self.session.get(method, json=data).json()['response']['result']

	def get_rules(self: Self) -> Optional[Dict[str, Any]]:
		rules: Dict[str, Any] = self.call('getrules')
		return Rules(rules)
