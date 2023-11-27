from typing import Self, Dict, List, Any
from eljur.student import Student

class Rules(object):
	def __init__(self: Self, data: Dict[str, Any]) -> None:
		self.roles: List[str] = data['roles']
		self.students: List[Student] = []
		for _, value in data['relations']['students'].items():
			student: Student = Student(value)
			self.students.append(student)
		self.schools: List[Any] = [] # in dev
		self.allowed_ads: List[str] = data['allowedAds']
		self.allowed_sections: List[str] = data['allowedSections']
		self.message_signature: str = data['messageSignature']
		self.upload_file_url: str = data['uploadFileUrl']
		self.support_phone: str = data['supportPhone']
		self.support_email: str = data['supportEmail']
		self.support_helpdesk: str = data['supportHelpdesk']
		self.support_description: str = data['supportDescription']
		self.name: str = data['name']
		self.age: int = data['age']
		self.id_: int = int(data['id'])
		self.vuid: str = data['vuid']
		self.id_hash: str = data['id_hash']
		self.title: str = data['title']
		self.vendor: str = data['vendor']
		self.vendor_id: int = data['vendor_id']
		self.guid: str = data['guid']
		self.last_name: str = data['lastname']
		self.first_name: str = data['firstname']
		self.middle_name: str = data['middlename']
		self.gender: str = data['gender']
		self.email: str = data['email']
		self.email_confirmed: bool = data['email_confirmed']
		self.region: str = data['region']
		self.region_code: int = int(data['regionCode'])
		self.city: str = data['city']
		self.rt_licey_school_end_date: bool = data['rt_licey_school_end_date']
