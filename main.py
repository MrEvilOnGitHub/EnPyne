def __init__(self, renderer=False, physics=False, event_handler=False):
    if renderer:
        import renderer
    if physics:
        import definitions
    if event_handler:
        import event_handler

def run():
    pass