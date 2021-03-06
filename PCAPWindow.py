import gtk, gobject, os

class PCAPWindow(gtk.Window):

  def __init__(self):
  
    #PCAP Window 
    super(PCAPWindow, self).__init__()
    self.set_title("PCAP")
    self.set_default_size(250,300)
    self.set_position(gtk.WIN_POS_CENTER)

    # Labels
    descLabel = gtk.Label("Open a PCAP file")
    pcapLabel = gtk.Label("PCAP Name")

    #Browse Buttons Box
    hbox1 = gtk.HBox()
    textViewBox = gtk.VButtonBox()
    browseButtonBox = gtk.VButtonBox()
    labelBox = gtk.VButtonBox()
    
    #Action Buttons Box
    vbox1 = gtk.VBox()
    actionButtonBox = gtk.HButtonBox()
    
    # Browse Button 1
    browsebtn1 = gtk.Button(label="Browse")
    
    # Open Button
    openbtn = gtk.Button(label="Open")
    
    # Cancel Button
    cancelbtn = gtk.Button(label="Cancel")
    
    # Text Buffers 
    pcapTextView = gtk.TextView()
    
    # Packing Browse Buttons

    labelBox.pack_start(pcapLabel, True, True, 5)
    
    browseButtonBox.pack_start(browsebtn1, True, True, 5)

    textViewBox.pack_start(pcapTextView, True, True, 5)

    browseButtonBox.set_border_width(5)

    # Adding Buttons Box to Buttons VBox
    hbox1.add(labelBox)
    hbox1.add(textViewBox)
    hbox1.add(browseButtonBox)
    
    # Packing Action Buttons
    actionButtonBox.pack_start(openbtn, True, True, 0)
    actionButtonBox.pack_start(cancelbtn, True, True, 0)
    
    # Adding Actions Box to Actions VBox
    vbox1.add(actionButtonBox)

    # File Chooser
    def chooseDialog(self, textview):
      dialog = gtk.FileChooserDialog("Open..", None, gtk.FILE_CHOOSER_ACTION_OPEN,(gtk.STOCK_OPEN, gtk.RESPONSE_OK, gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL))
      dialog.set_default_response(gtk.RESPONSE_OK)
      response = dialog.run()
      if response == gtk.RESPONSE_OK:
         #print dialog.get_filename(), 'selected'
          textBuffer = gtk.TextBuffer()
          textBuffer.set_text(dialog.get_filename())
          textview.set_buffer(textBuffer)
      dialog.destroy()

    # To close and exit the application
    def exit(widget, callback_data=None):
      self.destroy()
    
    browsebtn1.connect("clicked", chooseDialog, pcapTextView)
    cancelbtn.connect("clicked", exit)
    
    #Fixed positions
    fixed = gtk.Fixed()
    fixed.put(descLabel, 84, 5)
    fixed.put(hbox1, 0, 25)
    fixed.put(vbox1, 84, 65)
    
    self.add(fixed)
    self.set_default_size(0,0)
    self.set_resizable(False)
    self.show_all()

#PCAPWindow()
#gtk.main()
