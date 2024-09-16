# list : data structure that can hold multiple values of different data types
# list is mutable (can be modified)
# list is ordered (items have a defined order)
# list is indexed (items can be accessed by index)
# list is dynamic (can grow and shrink in size)
# list is denoted by square brackets []

# array : data structure that can hold multiple values of the same data type
# array is mutable
# array is ordered
# array is indexed
# array is static (fixed size)
# array is denoted by square brackets []

# creating a list
list_of_numbers = [1, 2, 3, 4, 5]
list_of_clouds = ["aws", "azure", "gcp", "digital ocean", "alibaba cloud"]


print(list_of_clouds)

list_of_clouds.append("IBM")

list_of_clouds.append("Salesforce")

list_of_clouds.append("Oracle")

list_of_clouds.append("linode")

print(list_of_clouds)

list_of_clouds.insert(2, "Runpod")

print(list_of_clouds)


print(len(list_of_clouds))

list_of_clouds.insert(0, "Hello Cloud")

print(list_of_clouds)

print(len(list_of_clouds))

for cloud in list_of_clouds:
    print(" ")
    print(cloud)

for i in range(1,6):
    print(i)

for i in range(1,10,2):
    print(i)