import os
# Gtk imports
import gobject
import notify2 as notify


class Notifier(object):
    def __init__(self, application_title, title, subtitle, body):
        if subtitle:
            body = subtitle+'\n'+body

        notify.init(application_title)

        self.action_count = 0

        self.notification = notify.Notification(
            title,
            body,
            "dialog-information"
        )
        self.data = None

    def show(self, timeout=5000):
        if timeout:
            self.notification.set_timeout(timeout)

        if notify.is_initted():
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
            print(out)
            os.sys.exit(0)
        else:
            print(action)
            os.sys.exit(0)


def main():
    app_title = "libnotify-terminal"
    title = "Notification"
    subtitle = None
    body = None
    actions = []
    is_reply = False
    reply_to = "the message"
    message = "Reply to the receieved message"

    args = os.sys.argv

    if len(args) < 3:
        os.sys.exit(-1)

    for i in range(1, len(args)):
        if args[i] == "--app-title":
            app_title = args[i+1]
        elif args[i] == "--title":
            title = args[i+1]
        elif args[i] == "--subtitle":
            subtitle = args[i+1]
        elif args[i] == "--body":
            body = args[i+1]
        elif args[i] == "--action":
            action = args[i+1].split(',')
            actions.append({
                'name': action[0],
                'label': action[1]
            })
        elif args[i] == "--reply":
            is_reply = True
        elif args[i] == "--reply-to":
            reply_to = args[i+1]
        elif args[i] == "--reply-message":
            message = args[i+1]
        else:
            pass

    if not body:
        os.sys.stderr.write("{0} needs a body.".format(args[0]))
        os.sys.exit(-1)

    n = Notifier(app_title, title, subtitle, body)

    if is_reply:
        n.add_reply_action("Reply", reply_to, message)
    for action in actions:
        n.add_action(action['name'], action['label'])

    n.show()


if __name__ == '__main__':
    main()
