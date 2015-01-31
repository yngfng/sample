
    drawingarea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(0, 0, 0))
    drawingarea.connect("expose-event", self.expose)

    glib.timeout_add(200, self.on_timer)
    def on_timer(self):
        self.queue_draw()
        return True
    
    dot = cairo.ImageSurface.create_from_png("dot.png")

        
        

    def expose(self, widget, event):
        cr = widget.window.cairo_create()
        cr.set_source_rgb(0, 0, 0)
        cr.paint()

        cr.set_source_surface(self.apple, self.apple_x, self.apple_y)
        cr.paint()

    def game_over(self, cr):
        (x, y, width, height, dx, dy) = cr.text_extents("Game Over")
        cr.set_source_rgb(65535, 65535, 65535)
        cr.move_to(w - width/2, h)
        cr.show_text("Game Over")
    
    def on_key_down(self, event): 
        key = event.keyval
        if key == gtk.keysyms.Left and not self.right: 
            self.left = True
class Snake(gtk.Window):

    def __init__(self):
        super(Snake, self).__init__()
        
        self.set_title('Snake')
        self.set_size_request(WIDTH, HEIGHT)
        self.set_resizable(False)
        #self.set_position(gtk.WIN_POS_CENTER)

        self.board = Board()
        self.connect("key-press-event", self.on_key_down)
        self.add(self.board)
        
        self.connect("destroy", gtk.main_quit)
        self.show_all()


    def on_key_down(self, widget, event): 
     
        key = event.keyval
        self.board.on_key_down(event)


Snake()
gtk.main()
