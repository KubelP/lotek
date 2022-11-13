Second version of lottery app.<br>
Many of people loves lottery games. Lottek is in Poland lottery game. You pick 6 numbers in range 1-49 with hope to draw this number on day of lottery. 

This app simulates on which draw you win main prize in lottery (match six numbers). 
For run python 3 interpreter is required.

There is no need for installation. Just copy files from repository and run in console by:

for linux: python3 main.py <br>
or <br>
for win: python main.py 

Required libraries:
- random
- time <br>
Both are standard python libraries. 

For tests in test_lotek.py it is necessary to install pytest:
pip install pytest

Enter your six numbers and wait for result. <br>
It returns on which draws you win your millions, total cost, teoreticaly number of years and time of running of script.

Default is set to pick 6 numbers in range 1-49, cost of one "lottery cupon" is 3 and there are 3 drawings in week. All of this values may be changed in main.py file.
