import gtk, gobject, os

class WorkspaceLauncherWindow(gtk.Window):

  def __init__(self):

    #Export Window
    super(WorkspaceLauncherWindow, self).__init__()
    self.set_title("Workspace Launcher")
    self.set_default_size(450,600)
    self.set_position(gtk.WIN_POS_CENTER)
    self.set_border_width(10)

    # Create labels and buttons
    table = gtk.Table(rows=3, columns=3, homogeneous=False)
    lblM = gtk.Label()
    lblM.set_markup("\n<b>Select a directory as a workspace: PDGS uses the workspace\ndirectory to store projects</b>")
    lblM.set_justify(gtk.JUSTIFY_CENTER)
    lbl1 = gtk.Label("Workspace")
    txtBox1 = gtk.TextView()
    txtBox1.set_editable(False)
    btn1 = gtk.Button("Browse")
    btn3 = gtk.Button("Launch")
    btn4 = gtk.Button("Cancel")

    # Attach all the buttons and labels to the table
    table.attach(lblM,0,4,0,1)
    table.attach(lbl1,0,1,1,2)
    table.attach(txtBox1,1,2,1,2)

    table.attach(btn1,2,3,1,2)
    table.attach(btn3,1,2,2,3)
    table.attach(btn4,2,3,2,3)

    table.set_row_spacings(20)
    table.set_col_spacings(15)

    # Method for canceling
    def cancel(widget,callback_data = None):
        self.destroy()
    # Method for opening a browse window
    def chooseFile(self, textview):
        dialog = gtk.FileChooserDialog("Open..", None, gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_OPEN, gtk.RESPONSE_OK, gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
        dialog.set_default_response(gtk.RESPONSE_OK)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            textBuffer = gtk.TextBuffer()
            textBuffer.set_text(dialog.get_filename())
            textview.set_buffer(textBuffer)
        dialog.destroy()

    # set the action of the button
    btn1.connect('clicked',chooseFile,txtBox1)
    btn4.connect('clicked',cancel)

    self.add(table)
    self.set_default_size(0,0)
    self.set_resizable(False)
    self.show_all()
#WorkspaceLauncherWindow()
#gtk.main()
