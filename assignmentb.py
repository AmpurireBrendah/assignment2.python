#Lists 
#Lists are mutable, it also with index .
#Items stored should be the same.
#Lists are array like structure (using indexing)
studentNames=["Sandra","Patricia","Phionah","Anitah"]#strings
studentMarks=[80,56,78,90] #integers
data=["Sandra",90,"Kamwokya"] #mixed types

#Access the whole list
print(studentNames, type(studentNames))

#Accessing list items
#Indexes (positive indexing)
print(studentNames[0])#first item
print(studentNames[1])#second item
print(studentNames[2])#third item
print(studentNames[3])#last item

#Indexes (Negative Indexing)
print(studentNames[-4])#first item
print(studentNames[-3])#second item
print(studentNames[-2])#third item
print(studentNames[-1])#Last item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      )

#question 1
#print from Patricia, Anitah, Faith, Phionah .Excluding the last and first using slicing.
studentNames.insert(2,"Faith")
studentNames.remove("Sandra")
print(studentNames)
print(studentNames[1:3]) #Excluding the first and last items

#question 2
#Add Masha at the fourth position
studentNames.insert(3,"Masha")
print(studentNames)

#question 3
#Update the name Phionah to Phionah Aladinah
studentNames[studentNames.index("Phionah")]="Phionah Aladinah"
print(studentNames)

#question 4
#Display the length of the student list.
print(f"The length of the student list is : {len(studentNames)}")

#question 5
#Print all the student names using  a 4loop.
for x in studentNames:
    print(x)

# question 6
# Calculate the total marks for the student marks variable .
totalMarks=sum(studentMarks)
print(totalMarks)   #304  