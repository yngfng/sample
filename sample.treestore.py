treestore = TreeStore(gtk.gdk.Pixbuf, int, str, 'gboolean')
# path iter
path = store.get_path(iter)
treeiter = store.get_iter(path)
treeiter = store.get_iter_first()
treeiter = store.iter_next(iter)
treeiter = treestore.iter_children(parent)
treeiter = treestore.iter_nth_child(parent, n)
treeiter = treestore.iter_parent(child)
treerowref = TreeRowReference(model, path)
# add iter
iter = append(parent, row=None)
iter = prepend(parent, row=None)
iter = insert(parent, position, row=None)
iter = insert_before(parent, sibling, row=None)
iter = insert_after(parent, sibling, row=None)
# remove iter
result = treestore.remove(iter)
treestore.clear()
# value get set
value = store.get_value(iter, column)
values = store.get(iter, column, ...)
val0, val2 = store.get(iter, 0, 2)
store.set_value(iter, column, value)
store.set(iter, ...)
store.set(iter, 0, 'Foo', 5, 'Bar', 1, 123)
# order
treestore.swap(a, b)
treestore.move_after(iter, position)
treestore.move_before(iter, position)
treestore.reorder(parent, new_order)
# func
def move_child_rows(treestore, from_parent, to_parent):
  n_columns = treestore.get_n_columns()
  iter = treestore.iter_children(from_parent)
  while iter:
    values = treestore.get(iter, *range(n_columns))
    treestore.remove(iter)
    treestore.append(to_parent, values)
    iter = treestore.iter_children(from_parent)
  return
store.foreach(func, user_data)
def func(model, path, iter, user_data):
...
# match if the value in the first column is >= the passed in value
# data is a tuple containing the match value and a list to save paths
def match_value_cb(model, path, iter, data):
  if model.get_value(iter, 0) >= data[0]:
    data[1].append(path)
  return False     # keep the foreach going
pathlist = []
treestore.foreach(match_value_cb, (10, pathlist))
# foreach works in a depth first fashion
pathlist.reverse()
for path in pathlist:
  treestore.remove(treestore.get_iter(path))
...
 treestore = TreeStore(str)
 ...
 def match_func(model, iter, data):
     column, key = data # data is a tuple containing column number, key
     value = model.get_value(iter, column)
     return value == key
 def search(model, iter, func, data):
     while iter:
         if func(model, iter, data):
             return iter
         result = search(model, model.iter_children(iter), func, data)
         if result: return result
         iter = model.iter_next(iter)
     return None
 ...
 match_iter = search(treestore, treestore.iter_children(None), 
                     match_func, (0, 'foo'))
...
liststore = gtk.ListStore(str, str)
...
# add some rows to liststore
...
# for looping
for row in liststore:
    # do individual row processing
...
# list comprehension returning a list of values in the first column
values = [ r[0] for r in liststore ]
...
row = model[0]
row = model['0']
row = model["0"]
row = model[(0,)]
i = model.get_iter(0)
row = model[i]
del model[(0,0)]
...
liststore = gtk.ListStore(str, int, object)
...
liststore[0] = ['Button', 23, gtk.Button('Label')]
...
liststore = gtk.ListStore(str, int)
liststore.append(['Random string', 514])
...
row = liststore[0]
value1 = row[1]
value0 = liststore['0'][0]
for value in row:
    print value
val0, val1 = row
...
 treestore = TreeStore(str)
 ...
 def match_func(row, data):
     column, key = data # data is a tuple containing column number, key
     return row[column] == key
 ...
 def search(rows, func, data):
     if not rows: return None
     for row in rows:
         if func(row, data):
             return row
         result = search(row.iterchildren(), func, data)
         if result: return result
     return None
 ...
 match_row = search(treestore, match_func, (0, 'foo'))
treestore[(1,0,1)][1] = 'abc'
treestore.append(parent, ['qwe', 'asd', 123])
treesortable.set_sort_func(sort_column_id, sort_func, user_data=None)
def sort_func_function(model, iter1, iter2, data)
def sort_func_method(self, model, iter1, iter2, data)
treesortable.set_sort_column_id(sort_column_id, order)
treesortable.set_default_sort_func(sort_func, user_data=None)
result = treesortable.has_default_sort_func()

