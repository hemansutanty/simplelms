from orm_choices import choices

@choices
class UserGender:
	class Meta:
		UNKNOWN = [0,"Unknown"]
		MALE = [1,"Male"]
		FEMALE = [2,"Female"]
