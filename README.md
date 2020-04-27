# MorseCode1

Project Description
As the project name says, this project is about building a simple Morse code decoder with Python. This project is created using PyCharm IDE using Anaconda. As per the project requirements, the activities are divided into four tasks –
Task 1 – 
	This task is about to create a data dictionary of Morse codes. For this, I have created an Excel file with keys & value in two columns. And then, I have pulled the data from the Excel file (Data.xlsx) into the dictionary in Python. 
  	 
Figure 1 Fetch dictionary data from Excel
Creating an Excel file helps to easily modify/insert/delete the Morse code dictionary without touching the program (especially useful for someone with no programming knowledge). After pulling the dictionary, I have just displayed the dictionary as it is in the Task 1 output.  	
Note: If input = “1010*1001” & Output = “CX” – In this document, we are considering “1010”, “1001”, “C” & “X” as each letter/character. Whereas “1010*1001” & “CX” as sequence.
Task 2 –
	Task 2 involves taking input from the user & verify input sequence is 0 &/or 1. User can input any character.  We’ll take as much input as user wants until user terminates. To terminate, user needs to just leave input blank & press Enter. I’m using While loop to keep asking for inputs until blank. And then in the end, print back the list of all user inputs.
	To validate if the user has entered among 0 & 1 separated by *, I created a function with name as “input_validation_function”. I’ve imported “re” library (start of program) to implement regular expression. First, store the regular expression format of 0 & 1 in a string. And then check whether the input codes are as per the regular expression or not (e.g.: check whether 10102 from sequence 10102*010 is 0 &/or 1). Then store the invalid sequences in another list which is used to remove same sequences from original user input sequence list. The rest of the valid sequences are then forwarded to decode.
Task 3 –
	I’ve created the dictionary in Task 1 & stored valid user input in a list in Task 2. Now lets decode the input to English using “decode_function” function. This function is used to translate Morse sequence to English. We simply check each character code from the user input with value from our dictionary. If they match, we can identify the English character by referring the value’s key in the dictionary. This way, we build the English sequence.
Task 4 –
	This task file simply helps to count the number of occurrence of each character the decoded output. Again here, I’ve created a function & called it for making the program efficient.

Sample Run
 
Figure 3 Sample output
	I’ve tried to run the program by combination of valid & invalid inputs. And so far looks good!

Run Manual
1.	The dictionary data is fetched from an Excel file which should be in the project folder. The Excel file contains first column as keys & second as values. I’ve used “xlrd” library for this feature.
2.	Directly run Task 4 in PyCharm; will eventually have all the task files run at once.
3.	re library is imported in Task2.py. This is imported to check user input is 0 &/or 0. If not, then those (we are handling “*” in separate way).
4.	If any character apart from 0, 1 & * is found in the input, the whole sequence is ignored. If it is 0/1, but the Morse code is incorrect, then we show “<Invalid letter>” for that character as shown in the last example in above sample output screenshot (“HAP<Invalid letter>Y”).
5.	In PyCharm, I had manually set the Python interpreter as Anaconda in “Settings>Project Interpreter”
 

Understanding Flaw
	We have used regular expression to check the characters are whether only 0/1. As per below screenshot, I’m checking “is True” in “if condition” (blue underlined in screenshot). But I think, I should use “is False” instead. However, by using “is False”, I wasn’t getting what I was expecting. Whereas, “is True” logic works.
 
Figure 4 Flow of re (regular expression)

References
•	Stackoverflow.com. Python Creating Dictionary from excel data. Referred from https://stackoverflow.com/questions/14196013/python-creating-dictionary-from-excel-data?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa (Accessed 23/03/2018)
•	SiHa (Last edited Oct 6 '16 at 7:11), CrazyCasta. Stackoverflow.com. Check if string matches pattern. Retrieved from https://stackoverflow.com/questions/12595051/check-if-string-matches-pattern/12595533?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
•	Python Reference Manual. Function definitions. Referred ‘how to return data from functions’ from https://docs.python.org/2.0/ref/function.html
•	Community♦ (Last edited May 23 '17 at 12:02), Stênio Elson. Stackoverflow.com. Get key by value in dictionary. Referred from https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
