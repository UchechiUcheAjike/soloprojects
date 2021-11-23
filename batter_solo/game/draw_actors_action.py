from game.action import Action
from game.output_service import OutputService

class DrawActorsAction(Action):
    def __init__(self, output_service):
        self.output_service = output_service

    def execute(self, cast):
        self.output_service.clear_screen()
        for i in cast.values():
            self.output_service.draw_actors(i)
        self.output_service.flush_buffer()