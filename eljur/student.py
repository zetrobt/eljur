from typing import Self, Dict, List, Any

class Student(object):
	def __init__(self: Self, data: Dict[str, Any]) -> None:
		self.rules: List[str] = data['rules']
		self.rel: str = data['rel']
		self.name: str = data['name']
		self.title: str = data['title']
		self.last_name: str = data['lastname']
		self.first_name: str = data['firstname']
		self.gender: str = data['gender']
		self.class_: int = data['class']
		self.parallel: int = data['parallel']
		self.city: str = data['city']
