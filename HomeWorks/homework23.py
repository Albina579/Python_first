# вывести на экран информацию о директории: имя - тип - размер (для файлов)

import os

for root, dirs, files in os.walk("../test"):
    for d in dirs:
        print(f"{d} - папка")
    for f in files:
        print(f"{f} - файл, {os.path.getsize( os.path.join( root, f ) )} байт")
