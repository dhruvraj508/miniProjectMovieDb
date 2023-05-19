import json
import time


def tsv2json(input_file,output_file):
	arr = []
	file = open(input_file, 'r', encoding="utf-8")
	a = file.readline()

	# The first line consist of headings of the record
	# so we will store it in an array and move to
	# next line in input_file.
	titles = [t.strip() for t in a.split('\t')]
	for line in file:
		d = {}
		for key, data in zip(titles, line.split('\t')):

			# Convert each row into dictionary with keys as titles
			if key in ["primaryProfession", "knownForTitles", "genres"]:
				inner_array = [f.strip() for f in data.split(",")]
				if inner_array not in [["\\N"],[""]]:
					d[key] = inner_array
				else:
					d[key] = None
			elif key == "characters":
				inner_array = [s.strip()[1:len(s)-1] for s in data[1:len(data)-2].split(",")]
				if inner_array != [""]:
					d[key] = inner_array
				else:
					d[key] = None
			else:
				if data.strip() == "\\N":
					d[key] = None
				else:
					if key in ["numVotes","birthYear","deathYear","isAdult","startYear","endYear","runtimeMinutes","ordering"]:
						d[key] = int(data.strip())
					elif key in ["averageRating"]:
						d[key] = float(data.strip())
					else:
						d[key] = data.strip()

		# we will use strip to remove '\n'.
		arr.append(d)

		# we will append all the individual dictionaires into list
		# and dump into file.
	with open(output_file, 'w', encoding='utf-8') as output_file:
		output_file.write(json.dumps(arr, indent=4))


def main():
	# Create the files
	filenames = ["name.basics", "title.basics","title.principals","title.ratings"]
	start_time = time.time()
	for filename in filenames:
		t1 = time.time()
		tsv2json(filename+".tsv",filename+".json")
		t2 = time.time()
		print("Converted " + filename + ".tsv in " + "%.2f seconds" % (t2-t1))
	end_time = time.time()
	print("Converted everything in " + "%.2f seconds" % (end_time-start_time))


if __name__ == "__main__":
	main()
