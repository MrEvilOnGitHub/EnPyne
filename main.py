def __init__(self, renderer=False, physics=False, event_handler=False):
    if renderer:
        import renderer
    if physics:
        import physics
    if event_handler:
        import event_handler

def run():
    pass