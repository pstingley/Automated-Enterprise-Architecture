
echo Scrubbing the data

@echo off
c:\Python27\ArcGIS10.4\Python.exe ./DataScrubber_2_7_2020.py
@echo off
echo  

echo Sorting the data
@echo off
c:\Python27\ArcGIS10.4\Python.exe ./Sortlines.py
@echo off
echo  

echo Counting the software packages
@echo off
c:\Python27\ArcGIS10.4\Python.exe ./Counter.py
@echo off
echo  

echo Aligning packages with the FEAF
@echo off
c:\Python27\ArcGIS10.4\Python.exe ./Match_With_FEAF_3_26_2020.py
@echo off
echo  