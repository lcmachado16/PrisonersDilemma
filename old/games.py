Games = { 
    'prisionersDilemmaRules': { 
        'name': 'Prisoners Dilemma Game',
        'actions': ['Cooperate', 'Defect'],
        'rewards': [[[1, 1], [20, 0]], [[0, 20], [10, 10]]]
    },
    'BattleOfSexes': { 
        'name': 'Battle Of Sexes',
        'actions': ['Ballet', 'Movie'],
        'rewards': [[[1, 4], [0, 0]], [[0, 0], [4, 1]]]
    },
    'rockScissorPaperRules': {
        'name': 'Rock Scissor Paper',
        'actions': ['Rock', 'Scissor', 'Paper'],
        'rewards': [
            [0, -1, 1], 
            [1, 0, -1],
            [-1, 1, 0]
        ]
    },
    'ParetoDominanceGameRules': {
        'name': 'Pareto Dominance Game',
        'actions': ['L', 'R'],
        'rewards': [
            [[9, 9], [0, 8]], 
            [[8, 0], [7, 7]]
        ]
    },
    'TwoFingerMorra': {
        'name': 'Two Finger Morra',
        'actions': ['One', 'Two'],
        'rewards': [
            [[2, -2], [3, -3]],
            [[3, -3], [2, -2]]
        ]
    }
}

# Test to print all game names
if __name__ == "__main__":
    for game_key in Games:
        print(Games[game_key]['name'])
