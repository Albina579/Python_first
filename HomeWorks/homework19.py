# Найти адрес электронной почты

import re

email_s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
reg = r"\w*[._-]?\d*[._-]?\d*\w*[._-]?\w*@\d*[._-]?\d*\w*[._-]?\w*\.ru"
print(re.findall(reg, email_s))
