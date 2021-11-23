from game.action import Action
from game.output_service import OutputService

class DrawActorsAction(Action):
     """A code template for drawing the actor's action. The responsibility of this class of objects is to draw actions of the actor.
    
    Stereotype:
        Controller
    """
    def __init__(self, output_service):
        self.output_service = output_service
        """outputs services of the actor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

    def execute(self, cast):
        self.output_service.clear_screen()
        for i in cast.values():
            self.output_service.draw_actors(i)
        self.output_service.flush_buffer()
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """