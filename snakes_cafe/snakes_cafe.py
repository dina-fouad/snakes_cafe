menu = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
Appetizers
----------
Wings
Cookies
Spring Rolls
Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden
Desserts
--------
Ice Cream
Cake
Pie
Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
"""
print(menu)

ourmenu = ["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]

def myfunction():

    order = []
    your = input(' ')
    
    while your!= 'quit':
        
        if your in ourmenu:
            order.append(your)
            print(f'** {order.count(your)} order of {your} have been added to your meal **')
        else:
            print('please order one of the menu!!')
        your = input(' ')

if __name__ == "__main__":



   myfunction()
