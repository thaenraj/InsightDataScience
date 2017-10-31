#! /usr/bin/env python 

import sys 
import math 
import csv 
import datetime
from itertools import groupby
from operator import itemgetter

current_key = None	
current_zip = None

''' median function along with round functionality to process the list of values ''' 
''' define class called reducer_process that has iterator to iterate the mapper output rows ( cmteid, zipcode, transactionamt) in the stream (stdin) and yield a row using the generator yield '''
''' make_reducer method is used to  group the streamed data against the cmteid,zipcode column values and find the total, median values for the grouped values  using the python itemgetter and groupby functionality '''

def find_median(list): 
	sorted_list = sorted (list) 
	''' since middle is the list index it should be int value '''
	middle  = len(sorted_list) // 2 
	if len(sorted_list) % 2  == 0 : 
		median = round(sum(sorted_list [middle -1 : middle + 1] ) /2.0,0) 
	else : 
		 median  = round(sorted_list [middle],0 )
	'''print ('inside the find_median')'''
	return median 


class reducer_process (object) :
		def __init__(self,stream):
			self.stream = stream 
			self.current_key  = None 
			self.current_zip  = None 
		def make_output (self,key,zipcode,amt_list) :
			'''print ('\n output' + cmteid,zipcode,transactionamount)'''
			total = len(amt_list)
			total_amount =   sum(amt_list)
			median =  find_median(amt_list) 
			sys.stdout.write("{0}|{1}|{2}|{3}|{4}\n".format(str(key), str(zipcode), str(median), str(total),str(total_amount)))    
		def make_reducer (self) :
			amt_list = [] 
			grouper = itemgetter(0, 1) 
			''' group by keys and sort the grouped items '''
			for key_values, group in groupby(sorted(self),grouper):				
				for item in group:      
						''' new entry ''' 
						key =  item[0]
						zipcode =  item[1]
						transactionamt  = item[2]
						if ( key != self.current_key ) :
								'''print ('new key are ' + key,zipcode,key_values[0],key_values[1]) '''
								'''print (key,zipcode,transactionamt) '''
								amt_list.append(float(item[2]))                
								self.make_output(key, zipcode,amt_list) 
						else :
								self.current_key = key 
								self.current_zip = zipcode
		
				self.current_key = None	
				self.current_zip = None
				amt_list  = [] 

		def __iter__(self) : 
				for line in self.stream:  
					sp = line[:-1].split("|")
					key = sp[0]
					zipcode = sp[1]
					transactionamt = sp[2]
					yield key, zipcode , float(transactionamt)  	
					

if __name__ == '__main__':    
	insightreducer = reducer_process(sys.stdin)
	insightreducer.make_reducer()		
				

