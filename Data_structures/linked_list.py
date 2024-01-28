
class Node:                                       # 1. Создание класс узла

    def __init__(self, value, index):             # 1.1 Инициализация полей при инициализации классов

        self.value = value
        self.index = index                        # 1.1.1 Cоздание поля индекс экспереминательное, тк как несет дополнительную сложность в алгоритме
        self.next = None
        self.prev = None


class DoubleLinkedList:                           # 2. Создание класс Двустороннего Связного списка

    def __init__(self, value):                    # 2.1 Инициализация полей при инициализации классов

        self.head = Node(value, 0)                # 2.1.1 Голова списка указывает на новый узел создаваемый при создании экземпляра
        self.tail = self.head                     # 2.1.2 Хвост списка указыват на так же на голову, тк как узел является единственным
        self.length = 1                           # 2.1.3 Длина списка по умолчанию 1

    def append_node_Tail(self, value):            # 3 Метод при использовании которого новый узел добавляется в конец(хвост) списка

        new_index_node = self.tail.index + 1      # 3.1 Создаем новый индекс для нового узла от елемента который в находится в конце списка
        new_node = Node(value, new_index_node)    # 3.2 Создание нового узла и ссылки которая ссылается на новый узел
        new_node.prev = self.tail                 # 3.3 В новом узле обращаемся к ссылку на предыдущий элемент который является None изменяем ссылку на конец списка тем самым делаем связь prev
        self.tail.next = new_node                 # 3.4 Так как Хвост списка еще на предыдущем элементе до нового, делаем ссылку next на новый элемент 
        self.tail = new_node                      # 3.5 Ссылку хвоста списка переопределяем на новый элемент
        self.length += 1                          # 3.6 Длину списка увеливаем на 1

    def append_node_Head(self, value):            # 4 Создание метода при использовании которого новый узел добавляется в Голову (Начало) нашего списка
        new_index_node = 0                        # 4.1 По умолчанию индекс создаваемого узла равняется 0
        current = self.head                       # 4.2 Текущи

        while current is not None:                # 4.3 Создание цикла который увеличвает каждый индекс элемента на 1
            current.index += 1
            current = current.next

        new_node = Node(value, new_index_node)    # 4.4 Создание ссылки и нового узла
        new_node.next = self.head                 # 4.5 Изменение ссылки на следующий узел на узел который был 1 элементом
        self.head = new_node                      # 4.6 Изменение ссылки Головы на новый узел
        self.length += 1
 
    def take_value_use_index(self, incoming_index):  # 5 Создание метода который берет значение по индексу
        current = self.head                          
        while current is not None:

            if current.index == incoming_index:
                return current.value
            current = current.next

        return -1

    def print_all_list(self):
        current = self.head
        print(self.head.prev)
        while current is not None:
            print(current.value)
            current = current.next
        print(self.tail.next)

    def return_array(self):
        current = self.head
        array = []
        while current is not None:
            array.append(current.value)
            current = current.next
        return array


user_linked_list = DoubleLinkedList(0)
user_linked_list.append_node_Head(25)
user_linked_list.append_node_Tail(100)


user_linked_list.print_all_list()
array_from_ll = user_linked_list.return_array()

value = user_linked_list.take_value_use_index(3)
print(value)
