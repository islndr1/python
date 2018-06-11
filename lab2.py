alphabet = 'abcdefghijklmnopqrstuvwxyz,.!?;:_- ABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'  
	                    
menu = True         
while menu :    
	print("Меню: ")  
	print("1: Шифровать")  
	print("2: Раскодировать")  
	print("3: Выход")  
	pick = int(input("Ваш выбор: "))  
	if pick == 1 :  
		str = input("Введите строку: ")  
		slip = int(input("Введите смещение: "))  
		result = ""  
		for i in str:  
			result += alphabet[(alphabet.find(i) + slip) % len(alphabet)]  
		print(result)             
	if pick == 2 :  
		str = input("Введите строку: ")  
		for i in range(len(alphabet)):  
			result = ""  
			for j in str :  
				result += alphabet[(alphabet.find(j) + i) % len(alphabet)]  
			print(i, result)                  
	if pick == 3:  
		menu = False  


