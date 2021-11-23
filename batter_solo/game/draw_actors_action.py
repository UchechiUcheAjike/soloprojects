from game.action import Action
from game.output_service import OutputService

class DrawActorsAction(Action):
    """A code template for drawing the actor's action. The responsibility of this class of objects is to draw the actor's action.
    
    Stereotype:
        Controller
    """
    def __init__(self, output_service):
        
        self.output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self.output_service.clear_screen()
        for i in cast.values():
            self.output_service.draw_actors(i)
        self.output_service.flush_buffer()