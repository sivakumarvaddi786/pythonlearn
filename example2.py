from socket import SIO_RCVALL


py_string  = "This is the first line"
py_string_len  = len(py_string)
print(py_string[0:4])
print(py_string[:4])
print(py_string[:-1])
print(py_string_len)

first = "Siva"
last = "vaddi" 
message1 = 'hello ' + first + '['  + last + '] how are you?'
print(message1)

#formated string stars with f
msg1= f"hello {first} [{last}]. How are you? "
