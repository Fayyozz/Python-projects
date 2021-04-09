cats_list = []

# creating 100 cats with boolean False initially to represent if they have hats
for n in range(100):
    cats_list.append({"cat" + f"{n}": False})


def switch_hat(cat):
    for key in cat:
        if cat[key] is True:
            cat[key] = False
        else:
            cat[key] = True


for n in range(len(cats_list)):
    step = n
    for cat_dict in cats_list:
        try:
            if cats_list.index(cat_dict) % n == 0:
                switch_hat(cats_list[step])
                step += n
        except ZeroDivisionError:
            continue
        except IndexError:
            break

hat_list = []
for cat_dict in cats_list:
    for key in cat_dict:
        if cat_dict[key]:
            hat_list.append(key)
            print(key)


print(len(hat_list))



