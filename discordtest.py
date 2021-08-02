# Prepare imports
import gi
import discord_rpc
import time
import rpcloop

# Enforce minimum GTK version
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Definte Rich Presence settings
def readyCallback(current_user):
    print('Our user: {}'.format(current_user))

def disconnectedCallback(codeno, codemsg):
    print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
        codeno, codemsg
    ))

def errorCallback(errno, errmsg):
    print('An error occurred! Error {}: {}'.format(
        errno, errmsg
    ))

def set_presence(token, str1, str2, str3):
    # Note: 'event_name': callback
    callbacks = {
        'ready': readyCallback,
        'disconnected': disconnectedCallback,
        'error': errorCallback,
    }    

    discord_rpc.initialize(token, callbacks=callbacks, log=False)
    discord_rpc.update_presence(
        **{
            str1,
            str2,
            str3
        }
    )


# Establish handler functions
class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()
        discord_rpc.shutdown()

    def onLoginButtonPress(self, button):
        window.hide()
        self.userToken = tokentry.get_text()

        window2 = builder.get_object("window2")
        window2.show_all()

    def on_token_get(self, widget):
        print("Done!")

    def onPresenceSet(self, button):
        set_presence(self.userToken, "testing", "is this real", "wat")

# Build using glade file found in dir
builder = Gtk.Builder()
builder.add_from_file("discordrpc.glade")
builder.connect_signals(Handler())

# Show windows
window = builder.get_object("window1")
tokentry = builder.get_object("tokentry")
window.show_all()

# Execute main Glade loop
Gtk.main()
