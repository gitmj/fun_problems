class Queue():
  def __init__(self, data):
    self.front = None
    self.back = None
    self.data = data

  # return new back of queue.
  def put(self, data):
    node = self
    # Get to the back of queue.
    while node.back != None:
      node = node.back
    node.back = Queue(data);
    node.back.front = node;
    return node.back

  def get(self):
    if (self == None):
      return None
    # get to the front
    while self.front != None: 
      self = self.front

    if (self.back != None):
      self.back.front = None

    return self.data

  def walk(self):
    node = self
    # go to the back and start walking towards front
    while node.back != None:
      node = node.back

    # now print and walk towards front
    while node.front != None:
      print node.data
      node = node.front

    print node.data



def main():
    queue = Queue(1)
    queue = queue.put(2)
    queue = queue.put(3)
    queue = queue.put(4)
  
    print 'walk the queue'
    queue.walk()
    print 'front of queue'
    print queue.get()
    print 'front of queue'
    print queue.get()
    print 'walk the queue'
    queue.walk()

if __name__ == "__main__":
    main()
