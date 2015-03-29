

def test_enqueue(priority_que, mock_item_one):
    priority_que.enqueue(mock_item_one)
    assert priority_que == [(mock_item_one.priority(), mock_item_one)]

def test_deque(priority_que_with_items, mock_item_one):
    item = priority_que_with_items.deque()
    assert item == mock_item_one


