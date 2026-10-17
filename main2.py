
file_read = open('Codignal.txt', 'w')
print("File in Read Mode -")
print(file_read.read())
file_read.close()


file_write = open('Codignal.txt', 'w')

file_write.write(" File in write mode ....")
file_write.write("Hi! I am Penguin. I am 1 yr. old ")
file_write.close()


file_append = open('Codignal.txt',  'a')

file_append.write("\n File in append mode ....")
file_append.write("Hi! I am Penguin. I am 1 yr. old")
file_append.close()