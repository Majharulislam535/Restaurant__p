from Menu import Pizza,Burger,Drinks,Menu
from Restaurent import Restaurent
from User import Chef,Customer,Server,Manager
from Order import Order

def main():
    menu=Menu()
    pizza_1 = Pizza('Shutki pizza',600,'large',['shutki','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2=Pizza('Alur Borta pizza',400,'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3=Pizza('Dal pizza',500,'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)


    #Burger 

    burger_1 = Burger('Naga Burger',1000,'chicken',['bread','chili'])
    menu.add_menu_item('burger',burger_1)
    burger_2 = Burger('Beef Burger',1200,'beef',['goru','haddi'])
    menu.add_menu_item('burger',burger_2)

    #drinks

    coke = Drinks('coke',50,True)
    menu.add_menu_item('drinks',coke)
    coffe = Drinks('Mocha',300,False)
    menu.add_menu_item('drinks',coffe)
 
    # Restaurant 
   
    restaurent = Restaurent("Sona miya Restraurant",2000,menu)

    manager = Manager('kala miya',123,'kalachan@gmail.com','sonaimori',12000,'1 jan 2020','core')
    restaurent.add_employee('manager',manager)
    chef = Chef('Rustom Sonai',1235,'rustomSonai@gmail.com','Sonaipara',1000,'2 march 2555','chef','everything')
    restaurent.add_employee('chef',chef)
    server = Server('Sonaikot',1235,'Sonaikot@gmail.com','Sonaigi',1000,'2 march 25055','everything')
    restaurent.add_employee('server',server)

    #customer order
    customar_1 = Customer('Shakib khan',10000,22,'sokhina@gmail.com','bannani')
    order_1 = Order(customar_1,[pizza_1,coffe])
    customar_1.place_order(order_1)
    restaurent.add_order(order_1)
    restaurent.receive_payment(order_1,2000,customar_1)
    



    print(restaurent.revenue,restaurent.balance)
    

    # menu.show_menu()
    # restaurent.show_employ()



if __name__ =='__main__':
    main()

