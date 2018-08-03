import gtk


class OrganizeViewWindow(gtk.Window):
    def __init__(self):
        super(OrganizeViewWindow, self).__init__()
        self.set_title("Organize Views")
        self.set_border_width(10)
        self.set_position(gtk.WIN_POS_CENTER)
        # Boxes
        main_vbox = gtk.VBox(spacing=10)
        button_box = gtk.HBox()

        # Table to organize widgets
        table = gtk.Table(9, 4)
        table.set_row_spacings(5)
        table.set_col_spacings(5)

        # The title label
        title_box = gtk.HBox()
        title_label = gtk.Label("Customize the views")
        title_box.pack_start(title_label, expand=True, fill=True, padding=10)

        # Hide and show labels
	show_label = gtk.Label("Show")
        table.attach(show_label, 1, 2, 0, 1)
        hide_label = gtk.Label("Hide")
        table.attach(hide_label, 2, 3, 0, 1)

        # Project navigation radio buttons
        proj_nav_label = gtk.Label("Project Navigation")
        table.attach(proj_nav_label, 0, 1, 1, 2)
        self.proj_nav_btn1 = gtk.RadioButton(None)
        self.proj_nav_btn1.connect("toggled", self.on_selected, "proj_nav_btn1")
        table.attach(self.proj_nav_btn1, 1, 2, 1, 2)
        proj_nav_btn2 = gtk.RadioButton(self.proj_nav_btn1)
        proj_nav_btn2.connect("toggled", self.on_selected)
        table.attach(proj_nav_btn2, 2, 3, 1, 2)

        # Dissector builder area radio buttons
        dba_label = gtk.Label("Dissector Builder Area")
        table.attach(dba_label, 0, 1, 2, 3)
        self.dba_btn1 = gtk.RadioButton(None)
        self.dba_btn1.connect("toggled", self.on_selected, "dba_btn1")
        table.attach(self.dba_btn1, 1, 2, 2, 3)
        dba_btn2 = gtk.RadioButton(self.dba_btn1)
        dba_btn2.connect("toggled", self.on_selected)
        table.attach(dba_btn2, 2, 3, 2, 3)

        # Palette radio buttons
        pallet_label = gtk.Label("Palette")
        table.attach(pallet_label, 0, 1, 3, 4)
        self.palette_btn1 = gtk.RadioButton(None)
        self.palette_btn1.connect("toggled", self.on_selected, "palette_btn1")
        table.attach(self.palette_btn1, 1, 2, 3, 4)
        palette_btn2 = gtk.RadioButton(self.palette_btn1)
        palette_btn2.connect("toggled", self.on_selected)
        table.attach(palette_btn2, 2, 3, 3, 4)

        # Packet stream area radio buttons
        psa_label = gtk.Label("Packet Stream Area")
        table.attach(psa_label, 0, 1, 4, 5)
        self.psa_btn1 = gtk.RadioButton(None)
        self.psa_btn1.connect("toggled", self.on_selected, "psa_btn1")
        table.attach(self.psa_btn1, 1, 2, 4, 5)
        psa_btn2 = gtk.RadioButton(self.psa_btn1)
        psa_btn2.connect("toggled", self.on_selected)
        table.attach(psa_btn2, 2, 3, 4, 5)

        # Dissected stream area radion buttons
        dsa_label = gtk.Label("Dissected Stream Area")
        table.attach(dsa_label, 0, 1, 5, 6)
        self.dsa_btn1 = gtk.RadioButton(None)
        self.dsa_btn1.connect("toggled", self.on_selected, "dsa_btn1")
        table.attach(self.dsa_btn1, 1, 2, 5, 6)
        dsa_btn2 = gtk.RadioButton(self.dsa_btn1)
        dsa_btn2.connect("toggled", self.on_selected)
        table.attach(dsa_btn2, 2, 3, 5, 6)

        # Raw data area radio buttons
        rda_label = gtk.Label("Raw Data Area")
        table.attach(rda_label, 0, 1, 6, 7)
        self.rda_btn1 = gtk.RadioButton(None)
        self.rda_btn1.connect("toggled", self.on_selected, "rda_btn1")
        table.attach(self.rda_btn1, 1, 2, 6, 7)
        rda_btn2 = gtk.RadioButton(self.rda_btn1)
        rda_btn2.connect("toggled", self.on_selected)
        table.attach(rda_btn2, 2, 3, 6, 7)

        # Console area radio buttons
        console_label = gtk.Label("Console Area")
        table.attach(console_label, 0, 1, 7, 8)
        self.console_btn1 = gtk.RadioButton(None)
        self.console_btn1.connect("toggled", self.on_selected, "console_btn1")
        table.attach(self.console_btn1, 1, 2, 7, 8)
        console_btn2 = gtk.RadioButton(self.console_btn1)
        console_btn2.connect("toggled", self.on_selected)
        table.attach(console_btn2, 2, 3, 7, 8)

        # The buttons
        rtd_button = gtk.Button(label="Restore to Default")
        confirm_button = gtk.Button(label="Confirm")
        cancel_button = gtk.Button(label="Cancel")
        button_box.pack_start(rtd_button, True, True, 5)
        button_box.pack_start(confirm_button, True, True, 5)
        button_box.pack_start(cancel_button, True, True, 5)

        # Sets all the radio buttons to true
        def restore_to_default(widget):
            self.proj_nav_btn1.set_active(True)
            self.dba_btn1.set_active(True)
            self.palette_btn1.set_active(True)
            self.psa_btn1.set_active(True)
            self.dsa_btn1.set_active(True)
            self.rda_btn1.set_active(True)
            self.console_btn1.set_active(True)

        # Returns the values of the radio buttons
        def confirm(widget):
            self.destroy()
            return self.proj_nav_btn1.get_active(), self.dba_btn1.get_active(), \
                   self.palette_btn1.get_active(), self.psa_btn1.get_active(), \
                   self.dsa_btn1.get_active(), self.rda_btn1.get_active(), \
                   self.console_btn1.get_active()

        # Exits the window
        def exit(widget, callback_data=None):
            self.destroy()

        rtd_button.connect("clicked", restore_to_default)
        confirm_button.connect("clicked", confirm)
        cancel_button.connect("clicked", exit)

        main_vbox.pack_start(title_box, True, True, 5)
        main_vbox.pack_start(table, True, True, 5)
        main_vbox.pack_start(button_box, True, True, 5)

        self.add(main_vbox)
        self.show_all()

    # Debugging method
    def on_selected(self, widget, data=None):
        return
        # print "Project Navigation: %s\nDissector Building Area: %s\n" \
        #       "Palette: %s\nPacket Stream Area: %s\nDissected Stream Area: %s\n" \
        #       "Raw Data Area: %s\nConsole Area: %s" % (self.proj_nav_btn1.get_active(),
        #                                                self.dba_btn1.get_active(),
        #                                                self.palette_btn1.get_active(),
        #                                                self.psa_btn1.get_active(),
        #                                                self.dsa_btn1.get_active(),
        #                                                self.rda_btn1.get_active(),
        #                                                self.console_btn1.get_active())
