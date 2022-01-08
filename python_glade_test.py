import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
 
def entry_focus_in(entry, event):
     stylecontext = entry.get_style_context()
     stylecontext.add_class("borderentry")
     stylecontext.remove_class("noborderentry")
 
def entry_focus_out(entry, event):
     stylecontext = entry.get_style_context()
     stylecontext.add_class("noborderentry")
     stylecontext.remove_class("borderentry")
 
if __name__ == '__main__':
     builder = Gtk.Builder()
     builder.add_from_file("python_glade_test.glade")
     window = builder.get_object("mainframe")
     css_provider = Gtk.CssProvider()
     css_provider.load_from_path('style.css')
     Gtk.StyleContext.add_provider_for_screen(
         window.get_screen(),
         css_provider,
         Gtk.STYLE_PROVIDER_PRIORITY_USER)
 
     entry1 = builder.get_object("entry1")
     entry1.connect("focus-in-event", entry_focus_in)
     entry1.connect("focus-out-event", entry_focus_out)
     entry2 = builder.get_object("entry2")
     entry2.connect("focus-in-event", entry_focus_in)
     entry2.connect("focus-out-event", entry_focus_out)
     entry3 = builder.get_object("entry3")
     entry3.connect("focus-in-event", entry_focus_in)
     entry3.connect("focus-out-event", entry_focus_out)
     window.show_all()
     Gtk.main()
