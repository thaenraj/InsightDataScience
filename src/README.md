This is the directory where your source code would reside.

I used  two sets of python programs (mapper , reducer) to generate these two output files 

Set 1 ) :: used to  generate insight_medianvals_by_date.txt  output file  
insight_mapper_date.py
insight_reducer_date.py

Set 2) :: used to  generate insight_medianvals_by_zip.txt  output file  
insight_mapper_zip.py
insight_reducer_zip.py

How to run 
cat itcont_2016_20161214_92060702.txt |python  insight_mapper_zip.py | python insight_reducer_zip.py >> medianvals_by_zip.txt
cat itcont_2016_20161214_92060702.txt |python  insight_mapper_date.py | python insight_reducer_date.py >> medianvals_by_date.txt
 
cat small_input.txt |python  insight_mapper_zip.py | python insight_reducer_zip.py >> medianvals_by_zip.txt
cat small_input.txt |python  insight_mapper_date.py | python insight_reducer_date.py >> medianvals_by_date.txt

(PS:: insight_process_date_nostream.py is inprogress source code,need to fix the issue in grouping the transactiondate ) 
