class GameEventHandler:
    def on_key_press(self, symbol, modifiers):
        print('Key pressed in game')
        return True

    def on_mouse_press(self, x, y, button, modifiers):
        print('Mouse button pressed in game')
        return True

game_handlers = GameEventHandler()

def start_game()
    window.push_handlers(game_handlers)

def stop_game()
    window.pop_handlers()