#! /usr/bin/env python 

import sys 
import math 
import csv 
import datetime
import os 
from itertools import groupby
from operator import itemgetter

'''  todolist''' 
''' keep the input validation functions as  helper class'''
''' handle try exception '''

def make_output (key, transactiondate,amt_list) :
	'''print ('\n output' + cmteid,transactiondate,transactionamount)'''
	total = len(amt_list)
	total_amount =   sum(amt_list)
	median =  find_median(amt_list) 
	return '|'.join([str(key), str(transactiondate), str(median), str(total),str(total_amount)])
	'''sys.stdout.write("{0}|{1}|{2}|{3}|{4}\n".format(str(key),str(transactiondate),str(median),str(total),str(total_amount))) '''
	

def write_output(outfilename,result):
	with open(outfilename, "w") as insight_handle:
		'''fieldnames = ['key', 'transactiondate'  ,'median' , 'total' , 'total_amount' ]'''
		writer = csv.writer(insight_handle)
		'''writer.writeheader()'''
		for value in result:
				print ('inside' )
				print (value )
				writer.writerow( [value])	
		
	

def find_median(list): 
	sorted_list = sorted (list) 
	print ('inside the median' )
	print (list)
	''' since middle is the list index it should be int value '''
	middle  = len(sorted_list) // 2 
	if len(sorted_list) % 2  == 0 : 
		median = round(sum(sorted_list [middle -1 : middle + 1] ) /2.0,0) 
	else : 
		 median  = round(sorted_list [middle],0 )
	'''print ('inside the find_median')'''
	return median 


def is_not_empty(teststring): 
	if teststring and teststring.strip():
		return True
	else :
		return False 

def validate_date (transactiondate)  : 
	if ( is_not_empty(transationdate)  and   len(transactiondate) == 8 and   datetime.datetime.strptime(date_text, '%m%d%Y')) : 
		return True 
	else :
		return  False 

def validate_zip(zipcode): 
	if   ( is_not_empty(zipcode) and  len(zipcode) >= 5 ): 
		return True
	else :
		return False 

def validate_cmteid(cmteid): 
	if   ( is_not_empty(cmteid) ): 
		return True
	else :
		return False 

def validate_trans_amt  (testamount)  : 
		if len(testamount) > 0 : 
			'''and  type(float(testamount))  == float:'''
			return True  
		else :	
			return False 

def validate_other_id  (testid)  : 
		if is_not_empty (testid):
			return True  
		else :	
			return False

def parse_file(filename):
	data = [] 
	with open (filename) as filehandle :
		print (filename)
		file_handle  = csv.reader (filehandle , delimiter = '|') 
		for line  in file_handle :
			if (len(line) != None):
					cmteid = line[0]
					print (cmteid)
					zipcode    =   line [10] 
					transactiondate = line [13] 
					transactionamount = line[14] 
					otherid = line [15] 
			if ( validate_other_id(otherid) and validate_cmteid(cmteid)  and validate_zip(zipcode)  and  validate_trans_amt(transactionamount) )	:
					 data.append([cmteid,transactiondate,transactionamount]) 
		print (data)			 
		return data 
	
			
def  process_file(data) :
				amt_list = [] 
 
				output  = [] 
				grouper = itemgetter(0, 1) 
				''' group by keys and sort the grouped items '''
				for key_values, group in groupby(sorted(data),grouper):		
					current_key  = None 
					current_date  = None		
					for item in group:  
						 
						print (item)     
						''' new entry ''' 
						key =  item[0]
						print (key) 
						transactiondate =  item[1]
						print (transactiondate)
						transactionamt  = item[2]
						print (transactionamt)
						if ( key != current_key and  transactiondate  !=  current_date) :
								if ( current_key == None ) :
									print ('new key are ' + key,transactiondate,key_values[0],key_values[1]) 
									'''print (key,transactiondate,transactionamt) '''
									amt_list.append(float(item[2]))                
									result = make_output(key, transactiondate,amt_list) 
									'''print (result)'''	
									output.append(result)
								current_key = key 
								current_date = transactiondate								

						else :
								current_key = key 
								current_date = transactiondate
								amt_list.append(float(item[2])) 
								result = make_output(key, transactiondate,amt_list)
								amy_list = []  
				current_key = None	
				current_date = None
				amt_list  = [] 
				return  output 				
				

if __name__ == '__main__':  
			sys.argv = ["insight_process_date.py"] 
			'''if  len(sys.argv) == 1 : 
			print ("Please provide the  input file path :") 
			else  : '''
			filepath = "/home/cloudera/insight/src/"  
			outfilename = "//home//cloudera//insight/src/smedianvals_by_date.txt"
			print (filepath) 
			path  = r"%s" % filepath 
			print  (path) 
			file = "small_input.txt" 
			'''for file in os.listdir(path) : '''
			filename  = os.path.join(path,file) 
			print (filename) 
			'''  process a file ''' 
			data  = parse_file(filename)
			result = process_file (data)
			print (result) 
			write_output(outfilename,result)


		
				
	
		 
			
