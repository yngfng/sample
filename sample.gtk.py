#! /usr/bin/env python


#= VBox ================================================
vbox = gtk.VBox(False, 20)
self.window.add(vbox)
vbox.pack_start(button, True, True, 2)
#= Window ================================================
super(PyApp, self).__init__()
self.set_title("Buttons")
self.set_size_request(250, 200)
self.set_position(gtk.WIN_POS_CENTER)
self.set_icon_from_file("web.png")
self.connect("destroy", gtk.main_quit)
self.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(6400, 6400, 6440))
w = self.allocation.width
h = self.allocation.height
        
#= Fixed ================================================
fixed = gtk.Fixed()
fixed.put(btn1, 20, 30)


#= Button ================================================
btn1 = gtk.Button("Button")
btn1.set_sensitive(False)
btn3 = gtk.Button(stock=gtk.STOCK_CLOSE)
btn4 = gtk.Button("Button")
btn4.set_size_request(80, 40)


#= tooltip ================================================
self.set_tooltip_text("Window widget")
#= from file ================================================
try:
    self.mincol = gtk.gdk.pixbuf_new_from_file("mincol.jpg")
except Exception, e:
    print e.message
    sys.exit(1)
#= label ================================================
label = gtk.Label(lyrics)
self.label.set_label(widget.get_active_text()) 


#= combo ================================================
cb = gtk.combo_box_new_text()
cb.connect("changed", self.on_changed)
cb.append_text('Ubuntu')
cb.append_text('Mandriva')
def on_changed(self, widget):
    self.label.set_label(widget.get_active_text()) 

#= Image ================================================
image = gtk.Image()
    image.set_from_file("redrock.png")


#= CheckButton ================================================
button = gtk.CheckButton("Show title")
button.set_active(True)
button.unset_flags(gtk.CAN_FOCUS)
button.connect("clicked", self.on_clicked)
widget.get_active()

#= Entry ================================================
entry = gtk.Entry()
entry.add_events(gtk.gdk.KEY_RELEASE_MASK)
entry.connect("key-release-event", self.on_key_release)
widget.get_text()   

#= DrawingArea ================================================
darea = gtk.DrawingArea()
darea.connect("expose-event", self.expose)
        

#= import ================================================
#= color ================================================
gtk.gdk.Color
colormap.alloc_color('red')
colormap.alloc_color('green')
colormap.alloc_color('blue')
colormap.alloc_color('blue')

#= pixfuf ================================================
gtk.gdk.Pixbuf
folderpb = gtk.gdk.pixbuf_from_file('folder.xpm')
filepb = gtk.gdk.pixbuf_from_file('file.xpm')










