This test has been provided for you so that you can see one example, however, you should be creating your own tests to check that your code runs as expected.

I perfomed two  tests  to generate both the medianvals_by_zip.txt and medianvals_by_date.txt  files. In this  test i used 
two input files 
1. small_input.txt that has 10-15 rows 
2. itcont_2016_20161214_92060702.txt ( from the 2015-2016  dataset) 

cat itcont_2016_20161214_92060702.txt |python  insight_mapper_zip.py | python insight_reducer_zip.py >> medianvals_by_zip.txt
cat itcont_2016_20161214_92060702.txt |python  insight_mapper_date.py | python insight_reducer_date.py >> medianvals_by_date.txt
 
cat small_input.txt |python  insight_mapper_zip.py | python insight_reducer_zip.py >> medianvals_by_zip.txt
cat small_input.txt |python  insight_mapper_date.py | python insight_reducer_date.py >> medianvals_by_date.txt
