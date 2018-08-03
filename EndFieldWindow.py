import gtk

class EndFieldWindow(gtk.Dialog):

    def __init__(self, parent):

        super(EndFieldWindow, self).__init__(parent=parent)

        self.set_title("End Field")
        self.set_size_request(500,50)

        self.run()
        self.destroy()
