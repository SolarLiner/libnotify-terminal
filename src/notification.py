import gi
import os
import subprocess
gi.require_version('Notify', '0.7')
gi.require_version('Gtk', '3.0')
from gi.repository import Notify, Gtk


class Notification:
    def __init__(self, application_title, title, subtitle, body):
        if subtitle:
            body = subtitle+'\n'+body

        Notify.init(application_title)

        self.notification = Notify.Notification.new(
            title,
            body,
            "dialog-information"
        )
        self.data = None

    def show(self, timeout=None):
        if timeout:
            self.notification.set_timeout(timeout)

        if Notify.is_initted():
            self.notification.show()
            Gtk.main()
        else:
            os.sys.exit(2)

    def add_action(self, action, label):
        self.notification.add_action(action, label, self.notification_callback)

    def add_close_action(self, label):
        self.add_action('close', label)

    def add_reply_action(self, label, reply_to, message):
        self.add_action('reply', label)
        self.set_category('im.recieved')
        self.data = {
            'reply': reply_to,
            'message': message
        }

    def set_category(self, category):
        self.notification.set_category(category)

    def notification_callback(self, notification, action, data=None):
        if action == 'close':
            notification.close()
            os.sys.exit(0)
        elif action == 'reply':
            notification.close()
            title = "Reply to {0}".format(self.data['reply'])
            text = self.data['message']
            out = os.popen("zenity --entry '--title={0}' '--text={1}'".format(title, text)).read()
            print out
            os.sys.exit(0)
        else:
            print action
            os.sys.exit(0)