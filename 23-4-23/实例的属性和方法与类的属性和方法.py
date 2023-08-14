class Hello(object):
    text = "hello world!"
a=Hello()
print(Hello.text)
print(a.text)
print("==============")
Hello.text="666666"
print(Hello.text)
print(a.text)
print("==============")
a.text="1111111"
print(Hello.text)
print(a.text)
print("==============")
print(dir(Hello))
print(dir(a))