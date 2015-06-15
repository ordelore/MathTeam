#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  inputMath.py
#  
#  Copyright 2015 Lorenzo Orders <ordelore@gmail.com>
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
save_file = {}
save_data = save_file
def chk(directory):
	if not(os.path.exists(directory)):
		os.makedirs(directory)
def write(direct):
	intFileNumber = 0
	strCurPath = os.getcwd()
	os.chdir(direct)
	while os.path.isfile(str(intFileNumber) + ".txt"):
		intFileNumber += 1
	save_file = open(str(intFileNumber)+".txt", "wb")
	pickle.dump(save_data,save_file)
	save_file.close()
	os.chdir(strCurPath)
def main():
	from sys import platform as _platform
	intFileNumber = 0
	chrAnswer = "y"
	save_data = {}
	chk("fresh")
	chk("freshsoph2")
	chk("freshsoph8")
	chk("soph")
	chk("junior")
	chk("senior")
	chk("junsen2")
	chk("junsen8")
	chk("calculate")
	chk("oral")
	while chrAnswer != "n":
		print("\nWhen you input your values, they must be in between quotes.")
		Topic = input("\nTopic of question. eg: Number Theory, Number Bases, etc. (One word, please): ").lower()
		Problem = input("\nWhat is the question?: ")
		Answer = input("\nAnswer to problem: ")
		Team = input("\nTeam level.\nPossible options: Freshman, Sophmore, Junior, Senior, FreshSoph2Person, JunSen2Person, FreshSoph8Person, JunSen8Person, Calculator, Orals: ").lower()
		Picture = input("\nName of picture file (if applicable). If no picture needed, press Enter: ")
		save_data = {'Topic':Topic, 'Problem':Problem, 'Answer':Answer, 'PicturePath':Picture}
		if Team == "freshman":
			write("fresh")
		if Team == "sophmore":
			write("soph")
		if Team == "junior":
			write("junior")
		if Team == "senior":
			write("senior")
		if Team == "orals":
			write("oral")
		if Team == "calculator":
			write("calculate")
		if Team == "freshsoph2":
			write("freshsoph2")
		if Team == "freshsoph8":
			write("freshsoph8")
		if Team == "junsen2":
			write("junsen2")
		chrAnswer = input("\nEnter another problem? [y/n]")
	return 0
if __name__ == '__main__':
	main()
