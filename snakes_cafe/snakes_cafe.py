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
    yourorder = input(' ')
    
    while yourorder != 'quit':
        
        if yourorder in ourmenu:
            order.append(yourorder)
            print(f'** {order.count(yourorder)} order of {yourorder} have been added to your meal **')
        else:
            print('please order one of the menu!!')
        yourorder = input(' ')

if __name__ == "__main__":

   myfunction()
