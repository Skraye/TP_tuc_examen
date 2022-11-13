import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

with open('../resources/draw.json', encoding='utf-8') as draw:
    draw_data = json.load(draw)
response_draw_data = {"winner": "draw"}

with open('../resources/poke1_win.json', encoding='utf-8') as poke1:
    poke1_data = json.load(poke1)
response_win1_data = {"winner": "1"}

with open('../resources/poke2_win.json', encoding='utf-8') as poke2:
    poke2_data = json.load(poke2)
response_win2_data = {"winner": "2"}

def test_battle_draw_should_respond_with_200_and_draw():
    """
        Unitary test for battle resulting in a draw
    """
    #Given/When
    response = client.post(
            "/battle/1/2",
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            draw_data= json.dumps(draw_data))    
    #Then
    assert response.status_code == 200
    assert response.json() == response_draw_data

def test_battle_win_poke1_should_respond_with_200_and_win_poke1():
    """
        Unitary test for battle resulting in a win for player 1
    """
    #Given/When
    response = client.post(
            "/battle/1/2",
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            draw_data= json.dumps(draw_data))
        #Then
    assert response.status_code == 200
    assert response.json() == response_win1_data

def test_battle_win_poke2_should_respond_with_200_and_win_poke2():
    """
        Unitary test for battle resulting in a win for player 1
    """
    #Given/When
    response = client.post(
            "/battle/1/2",
            headers={'accept': 'application/json', 'Content-Type': 'application/json'},
            draw_data= json.dumps(draw_data))
    #Then
    assert response.status_code == 200
    assert response.json() == response_win2_data
