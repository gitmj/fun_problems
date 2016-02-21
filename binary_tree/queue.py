class Queue():
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []
  
  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    if (self.isEmpty()):
      return None
    return self.items.pop()
  
  def size(self):
    return len(self.items)
  


def main():
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
  
    print queue.dequeue()
    print queue.dequeue()
    queue.enqueue(5)
    print queue.dequeue()
    print queue.dequeue()
    print queue.dequeue()

if __name__ == "__main__":
    main()
