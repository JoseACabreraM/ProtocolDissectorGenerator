import gtk, gobject, os

class ProjectImportWindow(gtk.Window):

    def __init__(self):

        #Main Window
        super(ProjectImportWindow, self).__init__()
        self.set_title("Project Import")
        self.set_default_size(500,200)
        self.set_position(gtk.WIN_POS_CENTER)

        #labels
        label = gtk.Label("Import a Project Into The Current Workspace")
        label2= gtk.Label("Project")

        #Buttons Box
        vbox1 = gtk.VBox()
        box1 = gtk.HButtonBox()

        #Button1
        btn1 = gtk.Button(label="Import")
        #Button2
        btn2 = gtk.Button(label="Cancel")
        #Button3
        btn3 = gtk.Button(label="Browse")

        #Pack to box1
        box1.pack_start(btn1, True, True, 0)
        box1.pack_start(btn2, True, True, 0)
        box1.set_border_width(5)

		#TextView1
        dba1 = gtk.TextView()
        dba1.set_size_request(250, 20)

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
        btn2.connect('clicked',cancel)
        btn3.connect('clicked',chooseFile,dba1)

        #VBox
        vbox1.add(box1)
        vbox1.set_border_width(5)

        #Fixed positions
        fixed = gtk.Fixed()
        fixed.put(label,140,  0)
        fixed.put(vbox1,290, 110)
        fixed.put(dba1, 130, 80)
        fixed.put(label2,80, 80)
        fixed.put(btn3,385,80)

        self.add(fixed)
        self.show_all()

#ProjectImportWindow()
#gtk.main()
