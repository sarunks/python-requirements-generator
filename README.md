python-requirements-generator
=============================

Scans all files recursively in a directory and prints all imports that are needed, that are not installed

Download the file
Run python python_requirements_generator.py <FULL FOLDER PATH>
Note: Absolute path wont work
Example python python_requirements_generator.py /home/johndoe/myapplicationcode

Sample Output

2014-12-02::16:06:08 GENERATING REQUIREMENTS
2014-12-02::16:06:08 REQUIREMENTS :
					ast
					datetime
					flask
					glob
					importlib
					json
					logging
					mandrill
					os
					passlib
					prettytable
					pudb
					pymongo
					pytz
					random
					requests
					string
					sys
					time
					validate_email
					xml
					
2014-12-02::16:07:02 CHECKING WHETHER REQUIREMENTS ARE ALREADY INSTALLED
2014-12-02::16:07:02 REQUIREMENTS TO BE INSTALLED :
							prettytable
