# function for checking if an instance has collided with any objects
def collision_detector(objects, instance):
    for graphic in objects:
        if instance.x + instance.width > graphic.x and instance.x < graphic.x + graphic.width:
            if instance.y + instance.height > graphic.y and instance.y < graphic.y + graphic.height:
                instance.collision(graphic)
