from online_game import Player
import pytest
import pygame

def test_process_character_move():
    character_1 = Player(0, 0, 75, 100, (0, 50, 255))
    keyboard = {pygame.K_LEFT: 0,
                pygame.K_RIGHT: 0,
                pygame.K_UP: 0,
                pygame.K_DOWN: 0
            }
    
    save_position = character_1.rect
    
    character_1.process_character_move(keyboard)
    assert character_1.rect == save_position
    
    keyboard[pygame.K_LEFT] = 1
    character_1.process_character_move(keyboard)
    assert character_1.rect == (-6, 0, 75, 100)
    
    keyboard[pygame.K_LEFT] = 0
    
    keyboard[pygame.K_RIGHT] = 1
    character_1.process_character_move(keyboard)
    assert character_1.rect == (0, 0, 75, 100)
    
    keyboard[pygame.K_RIGHT] = 0
    
    keyboard[pygame.K_DOWN] = 1
    character_1.process_character_move(keyboard)
    assert character_1.rect == (0, 6, 75, 100)
    
    keyboard[pygame.K_DOWN] = 0
    
    keyboard[pygame.K_UP] = 1
    character_1.process_character_move(keyboard)
    assert character_1.rect == (0, 0, 75, 100)
    
    keyboard[pygame.K_UP] = 0
    
    keyboard[pygame.K_LEFT] = 1
    keyboard[pygame.K_UP] = 1
    character_1.process_character_move(keyboard)
    assert character_1.rect == (-6, -6, 75, 100)
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])