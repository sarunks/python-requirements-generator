python-requirements-generator
=============================

Scans all files recursively in a directory and prints all imports that are needed, that are not installed

Download the file<br />
RUN python python_requirements_generator.py \<FULL FOLDER PATH\><br />
Note: Absolute path wont work<br />
EXAMPLE: python python_requirements_generator.py /home/johndoe/myapplicationcode<br />
Works with python 2.6,2.7,3.0

Sample Output

2014-12-02::16:06:08 GENERATING REQUIREMENTS<br />
2014-12-02::16:06:08 REQUIREMENTS :<br />
					ast<br />
					datetime<br />
					flask<br />
					glob<br />
					importlib<br />
					json<br />
					logging<br />
					mandrill<br />
					os<br />
					passlib<br />
					prettytable<br />
					pudb<br />
					pymongo<br />
					pytz<br />
					random<br />
					requests<br />
					string<br />
					sys<br />
					time<br />
					validate_email<br />
					xml<br />
					<br />
2014-12-02::16:07:02 CHECKING WHETHER REQUIREMENTS ARE ALREADY INSTALLED<br />
2014-12-02::16:07:02 REQUIREMENTS TO BE INSTALLED :<br />
							prettytable<br />
