import gtk, gobject, os

class NewProjectWindow(gtk.Window):

  def __init__(self):

    #Export Window
    super(NewProjectWindow, self).__init__()
    self.set_title("New Project")
    self.set_default_size(900,900)
    self.set_position(gtk.WIN_POS_CENTER)
    self.set_border_width(10)

    # Create table
    table = gtk.Table(rows=6, columns=10, homogeneous=False)

    # Create labels
    lblM = gtk.Label()
    lblM.set_markup("\n<b>Create a new project</b>")
    lblM.set_justify(gtk.JUSTIFY_CENTER)
    lbl1 = gtk.Label("Project Name")
    lbl2 = gtk.Label("Description")

    # Create textViews
    txtBox1 = gtk.TextView()
    txtBox1.set_editable(False)
    txtBox2 = gtk.TextView()
    txtBox2.set_editable(False)

    # Create buttons
    CreateBtn = gtk.Button("Create")
    CancelBtn = gtk.Button("Cancel")

    # Attaach everithing to the table
    table.attach(lblM,0,3,0,1)
    table.attach(lbl1,0,1,1,2)
    table.attach(lbl2,0,1,2,3)
    table.attach(txtBox1,1,9,1,2)
    table.attach(txtBox2,1,9,2,5)
    table.attach(CreateBtn,8,9,5,6)
    table.attach(CancelBtn,9,10,5,6)

    table.set_row_spacings(20)
    table.set_col_spacings(15)
    # Method for closing window
    def exit(widget,callback_data = None):
        self.destroy()

    # set the action of the button
    CancelBtn.connect("clicked", exit)

    self.add(table)
    self.set_default_size(0,0)
    self.set_resizable(False)
    self.show_all()

#NewProjectWindow()
#gtk.main()
