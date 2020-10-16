# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Order import Order
from Courier import Courier

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = Order()
    order.readJson()
    print(len(order.orderdata))
    fifo_count = order.fifo()
    matched_count = order.matched()
    print(fifo_count,matched_count)
