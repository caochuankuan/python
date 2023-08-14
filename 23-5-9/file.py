f=open("css.css","r")
css=f.read()
print(css)
f.close()

with open("a.txt","r") as f:
    print(f.read())
    f.close()

try:
    f=open("a.txt","r")
    print(f.read())
finally:
    if f:
        f.close()