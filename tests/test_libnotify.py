import src.libnotify_terminal as notify

class TestLibnotifyTerminal(object):
    n = notify.Notifier("Application", "Title", "Subtitle", "Body")

    def test_notification_created(self):
        assert self.n.notification is not None

    def test_add_action(self):
        count = self.n.action_count

        self.n.add_action("action", "label")
        assert self.n.action_count == count+1

    def test_add_reply(self):
        count = self.n.action_count

        self.n.add_reply_action("label", "Ali Connors", "Message")
        assert self.n.action_count == count+1
        assert self.n.data == {
            'reply': "Ali Connors",
            'message': "Message"
        }

    def test_notification_callback(self, capsys):
        self.n.notification_callback(self.n, "action")
        out, err = capsys.readouterr()

        assert out == "action"