import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0]
        paddle = cast["paddle"][0]
        bricks = cast["brick"]
        score = cast["score"][0]

        # paddle/ball collision
        if  ( ball.get_position().get_y() == paddle.get_position().get_y() ):

            if ( ( ball.get_position().get_x() >= paddle.get_position().get_x() )
            and ( ball.get_position().get_x() < paddle.get_position().get_x() + 10 ) ):
                velocity = Point( random.randint(-1, 1), ball.get_velocity().reverse().get_y() )
                ball.set_velocity(velocity)
            
            # game over
            else:
                sys.exit()

        # ball/brick collision
        for brick in bricks:
            if (ball.get_position().equals( brick.get_position() ) 
             or ( (ball.get_position().get_x() == brick.get_position().get_x() + 1 ) 
              and  (ball.get_position().get_y() == brick.get_position().get_y()    ) ) ):
                velocity = Point( random.randint(-1, 1), ball.get_velocity().reverse().get_y() )
                ball.set_velocity(velocity)
                brick.set_text("")
                brick.set_position(Point(0, 0))

                score.add_points(1)

        # ball/top of screen collision
        if ball.get_position().get_y() == 1:
            velocity = Point( random.randint(-1, 1), ball.get_velocity().reverse().get_y() )
            ball.set_velocity(velocity)

        # ball/right wall collision
        if ball.get_position().get_x() == constants.MAX_X:
            velocity = Point( ball.get_velocity().reverse().get_x(), ball.get_velocity().get_y() )
            ball.set_velocity(velocity)

        # ball/left wall collision
        if ball.get_position().get_x() == 0:
            velocity = Point( ball.get_velocity().reverse().get_x(), ball.get_velocity().get_y() )
            ball.set_velocity(velocity)