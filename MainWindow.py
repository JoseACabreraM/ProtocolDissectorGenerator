import gtk, gobject, os
from EndFieldWindow import EndFieldWindow
from FieldWindow import FieldWindow
from PacketInformationWindow import PacketInformationWindow
from ReferenceListWindow import ReferenceListWindow
from StartFieldWindow import StartFieldWindow
from PCAPWindow import PCAPWindow
from ExportWindow import ExportWindow
from OrganizeViewWindow import OrganizeViewWindow
from DissectorScriptWindow import DissectorScriptWindow
from ProjectImportWindow import ProjectImportWindow
from NewProjectWindow import NewProjectWindow
from WorkspaceLauncherWindow import WorkspaceLauncherWindow


class MainWindow(gtk.Window):

    def __init__(self):

        # Main Window
        super(MainWindow, self).__init__()
        self.set_title("Protocol Dissector Generator System")
        self.set_default_size(500, 1000)
        self.set_position(gtk.WIN_POS_CENTER)

        # Title
        title = gtk.Label("Protocol Dissector Generator System")

        # Buttons' Box
        vbox1 = gtk.VBox()
        box1 = gtk.HButtonBox()

        # Button1
        btn1 = gtk.Button(label="Create Project")
        btn1.connect("clicked", self.show_NewProjectWindow)
        # Button2
        btn2 = gtk.Button(label="Save Project")
        # Button3
        btn3 = gtk.Button(label="Close Project")
        # Button4
        btn4 = gtk.Button(label="Switch Workspace")
        btn4.connect("clicked", self.show_WorkspaceLauncherWindow)
        # Button5
        btn5 = gtk.Button(label="Import Project")
        btn5.connect("clicked", self.show_ProjectImportWindow)
        # Button6
        btn6 = gtk.Button(label="Export Project")
        btn6.connect("clicked", self.show_ExportWindow)
        # Button7
        btn7 = gtk.Button(label="Generate Dissector Script")
        btn7.connect("clicked", self.show_DissectorScriptWindow)
        # Button8
        btn8 = gtk.Button(label="Organize Views")
        btn8.connect("clicked", self.show_OrganizeviewWindow)
        # Button9
        btn9 = gtk.Button(label="Open PCAP")
        btn9.connect("clicked", self.show_PCAPWindow)

        # Pack to box1
        box1.pack_start(btn1, True, True, 0)
        box1.pack_start(btn2, True, True, 0)
        box1.pack_start(btn3, True, True, 0)
        box1.pack_start(btn4, True, True, 0)
        box1.pack_start(btn5, True, True, 0)
        box1.pack_start(btn6, True, True, 0)
        box1.pack_start(btn7, True, True, 0)
        box1.pack_start(btn8, True, True, 0)
        box1.pack_start(btn9, True, True, 0)
        box1.set_border_width(5)

        # VBox
        vbox1.add(box1)
        vbox1.set_border_width(5)

        # Scrolled Window for Workspace
        swWorkspace = gtk.ScrolledWindow()
        swWorkspace.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        # Project Navigator Tree
        pnLabel = gtk.Label("Project Navigator")

        tree = gtk.TreeView()
        languages = gtk.TreeViewColumn()
        cwd = os.getcwd()
        path = cwd.split('\\')
        languages.set_title(path[-1])
        cell1 = gtk.CellRendererText()
        languages.pack_start(cell1, True)
        languages.add_attribute(cell1, "text", 0)
        treestore1 = gtk.TreeStore(str)
        parents = {}
        for dirname, subdirnames, files in os.walk('.'):
            for subdirname in subdirnames:
                parents[os.path.join(dirname, subdirname)] = treestore1.append(parents.get(dirname, None), [subdirname])
            for filename in files:
                treestore1.append(parents.get(dirname, None), [filename])
        tree.append_column(languages)
        tree.set_model(treestore1)
        tree.set_size_request(200, 590)

        swWorkspace.add(tree)

        # TextView
        dbaLabel = gtk.Label("Dissector Builder Area")

        dba = gtk.TextView()
        dba.set_size_request(700, 350)

        # Palette
        paletteLabel = gtk.Label("Palette")

        table = gtk.Table(23, 2, True)
        table.set_row_spacings(2)
        table.set_col_spacings(2)

        # Scrolled Window for Palette
        swPalette = gtk.ScrolledWindow()
        swPalette.set_size_request(400, 350)
        swPalette.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        # Field Section
        fieldLbl = gtk.Label("Field")
        table.attach(fieldLbl, 0, 2, 0, 1)

        btnsf = gtk.Button(label="Start Field")
        btnsf.connect('clicked', self.show_StartFieldWindow)
        table.attach(btnsf, 0, 2, 1, 2)

        vsbtn = gtk.Button(label="Field (Var Size)")
        vsbtn.connect('clicked', self.show_FieldWindow)
        table.attach(vsbtn, 0, 1, 2, 3)

        btn1b = gtk.Button(label="Field (1 Byte)")
        btn1b.connect('clicked', self.show_FieldWindow)
        table.attach(btn1b, 1, 2, 2, 3)

        btn2b = gtk.Button(label="Field (2 Byte)")
        btn2b.connect('clicked', self.show_FieldWindow)
        table.attach(btn2b, 0, 1, 3, 4)

        btn4b = gtk.Button(label="Field (4 Byte)")
        btn4b.connect('clicked', self.show_FieldWindow)
        table.attach(btn4b, 1, 2, 3, 4)

        btn8b = gtk.Button(label="Field (8 Byte)")
        btn8b.connect('clicked', self.show_FieldWindow)
        table.attach(btn8b, 0, 1, 4, 5)

        btn16b = gtk.Button(label="Field (16 Byte)")
        btn16b.connect('clicked', self.show_FieldWindow)
        table.attach(btn16b, 1, 2, 4, 5)

        rlbtn = gtk.Button(label="Reference List")
        rlbtn.connect('clicked', self.show_ReferenceListWindow)
        table.attach(rlbtn, 0, 1, 5, 6)

        pibtn = gtk.Button(label="Packet Information")
        pibtn.connect('clicked', self.show_PacketInformationWindow)
        table.attach(pibtn, 1, 2, 5, 6)

        efbtn = gtk.Button(label="End Field")
        efbtn.connect('clicked', self.show_EndFieldWindow)
        table.attach(efbtn, 0, 2, 6, 7)

        # Construct Section
        constructLbl = gtk.Label("Construct")
        table.attach(constructLbl, 0, 2, 8, 9)

        decisionBtn = gtk.Button(label="Decision")
        table.attach(decisionBtn, 0, 2, 9, 11)
        decisionBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        decisionBtn.connect("drag_data_get", self.on_drag_data_get)

        connectorBtn = gtk.Button(label="Connector")
        table.attach(connectorBtn, 0, 2, 11, 13)
        connectorBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        connectorBtn.connect("drag_data_get", self.on_drag_data_get)

        exprLabel = gtk.Label("Expression")
        table.attach(exprLabel, 0, 1, 13, 14)

        relatOprLabel = gtk.Label("Relational Operator")
        table.attach(relatOprLabel, 0, 2, 14, 15)

        lessBtn = gtk.Button("<")
        table.attach(lessBtn, 0, 1, 15, 16)
        lessBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        lessBtn.connect("drag_data_get", self.on_drag_data_get)

        greaterBtn = gtk.Button(">")
        table.attach(greaterBtn, 1, 2, 15, 16)
        greaterBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        greaterBtn.connect("drag_data_get", self.on_drag_data_get)

        lessOrEqBtn = gtk.Button("<=")
        table.attach(lessOrEqBtn, 0, 1, 16, 17)
        lessOrEqBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        lessOrEqBtn.connect("drag_data_get", self.on_drag_data_get)

        greaterOrEqBtn = gtk.Button(">=")
        table.attach(greaterOrEqBtn, 1, 2, 16, 17)
        greaterOrEqBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        greaterOrEqBtn.connect("drag_data_get", self.on_drag_data_get)

        equalBtn = gtk.Button("==")
        table.attach(equalBtn, 0, 1, 17, 18)
        equalBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        equalBtn.connect("drag_data_get", self.on_drag_data_get)

        notEqBtn = gtk.Button("~=")
        table.attach(notEqBtn, 1, 2, 17, 18)
        notEqBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        notEqBtn.connect("drag_data_get", self.on_drag_data_get)

        lgcOprLabel = gtk.Label("Logical Operator")
        table.attach(lgcOprLabel, 0, 2, 18, 19)

        andBtn = gtk.Button("And")
        table.attach(andBtn, 0, 2, 19, 20)
        andBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        andBtn.connect("drag_data_get", self.on_drag_data_get)

        orBtn = gtk.Button("Or")
        table.attach(orBtn, 0, 2, 20, 21)
        orBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        orBtn.connect("drag_data_get", self.on_drag_data_get)

        notBtn = gtk.Button("Not")
        table.attach(notBtn, 0, 2, 21, 22)
        notBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        notBtn.connect("drag_data_get", self.on_drag_data_get)

        operandBtn = gtk.Button("Operand")
        table.attach(operandBtn, 0, 1, 22, 23)
        operandBtn.drag_source_set(gtk.gdk.BUTTON1_MASK, [("text/plain", 0, 1)], gtk.gdk.ACTION_COPY)
        operandBtn.connect("drag_data_get", self.on_drag_data_get)

        swPalette.add_with_viewport(table)

        # Notebook
        nb = gtk.Notebook()
        nb.set_tab_pos(gtk.POS_TOP)

        tv1 = gtk.TextView()
        nb.append_page(tv1)
        nb.set_tab_label_text(tv1, "Packet Stream Area")

        tv2 = gtk.TextView()
        nb.append_page(tv2)
        nb.set_tab_label_text(tv2, "Dissected Stream Area")

        tv3 = gtk.TextView()
        nb.append_page(tv3)
        nb.set_tab_label_text(tv3, "Raw Data Area")

        tv4 = gtk.TextView()
        nb.append_page(tv4)
        nb.set_tab_label_text(tv4, "Console Area")

        nb.set_size_request(1120, 215)

        # Fixed positions
        fixed = gtk.Fixed()
        fixed.put(title, 12, 5)
        fixed.put(vbox1, 0, 18)
        fixed.put(pnLabel, 12, 80)
        fixed.put(swWorkspace, 12, 100)
        fixed.put(dbaLabel, 500, 80)
        fixed.put(dba, 220, 100)
        fixed.put(paletteLabel, 1112, 80)
        fixed.put(swPalette, 940, 100)
        fixed.put(nb, 220, 475)

        self.add(fixed)
        self.connect("destroy", gtk.main_quit)
        self.set_default_size(0, 700)
        self.show_all()

    def show_WorkspaceLauncherWindow(self, widget):
        wsl = WorkspaceLauncherWindow()

    def show_NewProjectWindow(self, widget):
        npWindow = NewProjectWindow()
    
    def show_StartFieldWindow(self, widget):
        sfWindow = StartFieldWindow(parent=self)

    def show_EndFieldWindow(self, widget):
        efWindow = EndFieldWindow(parent=self)

    def show_FieldWindow(self, widget):
        fwWindow = FieldWindow(parent=self)

    def show_ReferenceListWindow(self, widget):
        rlWindow = ReferenceListWindow(parent=self)

    def show_PacketInformationWindow(self, widget):
        piWindow = PacketInformationWindow(parent=self)

    def show_ExportWindow(self, widget):
        sfWindow = ExportWindow()

    def show_ProjectImportWindow(self, widget):
        importWindow = ProjectImportWindow()

    def show_DissectorScriptWindow(self, widget):
        dsWindow = DissectorScriptWindow()

    def show_PCAPWindow(self, widget):
        pcapWindow = PCAPWindow()

    def show_OrganizeviewWindow(self, widget):
        organizeViewWindow = OrganizeViewWindow()

    def on_drag_data_get(self, widget, drag_context, selection, info, time):

        if widget.get_label() == 'Decision':
            selection.set_text('if(Condition)\n{\n\n}', -1)
        else:
            selection.set_text(widget.get_label(), -1)


MainWindow()
gtk.main()
