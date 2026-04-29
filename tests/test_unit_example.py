def get_filtered_items(items, keyword):
    return [item for item in items if keyword.lower() in item.lower()]


def test_get_filtered_items_returns_matches():
    items = ["apple", "banana", "apricot", "cherry"]
    result = get_filtered_items(items, "ap")
    assert result == ["apple", "apricot"]


def test_get_filtered_items_empty_list():
    assert get_filtered_items([], "apple") == []


def test_get_filtered_items_no_match():
    assert get_filtered_items(["banana", "cherry"], "ap") == []
