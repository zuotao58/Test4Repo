#!/usr/bin/python

# Filename : allinone.py
# ============================================================================
#  Object: SWO int tool
# ============================================================================
#   Date          Author            Modification
#  2017-04-05	  JW	            Creation
# ============================================================================
# Main use:
# Read file and fetch info.
# ============================================================================

import os
import re
import sys

def get_apk_list(CFG_FILE='./int/common/allinone_table.txt'):
	if os.path.exists(CFG_FILE):
		app_list = open(CFG_FILE,'r').read().split('\n')
		#print app_list
	else:
		app_list = []
	return app_list

def get_apk_info5(sub_apk_list,sub_modulename,sub_branchname):
	for apps in sub_apk_list:
		if not apps.startswith('#'):
			match = re.match('([\w]+[.]+[\w]+[.]+[\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)', apps)
			if match:
				vol1 = match.group(1)
				vol2 = match.group(2)
				vol3 = match.group(3)
				vol4 = match.group(4)
				vol5 = match.group(5)
				if (vol3 == sub_modulename) and (vol1 == sub_branchname) :
					sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5
					print sub_apk_info
					return sub_apk_info

def get_apk_info6(sub_apk_list,sub_modulename):
	for apps in sub_apk_list:
		if not apps.startswith('#'):
	#		print app
			match = re.match('([\w]+)\s+([\w]+[.][\w])\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)', apps)
			if match:
				vol1 = match.group(1)
				vol2 = match.group(2)
				vol3 = match.group(3)
				vol4 = match.group(4)
				vol5 = match.group(5)
				vol6 = match.group(6)
				if vol1 == sub_modulename:
					sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5+' '+vol6
					#print sub_apk_info
					return sub_apk_info
			else:
				match = re.match('([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)', apps)
				if match:
					vol1 = match.group(1)
					vol2 = match.group(2)
					vol3 = match.group(3)
					vol4 = match.group(4)
					vol5 = match.group(5)
					vol6 = match.group(6)
					if vol1 == sub_modulename:
						sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5+' '+vol6
						#print sub_apk_info
						return sub_apk_info

def get_apk_info7(sub_apk_list,sub_modulename):
	for apps in sub_apk_list:
		if not apps.startswith('#'):
	#		print app
			match = re.match('([\w]+)\s+([\w]+[.][\w])\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)', apps)
			if match:
				vol1 = match.group(1)
				vol2 = match.group(2)
				vol3 = match.group(3)
				vol4 = match.group(4)
				vol5 = match.group(5)
				vol6 = match.group(6)
				vol7 = match.group(7)
				if vol1 == sub_modulename:
					sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5+' '+vol6+' '+vol7
					#print sub_apk_info
					return sub_apk_info
			else:
				match = re.match('([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)', apps)
				if match:
					vol1 = match.group(1)
					vol2 = match.group(2)
					vol3 = match.group(3)
					vol4 = match.group(4)
					vol5 = match.group(5)
					vol6 = match.group(6)
					vol7 = match.group(7)
					if vol1 == sub_modulename:
						sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5+' '+vol6+' '+vol7
						#print sub_apk_info
						return sub_apk_info

def get_apk_info10(sub_apk_list,module_name):
	for apps in sub_apk_list:
		if not apps.startswith('#'):
	#		print app
			match = re.match('([\w]+)\s+([\w]+[.][\w])\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w//]+)\s+([\w//]+)\s+([\w//]+)', apps)
			if match:
				vol1 = match.group(1)
				vol2 = match.group(2)
				vol3 = match.group(3)
				vol4 = match.group(4)
				vol5 = match.group(5)
				vol6 = match.group(6)
				vol7 = match.group(7)
				vol8 = match.group(8)
				vol9 = match.group(9)
				vol10 = match.group(10)				
				if vol3 == module_name:
					sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5+' '+vol6+' '+vol7+' '+vol8+' '+vol9+' '+vol10
					#print sub_apk_info
					return sub_apk_info
			else:
				match = re.match('([\w]+[.]+[\w]+[.]+[\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w]+)\s+([\w//]+)\s+([\w//]+)\s+([\w//]+)', apps)
				if match:
					vol1 = match.group(1)
					vol2 = match.group(2)
					vol3 = match.group(3)
					vol4 = match.group(4)
					vol5 = match.group(5)
					vol6 = match.group(6)
					vol7 = match.group(7)
					vol8 = match.group(8)
					vol9 = match.group(9)
					vol10 = match.group(10)	
					if vol3 == module_name :
						sub_apk_info=vol1+' '+vol2+' '+vol3+' '+vol4+' '+vol5+' '+vol6+' '+vol7+' '+vol8+' '+vol9+' '+vol10
						#print sub_apk_info
						return sub_apk_info

if __name__ == "__main__":
	

        if sys.argv[1]=='table6vol':
		apk_list = get_apk_list('./int/common/allinone_table.txt')
		apk_info=get_apk_info6(apk_list,sys.argv[2])
		print apk_info
        elif sys.argv[1]=='table7vol':
		apk_list = get_apk_list('./int/common/allinone_table.txt')
		apk_info=get_apk_info7(apk_list,sys.argv[2])
		print apk_info
        elif sys.argv[1]=='table10vol':
		apk_list = get_apk_list('./int/common/allinone_table.txt')
		apk_info=get_apk_info10(apk_list,sys.argv[2])
		print apk_info
        elif sys.argv[1]=='table5vol':
                apk_list = get_apk_list('./int/common/allinone_table.txt')
                apk_info=get_apk_info5(apk_list,sys.argv[2],sys.argv[3])
	else:
		print "Error:Please select correct table."
		sys.exit(1)
