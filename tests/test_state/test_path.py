

def test_state_5(state_5):
    assert state_5.path() == [
        # action , plates
        (''      , [])    , # state 0
        ('+'     , [20])  , # state 1
        ('l'     , [20])  , # state 2
        ('-'     , [20])  , # state 3
        ('+'     , [25])  , # state 4
        ('l'     , [25])  , # state 3
        ]

# a true integration test
def test_state_finish(a_star_search_with_state_start):
    assert a_star_search_with_state_start.path() == [
        # action  , plates
        (''       , [])     ,
        ('+'      , [20])    ,
        ('l'      , [20])    ,
        ('-'      , [20])    ,
        ('+'      , [25])    ,
        ('l'      , [25])    ,
        ('+'      , [15])    ,
        ('l'      , [25, 15])    ,
        ]
