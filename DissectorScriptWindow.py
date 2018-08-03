import gtk
class DissectorScriptWindow(gtk.Window):

    def __init__(self):

        #Main Window
        super(DissectorScriptWindow, self).__init__()
        self.set_title("Dissector Script")
        self.set_default_size(500,250)
        self.set_position(gtk.WIN_POS_CENTER)

        #labels
        label = gtk.Label("Generate a Custom Dissector Script from a Selected Project")
        label2= gtk.Label("Project")
        label3= gtk.Label("Dissector Format")
        label4= gtk.Label("Save Location")

        #Buttons Box
        vbox1 = gtk.VBox()
        box1 = gtk.HButtonBox()

        #Button1
        btn1 = gtk.Button(label="Generate")
        #Button2
        btn2 = gtk.Button(label="Cancel")
        #Button3
        btn3 = gtk.Button(label="Browse")
        #Button4
        btn4 = gtk.Button(label="Browse")

        #Pack to box1
        box1.pack_start(btn1, True, True, 0)
        box1.pack_start(btn2, True, True, 0)
        box1.set_border_width(5)

		#TextView1
        dba1 = gtk.TextView()
        dba1.set_size_request(250, 20)
		#TextView2
        dba2 = gtk.TextView()
        dba2.set_size_request(250, 20)
		#TextView3
        dba3 = gtk.TextView()
        dba3.set_size_request(250, 20)

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
        btn4.connect('clicked',chooseFile,dba3)

        #VBox
        vbox1.add(box1)
        vbox1.set_border_width(5)

        #Fixed positions
        fixed = gtk.Fixed()
        fixed.put(vbox1,310, 160)
        fixed.put(label,100,  0)
        fixed.put(dba1, 150, 80)
        fixed.put(dba2, 150,110)
        fixed.put(dba3, 150,140)
        fixed.put(label2,50, 80)
        fixed.put(label3,50, 110)
        fixed.put(label4,50, 140)
        fixed.put(btn3,405,80)
        fixed.put(btn4,405,140)

        self.add(fixed)
        self.show_all()
