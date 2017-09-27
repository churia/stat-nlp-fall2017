from sklearn.metrics import confusion_matrix as cfm

with open("output_dev.txt") as f:
	data = f.readlines()

pred = []
y = []
label = {"drug":1,"person":2,"place":3,"movie":4,"company":5}

for line in data:
	strs = line.split()
	for s in strs:
		if "guess=" in s:
			pred.append(label[s.replace("guess=","")])
		if "gold=" in s:
			y.append(label[s.replace("gold=","")])

print cfm(y,pred)

index = [i for i,e in enumerate(y) if e!=pred[i]]
for idx in index:
	print data[idx].strip()
						
