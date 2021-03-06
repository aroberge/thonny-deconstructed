""" Helper view for Thonny developers
"""

from ynnoht import get_workbench
from ynnoht.tktextext import TextFrame
from ynnoht.common import DebuggerResponse


class EventsView(TextFrame):
    def __init__(self, master):
        TextFrame.__init__(self, master)
        # self.text.config(wrap=tk.WORD)
        get_workbench().bind("ShowView", self._log_event, True)
        get_workbench().bind("HideView", self._log_event, True)
        get_workbench().bind("ToplevelReponse", self._log_event, True)
        get_workbench().bind("DebuggerResponse", self._log_event, True)
        get_workbench().bind("ProgramOutput", self._log_event, True)
        get_workbench().bind("InputRequest", self._log_event, True)

    def _log_event(self, event):
        self.text.insert("end", event.sequence + "\n")
        for name in dir(event):
            if name not in ["sequence", "setdefault", "update"] and not name.startswith("_"):
                self.text.insert(
                    "end", "    " + name + ": " + repr(getattr(event, name))[:100] + "\n"
                )

        if isinstance(event, DebuggerResponse):
            frame = event.stack[-1]
            self.text.insert("end", "    " + "event" + ": " + frame.event + "\n")
            self.text.insert("end", "    " + "focus" + ": " + str(frame.focus) + "\n")

        self.text.see("end")


def load_plugin() -> None:
    if get_workbench().get_option("general.debug_mode"):
        get_workbench().add_view(EventsView, _("Events"), "se")
