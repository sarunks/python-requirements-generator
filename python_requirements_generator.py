import glob
import os
import time
import sys

def ts_print(msg):
	print time.strftime("%Y-%m-%d::%H:%M:%S"), msg

def get_requirements_in_file(file_name):
	requirements = []
	f_open = open(file_name, "r")
	line = f_open.readline()
	while (line):
		for sub_line in line.split(";"):
			if "'" not in sub_line and '"' not in sub_line:
				if "from " in sub_line:
					requirements.append(sub_line.split("from ")[1].split(" ")[0].strip().split(".")[0])
				elif "import " in sub_line:
					for x in (sub_line.split("import ", 1)[1]).split(","):
						requirements.append(x.strip().split(".")[0])
		line = f_open.readline()
	f_open.close()
	return requirements

def get_all_files_recursive(file_path):
	py_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(file_path)  for f in filenames if os.path.splitext(f)[1] == '.py' ]
	return py_files

def get_all_requirements(file_path):
	ts_print("GENERATING REQUIREMENTS")
	requirements = []
	directories = ["app"]
	py_files = get_all_files_recursive(file_path)
	for x in py_files:
		requirements.extend(get_requirements_in_file(x))
		if len(x.split("/")) >= 3:
			directories.extend(x.split("/")[1:(len(x.split("/"))-1)])
	requirements_final = sorted(list(set(requirements) - set(directories)))
	ts_print("REQUIREMENTS :\n\t\t\t\t\t%s\n" % "\n\t\t\t\t\t".join(requirements_final))
	ts_print("CHECKING WHETHER REQUIREMENTS ARE ALREADY INSTALLED")
	not_installed_requirements = []
	for x in requirements_final:
		try:
			__import__(x)
		except Exception, e:
			not_installed_requirements.append(x)
	if not_installed_requirements:
		ts_print("REQUIREMENTS TO BE INSTALLED :\n\t\t\t\t\t\t\t%s\n" % "\n\t\t\t\t\t\t\t".join(not_installed_requirements))
	else:
		ts_print("ALL REQUIREMENTS PRESENT")

if __name__ == "__main__":
	if len(sys.argv) <= 1:
		ts_print("SPECIFY FULL PATH OF FOLDER, Example /home/username/mappcode")
		exit()
	get_all_requirements(sys.argv[1])

