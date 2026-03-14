class Node:
  def __init__(self,data):
    self.data = data  # data는 값을 가리키는 변수(속성, attribute)
    self.next = None  # next는 다음 노드를 가리키는 변수

class LinkedList:
  def __init__(self):
    self.head = None
    self.length = 0
  
  def __len__(self):
    return self.length

  def appendleft(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      node = Node(data)
      node.next = self.head
      self.head = node
    self.length += 1

  def append(self, data):
    if self.head is None:
      self.head = Node(data)
    else:
      node = self.head
      while node.next is not None:
        node = node.next
      node.next = Node(data)
    self.length += 1

  def __str__(self):
    if self.head is None:
      return "Linked lisy is empty!"
    res = "Head"
    node = self.head
    while node is not None:
      res += " -> " + str(node.data)
      node = node.next 
    return res

if __name__ == "__main__":
  my_list = LinkedList()
  print(f"연결 리스트 생성. 연결 리스트의 길이 = {len(my_list)}")
  print(my_list)
  print()
  for i in range(4):
    if i % 2:
      my_list.append(i)
    else:
      my_list.appendleft(i)
    print(f"{i}를 추가. 연결 리스트의 길이 = {len(my_list)}")
    print(my_list)
    print()