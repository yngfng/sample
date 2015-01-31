#! /usr/bin/env python


#= import ================================================
import pygtk
pygtk.require('2.0')
import gtk

#= window ================================================
window = [None] * 3
window = gtk.Window(gtk.WINDOW_TOPLEVEL)
window.set_title("URL Cache")
window.set_size_request(200, 200)
window.connect("delete_event", lambda wid: gtk.main_quit())
window.connect("delete_event", delete_event)
window.add(widget)
window.show_all()
#- delete event -
def delete_event(self, widget, event, data=None):
    gtk.main_quit()
    return False

#= treeview ================================================
#- drag and drop -------------------------------------------
self.treeview.enable_model_drag_source( gtk.gdk.BUTTON1_MASK,
                                        self.TARGETS,
                                        gtk.gdk.ACTION_DEFAULT|
                                        gtk.gdk.ACTION_MOVE)
self.treeview.enable_model_drag_dest(self.TARGETS,
                                     gtk.gdk.ACTION_DEFAULT)

self.treeview.connect("drag_data_get", self.drag_data_get_data)
self.treeview.connect("drag_data_received",
                      self.drag_data_received_data)

def drag_data_get_data(self, treeview, context, selection, target_id,
                       etime):
    treeselection = treeview.get_selection()
    model, iter = treeselection.get_selected()
    data = model.get_value(iter, 0)
    selection.set(selection.target, 8, data)

def drag_data_received_data(self, treeview, context, x, y, selection,
                            info, etime):
    model = treeview.get_model()
    data = selection.data
    drop_info = treeview.get_dest_row_at_pos(x, y)
    if drop_info:
        path, position = drop_info
        iter = model.get_iter(path)
        if (position == gtk.TREE_VIEW_DROP_BEFORE
            or position == gtk.TREE_VIEW_DROP_INTO_OR_BEFORE):
            model.insert_before(iter, [data])
        else:
            model.insert_after(iter, [data])
    else:
        model.append([data])
    if context.action == gtk.gdk.ACTION_MOVE:
        context.finish(True, True, etime)
    return

#- treeview -------------------------------------------
treeview = gtk.TreeView(liststore)
treeview.append_column(column)
treeview.set_search_column(0)
treeview.set_reorderable(True)
    #- liststore -------------------------------------------
    bugdata="""120595 NEW Custom GtkTreeModelFilter wrappers need
    121339 RESO dsextras.py installation directory is incorrect
    121611 RESO argument is guint, should be guint32"""
    for line in bugdata.split('\n'):
        l = line.split()
        self.liststore.append([int(l[0]), l[1], ' '.join(l[2:])])

    self.liststore = gtk.ListStore(int, str, str)
    self.b0.connect_object('clicked', gtk.ListStore.clear, self.liststore)
    #- sort model -------------------------------------------
    sortmodel = gtk.TreeModelSort(liststore)
    sortmodel.set_sort_column_id(n, gtk.SORT_ASCENDING)
    treeview = gtk.TreeView(win.sortmodel)
    #- filter model -------------------------------------------
    modelfilter = liststore.filter_new()
    modelfilter.refilter()
    modelfilter.set_visible_func(self.visible_cb, self.show_states)
    def visible_cb(self, model, iter, data):
        return model.get_value(iter, 1) in data
    #- treestore -------------------------------------------
    liststore = ListStore(gtk.gdk.Pixbuf, int, str, 'gboolean')
    treestore = TreeStore(gtk.gdk.Pixbuf, int, str, 'gboolean')
    treeiter = store.get_iter(path)
    treeiter = store.get_iter_first()
    treeiter = store.iter_next(iter)
    treeiter = treestore.iter_children(parent)
    treeiter = treestore.iter_nth_child(parent, n)
    treeiter = treestore.iter_parent(child)
    path = store.get_path(iter)
    treerowref = TreeRowReference(model, path)
    iter = append(parent, row=None)
    iter = prepend(parent, row=None)
    iter = insert(parent, position, row=None)
    iter = insert_before(parent, sibling, row=None)
    iter = insert_after(parent, sibling, row=None)
  result = treestore.remove(iter)
  treestore.clear()
    #- treeviewcolumn -------------------------------------------
    column = gtk.TreeViewColumn('URL', self.cell, text=0)
    column.set_title("Programming languages")
    column.pack_start(cell, True)
    column.set_attributes(cell, text=i)
    column.add_attribute(cell, 'text', 0)
    column.set_sort_column_id(i)
        #- cellranderertext -------------------------------------------
        cell = gtk.CellRendererText()
        #- cellranderertoggle -------------------------------------------
