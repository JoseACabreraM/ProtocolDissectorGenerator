import gtk




class PacketInformationWindow(gtk.Dialog):

    def __init__(self, parent):
        super(PacketInformationWindow, self).__init__(parent=parent)
        self.set_title("Packet Information")
        # self.set_size_request(460,100)
        self.row = 1

        #Table
        table = gtk.Table(6, 7)
        table.set_row_spacings(5)
        table.set_col_spacings(5)

        valueLbl = gtk.Label("Value")
        table.attach(valueLbl, 0, 1, 0, 1)

        textDescLbl = gtk.Label("Text Description")
        table.attach(textDescLbl, 1, 2, 0, 1)

        valueTxt = gtk.TextView()
        valueTxt.set_size_request(220, 20)
        table.attach(valueTxt, 0, 1, self.row, self.row + 1)

        textDescTxt = gtk.TextView()
        textDescTxt.set_size_request(220, 20)
        table.attach(textDescTxt, 1, 2, self.row, self.row + 1)

        self.row += 1

        def add_field(widget):
            add_valueTxt = gtk.TextView()
            add_valueTxt.set_size_request(220, 20)
            table.attach(add_valueTxt, 0, 1, self.row, self.row + 1)

            add_textDescTxt = gtk.TextView()
            add_textDescTxt.set_size_request(220, 20)
            table.attach(add_textDescTxt, 1, 2, self.row, self.row + 1)

            table.remove(self.button)
            self.OPEN_IMAGE = gtk.image_new_from_stock(gtk.STOCK_ADD, gtk.ICON_SIZE_BUTTON)
            self.button = gtk.Button()
            self.button.connect("clicked", add_field)
            self.button.set_image(self.OPEN_IMAGE)
            table.attach(self.button, 3, 4, self.row + 1, self.row + 2)
            fixed.show_all()

            self.row += 1

        self.OPEN_IMAGE = gtk.image_new_from_stock(gtk.STOCK_ADD, gtk.ICON_SIZE_BUTTON)
        self.button = gtk.Button()
        self.button.connect("clicked", add_field)
        self.button.set_image(self.OPEN_IMAGE)
        table.attach(self.button, 3, 4, self.row + 1, self.row + 2)

        fixed = gtk.Fixed()
        fixed.put(table, 5, 10)
        fixed.show_all()

        self.vbox.add(fixed)
        self.run()
        self.destroy()
