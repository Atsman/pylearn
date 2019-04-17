import unittest
from queues.queue import Queue


class TestQueue(unittest.TestCase):
    def test_queue(self):
        queue = Queue()
        queue.enqueue(1)
        self.assertEqual(1, queue.dequeue())

        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
