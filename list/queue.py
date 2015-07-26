from collections import deque


def main():
  queue = deque(['Eric', 'J', 'H'])
  print queue
  queue.append('N')
  print queue
  print queue.popleft()
  print queue


if __name__ == "__main__":
  main()
