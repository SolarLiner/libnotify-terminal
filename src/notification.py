import os
import subprocess
# Gtk imports
import gobject
import notify2 as Notify


class Notifier:
    def __init__(self, application_title, title, subtitle, body):
        if subtitle:
            body = subtitle+'\n'+body

        Notify.init(application_title)

        self.action_count = 0

        self.notification = Notify.Notification(
            title,
            body,
            "dialog-information"
        )
        self.data = None

    def show(self, timeout=3000):
        if timeout:
            self.notification.set_timeout(timeout)

        if Notify.is_initted():
            self.notification.show()
            if self.action_count > 0:
                gobject.timeout_add(timeout, lambda: os.sys.exit())
                gobject.MainLoop().run()
        else:
            os.sys.exit(2)

    def add_action(self, action, label):
        if self.action_count == 3:
            pass
        self.action_count += 1
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

    def on_closed(self):
        os.sys.exit()

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