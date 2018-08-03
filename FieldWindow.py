import gtk

class FieldWindow(gtk.Dialog):

    def __init__(self, parent):

        #Field Window
        super(FieldWindow, self).__init__(parent=parent)
        self.set_title("Field [Abbreviation]")

        #Table
        table = gtk.Table(9, 6)
        table.set_row_spacings(5)
        table.set_col_spacings(5)

        nameLbl = gtk.Label("Name")
        table.attach(nameLbl, 0, 1, 0, 1)

        nameTxt = gtk.TextView()
        nameTxt.set_size_request(300,10)
        table.attach(nameTxt, 1, 5, 0, 1)

        abvtnLbl = gtk.Label("Abbreviation")
        table.attach(abvtnLbl, 0, 1, 1, 2)

        abvtTxt = gtk.TextView()
        abvtTxt.set_size_request(300,10)
        table.attach(abvtTxt, 1, 5, 1, 2)

        descptnLbl = gtk.Label("Description")
        table.attach(descptnLbl, 0, 1, 2, 3)

        descptnTxt = gtk.TextView()
        descptnTxt.set_size_request(300,10)
        table.attach(descptnTxt, 1, 5, 2, 3)

        refListLbl = gtk.Label("Reference List")
        table.attach(refListLbl, 0, 1, 3, 4)

        refListcombobox = gtk.ComboBox()
        refListstore = gtk.ListStore(str)
        refListcell = gtk.CellRendererText()
        refListcombobox.pack_start(refListcell)
        refListcombobox.add_attribute(refListcell, 'text', 0)
        refListstore.append (["List of reference lists"])
        refListcombobox.set_model(refListstore)
        table.attach(refListcombobox, 1, 5, 3, 4)

        dataTypeLbl = gtk.Label("Data Type")
        table.attach(dataTypeLbl, 0, 1, 4, 5)

        dataTypecombobox = gtk.ComboBox()
        dataTypestore = gtk.ListStore(str)
        dataTypecell = gtk.CellRendererText()
        dataTypecombobox.pack_start(dataTypecell)
        dataTypecombobox.add_attribute(dataTypecell, 'text', 0)
        dataTypestore.append (["List of data types"])
        dataTypecombobox.set_model(dataTypestore)
        table.attach(dataTypecombobox, 1, 5, 4, 5)

        baseLbl = gtk.Label("Base")
        table.attach(baseLbl, 0, 1, 5, 6)

        basecombobox = gtk.ComboBox()
        basestore = gtk.ListStore(str)
        basecell = gtk.CellRendererText()
        basecombobox.pack_start(basecell)
        basecombobox.add_attribute(basecell, 'text', 0)
        basestore.append (["List of bases"])
        basecombobox.set_model(basestore)
        table.attach(basecombobox, 1, 5, 5, 6)

        maskLbl = gtk.Label("Mask")
        table.attach(maskLbl, 0, 1, 6, 7)

        maskTxt = gtk.TextView()
        maskTxt.set_size_request(300,10)
        table.attach(maskTxt, 1, 5, 6, 7)

        valconsLbl = gtk.Label("Value Constraint")
        table.attach(valconsLbl, 0, 1, 7, 8)

        valconsTxt = gtk.TextView()
        valconsTxt.set_size_request(300,10)
        table.attach(valconsTxt, 1, 5, 7, 8)

        requiredLbl = gtk.Label("Required")
        table.attach(requiredLbl, 0, 1, 8, 9)

        requiredTxt = gtk.CheckButton(None)
        table.attach(requiredTxt, 1, 5, 8, 9, xpadding=140)

        fixed = gtk.Fixed()
        fixed.put(table, 5, 15)
        fixed.show_all()

        self.vbox.add(fixed)
        self.run()
        self.destroy()
