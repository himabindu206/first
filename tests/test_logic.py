from logic import add_task, delete_task, complete_task


def test_add_task():
    tasks = []
    tasks = add_task(tasks, "Study")
    assert len(tasks) == 1


def test_delete_task():
    tasks = [{"task": "Study", "done": False}]
    tasks = delete_task(tasks, 0)
    assert tasks == []


def test_complete_task():
    tasks = [{"task": "Study", "done": False}]
    tasks = complete_task(tasks, 0)
    assert tasks[0]["done"] is True