import os
# Gtk imports
import notify2 as notify
import argparse
from gi.repository import GObject as gobject


class Notifier(object):
    def __init__(self, application_title, title, subtitle, body):
        if subtitle:
            body = subtitle+'\n'+body

        notify.init(application_title, mainloop='glib')

        self.action_count = 0

        self.notification = notify.Notification(
            title,
            body,
            "dialog-information"
        )
        self.data = None

    def show(self, timeout=5000):
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
            quit()
        elif action == 'reply':
            notification.close()
            title = "Reply to {0}".format(self.data['reply'])
            text = self.data['message']
            out = os.popen("zenity --entry '--title={0}' '--text={1}'".format(title, text)).read()
            print(out)
            quit()
        else:
            print(action)
            quit()


def main():
    args = get_args(os.sys.argv)
    n = Notifier(args.app_title, args.title, args.subtitle, args.body)

    if args.is_reply:
        n.add_reply_action("Reply", args.reply_to, args.message)
    for action in args.actions:
        assert isinstance(action, str)
        split_actions = action.split(',')
        assert len(split_actions) == 2
        id, label = split_actions
        n.add_action(id, label)

    n.show()


def get_args(args):
    parser = argparse.ArgumentParser(description='Fires notifications with callbacks from the command-line.')
    parser.add_argument_group(title='Notification')
    parser.add_argument('-b', '--body', dest='body', help='Notification body', required=True)
    parser.add_argument('--app-title', dest='app_title', nargs='?', help='Application title', default='libnotify-terminal')
    parser.add_argument('-t', '--title', dest='title', nargs='?', help='Notification title', default='Notification')
    parser.add_argument('-s', '--subtitle',
                        dest='subtitle',
                        nargs='?',
                        help='Notification subtitle (defined as the first line in the body, in bold)',
                        default=None
                        )
    parser.add_argument('--action',
                        dest='actions',
                        nargs='*',
                        help="Add action in the form {id},{label}, where label is the display name of the button. "
                            "When no actions are passed, %(prog)s returns directly. If an action has been specified, "
                            "it will wait for either timeout or callback. This is because on most (if not all) DEs, "
                            "after the notification has disappeared on-screen, if it can be found on a notification "
                            "tray, buttons will not be shown.",
                        default=[]
                        )
    parser.add_argument_group(title='Reply')
    parser.add_argument('-r', '--reply',
                        dest='is_reply',
                        nargs='?',
                        help='Flag notification as reply-able. This will internally use zenity to ask the user for a reply.',
                        action='store_true',
                        default=False
                        )
    parser.add_argument('--reply-to',
                        dest='reply_to',
                        nargs='?',
                        help='Recipient of the message to be sent. For display purposes only.',
                        default=None
                        )
    parser.add_argument('--reply-message',
                        dest='message',
                        nargs='?',
                        help='Original message. For display purposes only. Can be different than message body.',
                        default=None
                        )

    return parser.parse_args(args)


if __name__ == '__main__':
    main()
