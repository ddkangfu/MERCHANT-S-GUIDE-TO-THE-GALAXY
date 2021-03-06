#!/usr/local/bin/python
#coding=utf-8
import re

def Translate_To_Earth_Numerals(RomanStr):
	"""
		转义为阿拉伯数字模块

		将罗马数字转化为阿拉伯数字

		输入：
			罗马数字

		返回：
			阿拉伯数字

	"""

	if re.search('^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',RomanStr)!= None:
		NumDic = {"pattern":"","retNum":0}
		RomanPattern = {
			"0":('','','','M'),
			"1":('CM','CD','D','C',100),
			"2":('XC','XL','L','X',10),
			"3":('IX','IV','V','I',1)
		}
		i = 3
		NumItems = sorted(RomanPattern.items())
		for RomanItem in NumItems:
			if RomanItem[0] != '0':
				patstr = NumDic["pattern"].join(['',RomanItem[1][0]])
				if re.search(patstr,RomanStr) != None:
					NumDic["retNum"] += 9*RomanItem[1][4]
					NumDic["pattern"] = patstr
				else:
					patstr = NumDic["pattern"].join(['',RomanItem[1][1]])
					if re.search(patstr,RomanStr) != None:
						NumDic["retNum"] += 4*RomanItem[1][4]
						NumDic["pattern"] = patstr
					else:
						patstr = NumDic["pattern"].join(['',RomanItem[1][2]])
						if re.search(patstr,RomanStr) != None:
							NumDic["retNum"] += 5*RomanItem[1][4]
							NumDic["pattern"] = patstr
			if NumDic["pattern"] == '':
				NumDic["pattern"] = '^'
			tempstr = ''
			sum = 0
			for k in range(0,4):
				pstr = RomanItem[1][3].join(['','{']).join(['',str(k)]).join(['','}'])
				patstr = NumDic["pattern"].join(['',pstr])
				if re.search(patstr,RomanStr) != None:
					sum = k*(10**i)
					tempstr = patstr
			if tempstr !='':
				NumDic["pattern"] = tempstr
			else:
				NumDic["pattern"] = patstr
			NumDic['retNum'] += sum
			i -= 1
		return NumDic['retNum']
	else:
		print 'String is not a valid Roman numerals'




if __name__ == "__main__":

	a='MM'
	Translate_To_Earth_Numerals(a)
	
