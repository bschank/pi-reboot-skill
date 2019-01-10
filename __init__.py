from mycroft import MycroftSkill, intent_file_handler


class PiReboot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('reboot.pi.intent')
    def handle_reboot_pi(self, message):
        self.speak_dialog('reboot.pi')


def create_skill():
    return PiReboot()

