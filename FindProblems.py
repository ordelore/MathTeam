#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  FindProblems.py
#  
#  Copyright 2015 ordelore <ordelore@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pickle, os
from random import randint
def read(direct, ByTopic):
	save_file = {}
	if not(os.path.exists(direct)):
		os.makedirs(direct)
	intFileNumber = 0
	strCurPath = os.getcwd()
	os.chdir(direct)
	while os.path.isfile(str(intFileNumber) + ".txt"):
		intFileNumber += 1
	intFile = 0
	if ByTopic == 'y':
		intNumber = 0
		while save_file['Topic'] != Topic:
			intFile = randint(0, intFileNumber - 1)
			intNumber += 1
			if intNumber >= intFileNumber:
				print("No topics available")
				return 0
	else:
		intFile = randint(0, intFileNumber - 1)
	save_file = pickle.load(open(str(intFile)+".txt", 'rb'))
	Answer = save_file['Problem']
	print(Answer)
	answer = ""
	while answer != save_file['Answer']:
		answer = input("Answer?: ")
		if answer != save_file['Answer']:
			print("Incorrect")
	print("Correct")
	os.chdir(strCurPath)
def main():
	NewProblem = 'y'
	ByTopic = 'n'
	while NewProblem != 'n':
		Team = input("What team level are you looking for? \nOptions: Freshman, Sophmore, Junior, Senior, FreshSoph2Person, JunSen2Person\nFreshSoph8Person, JunSen8Person, Calculator, Orals: ").lower()
		ByTopic = input("Would you like to search by topic? [y/n]: ")
		if ByTopic == 'y':
			Topic = input("All one word, and be warned that your topic may not yet be implemented.\nEg: 'Number Bases' turns into NumberBases: ").lower()
		if Team == "freshman":
			read("fresh", ByTopic)
		if Team == "sophmore":
			read("soph", ByTopic)
		if Team == "junior":
			read("junior", ByTopic)
		if Team == "senior":
			read("senior", ByTopic)
		if Team == "orals":
			read("oral", ByTopic)
		if Team == "calculator":
			read("calculate", ByTopic)
		if Team == "freshsoph2":
			read("freshsoph2", ByTopic)
		if Team == "freshsoph8":
			read("freshsoph8", ByTopic)
		if Team == "junsen2":
			read("junsen2", ByTopic)
		NewProblem = input("Would you like a new problem? [y/n]: ")
	return 0

if __name__ == '__main__':
	main()

