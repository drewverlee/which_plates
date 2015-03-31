

def test_enqueue(priority_queue, mock_item_one):
    priority_queue.enqueue(mock_item_one)
    assert priority_queue == [(mock_item_one.priority(), mock_item_one)]

def test_deque(priority_queue_with_items, mock_item_one):
    item = priority_queue_with_items.deque()
    assert item == mock_item_one


