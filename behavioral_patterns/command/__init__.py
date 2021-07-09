from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Command):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"ComplexCommand: See, I can do complex things like printing"
              f"({self._payload})")


class Commander:
    set_simple_command = None
    set_complex_command = None
    """
    Initialize commands.
    """

    def init_simple_command(self, command: Command):
        self.set_simple_command = command

    def init_complex_command(self, command: Command):
        self.set_complex_command = command

    def execute_some_commands(self) -> None:
        print("Commander: Start doing simple command")
        self.set_simple_command.execute()

        print("Commander: Start doing complex command")
        self.set_complex_command.execute()


if __name__ == "__main__":
    commander = Commander()
    commander.init_simple_command(SimpleCommand(payload="This is a simple command"))
    commander.init_complex_command(ComplexCommand(payload="This is a complex command"))
    commander.execute_some_commands()
