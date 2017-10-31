#! /usr/bin/env python 

import sys 
import math 
import csv 
import datetime 

 
''' define class called mapper_process that iterator to iterate the rows in the stream (stdin) and yield a row using the generator yield '''
''' make_mapper method is used to output the mapper key value pair ( cmteid is the key, zipcode and transaction amt are its tied  values ) '''
''' define all input validation functions '''

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

''' define the class that has the member  'stream' (sys.stdin)  '''
class mapper_process (object) : 
		def __init__(self,stream):
			self.stream = stream 
		def make_output (self,cmteid,zipcode,transactionamount) :
			'''print ('\n output' + cmteid,zipcode,transactionamount)'''
			sys.stdout.write("{0}|{1}|{2}\n".format(cmteid,zipcode[0:5],transactionamount))    
		def make_mapper (self) :
			for line in self : 
				cmteid = line[0]
				'''print (cmteid)'''
				'''check the input file data ''' 	
				''' 1: other_id  should be null
					 2: transationdt  ( malformed , empty  ...) is ok for zip code file preparation but ignore the
						 same for the transaction_date  	preparation
					 3: invalid zipcode (malformed , empty  ... , less than 5 characters )  ignored for zipcode file but considered for date file 
					 4: cmte_id or transaction_dt should not be empty for both zip and date file preparation '''
				''' key ''' 
				''' rest of them are values ''' 
				'''data = [x for x in sp[1].split('|')]'''
				zipcode    =   line [10] 
				'''print ('the zipcode is '  + line [10]) '''
				transactiondate = line [13] 
				'''print ('the transactiondate is '  + line [13]) '''
				transactionamount = line[14] 
				''' print ('the transactionamount is '  + line [14]) '''
				otherid = line [15] 
				''' print ('the otherid is '  + line [15]) '''
				''' validate the input considerations rule ''' 
				if ( validate_other_id(otherid) and validate_cmteid(cmteid)  and 	validate_zip(zipcode)  and  validate_trans_amt(transactionamount) )	:				 
					'''print (cmteid,zipcode,transactiondate,transactionamount,otherid) '''
					'''make value as list of cloumn and map it for each key ''' 
					self.make_output(cmteid, zipcode,transactionamount) 	
					'''todolist''' 
					''' add invalid records - respective counters''' 
			
		def __iter__(self) : 
				stream_handle  = csv.reader (self.stream ,delimiter ='|') 
				for line  in stream_handle  : 
					'''print (line) 
					print (line[0],line[1])'''
					yield line
				

'''instantiate the mapper to process the stream from stdin '''

if __name__ == '__main__':    
	insightmapper = mapper_process(sys.stdin)
	insightmapper.make_mapper()		
				
			
			

