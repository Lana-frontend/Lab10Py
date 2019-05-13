class Notebook:
    total_quantity_in_stock = 10

    def __init__(self, color_in="%NO_INFO%", name_in="%NO_INFO%", price_in=0, number_of_pages_in=0, thickness_in=0,
             type_in="%NO_INFO%"):
        self._color = color_in
        self._name = name_in
        self._price = price_in
        self._number_of_pages = number_of_pages_in
        self._thickness = thickness_in
        self._type = type_in

    def __del__(self):
        print("%s was deleted" % self._color)

    def __str__(self):
        return "Color: {0}, Name: {1}, Price: {2} uah   \nNumber of pages: {3}, Thickness: {4} sm, Type: {5}.\n".format(
            self._color, self._name,
            self._price, self._number_of_pages, self._thickness, self._type)

    @staticmethod
    def update_quantity_in_stock(quantity_in_stock):
        Notebook.total_quantity_in_stock += quantity_in_stock


def main():
    unknown = Notebook()
    aquamarine = Notebook("Red", "Boo", 15, 20, 4, "cell")

    print(unknown)
    print(aquamarine)

    print("Total quantity in stock: " + str(Notebook.total_quantity_in_stock))
    Notebook.update_quantity_in_stock(2)
    print("Total quantity in stock: " + str(Notebook.total_quantity_in_stock))
    print()


main()