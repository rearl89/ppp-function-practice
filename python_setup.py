# initial printing "Hello" in terminal
print("Hello from inside a file!")
# printing hello to a user
def hello():
    print("Hello user!")
hello()
# printing arguments as list items
def pack(item1, item2, item3):
    return [item1, item2, item3]
pack("Pencil", "Pen", "Paper")
# print list of food items
def eat_lunch(food_items):
    if len(food_items) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(food_items)):
            if i == 0:
                print(f"First I eat {food_items[0]}")
            else:
                print(f"Next I eat {food_items[i]}")
eat_lunch([])
eat_lunch(["carrots", "pudding", "sandwich", "apple"])