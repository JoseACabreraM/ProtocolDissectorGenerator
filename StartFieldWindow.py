import gtk


class StartFieldWindow(gtk.Dialog):

    def __init__(self, parent):
        # StartField Window
        super(StartFieldWindow, self).__init__(parent=parent)
        self.set_title("Start Field [Protocol Name]")
        self.set_size_request(470, 150)

        # Table
        table = gtk.Table(5, 6)
        table.set_row_spacings(5)
        table.set_col_spacings(5)

        protocolNameLbl = gtk.Label("Protocol Name")
        table.attach(protocolNameLbl, 0, 1, 0, 1)

        protocolNameTxt = gtk.TextView()
        protocolNameTxt.set_size_request(300, 10)
        table.attach(protocolNameTxt, 1, 5, 0, 1)

        protocolDescLbl = gtk.Label("Protocol Description")
        table.attach(protocolDescLbl, 0, 1, 1, 2)

        protocolDescTxt = gtk.TextView()
        protocolDescTxt.set_size_request(300, 10)
        table.attach(protocolDescTxt, 1, 5, 1, 2)

        dependentPNLbl = gtk.Label("Dependent Protocol Name")
        table.attach(dependentPNLbl, 0, 1, 2, 3)

        dependentPNTxt = gtk.TextView()
        dependentPNTxt.set_size_request(300, 10)
        table.attach(dependentPNTxt, 1, 5, 2, 3)

        dependencyPttrnLbl = gtk.Label("Dependency Pattern")
        table.attach(dependencyPttrnLbl, 0, 1, 3, 4)

        dependencyPttrnTxt = gtk.TextView()
        dependencyPttrnTxt.set_size_request(300, 10)
        table.attach(dependencyPttrnTxt, 1, 5, 3, 4)

        fixed = gtk.Fixed()
        fixed.put(table, 5, 10)
        fixed.show_all()

        self.vbox.add(fixed)
        self.run()
        self.destroy()
