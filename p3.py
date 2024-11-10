from functools import reduce

class Node(object):
    def __init__(self, v, n):
        self.value = v
        self.next = n


class LinkedList(object):
    def __init__(self):
        self.first = None
        self.length = 0


    def add(self, value):
        # add will insert at the begining of the list
        self.first = Node(value, self.first)
        self.length = self.length + 1


    def test(self, value):
        tmp_node = self.first
        result = False
        # Iterate through nodes in the linked list
        while tmp_node:
            # Complete the function with the following hints:
            # If the current node's value matches the query value, set result to True and break the loop.
            # Otherwise, move to the next node in the list.
            if tmp_node.value == value:
                result = True
                break
            else:
                tmp_node = tmp_node.next
        return result


    def remove(self, value):
        tmp_node = self.first
        prev_len = self.length
        prev_node = self.first
        # Iterate through nodes in the linked list
        while tmp_node:
            # Complete the function with the following hints:
            # Check if the current node's value matches the value to be removed.
            if tmp_node.value == value:
                # If found and it is the first node, update the head of the list.
                if tmp_node.next == self.first.next: # compare next ptr see if they are the same node
                    self.first = tmp_node.next
                # If found and it is not the first node, update the previous node's next to skip the current node.
                else:
                    prev_node.next = tmp_node.next
                self.length -= 1
                break
            else:
                prev_node = tmp_node
                tmp_node = tmp_node.next
        # If the node is removed, decrement the length of the list.
        if self.length == prev_len:
            return False
        else:
            return True


    def len(self): 
        # Complete the function with the following hint:
        # Return the current length of the linked list.
        return self.length


    def Lprint(self):
        print("Current linked list: ", end='')
        result = [] 
        tmp_node = self.first
        # Iterate through nodes in the linked list
        while tmp_node:
            # Complete the function with the following hints:
            # Append the current node's value to the result list.
            result.append(tmp_node.value)
            # Move to the next node.
            tmp_node = tmp_node.next
        # Append "none" to indicate the end of the list.
        result.append('none')
        # Print the linked list values in the standard format via result list.
        print(*result, sep='-->')

