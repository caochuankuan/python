def func(name):
    def innerage(age):
        def innersex(sex):
            print("name:",name,"age:",age,"sex:",sex)
        return innersex
    return innerage
bb=func("yifeng")
cc=bb(26)
cc("male")