import os
import notification


def main():
    app_title = "libnotify-terminal"
    title = "A notification"
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

    n = notification.Notifier(app_title, title, subtitle, body)

    if is_reply:
        n.add_reply_action("Reply", reply_to, message)
    for action in actions:
        n.add_action(action['name'], action['label'])

    n.show()


if __name__ == '__main__':
    main()
