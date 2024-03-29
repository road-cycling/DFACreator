
import numpy as np
from numpy import linalg as LA

def main():
    userInput = int(input('Enter 1 for Problem 1, or 2 for Problem 2 '))

    if userInput == 1:
        power = int(input('n = '))
        print(problem1(power))
    elif userInput == 2:
        k = int(input('Input K: '))
        inputArray = input('Input numbers separated by spaces ex: "1 2 4 5" ').split(' ')
        numArray = [int(num) for num in inputArray]
        print(bfs(createArray(numArray, k), 0, numArray))

    else:
        print(userInput)
        print('Error!')


def problem1(power):

    array = np.array([

        # []
        [0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]], dtype=object)

    newMatrix = LA.matrix_power(array, power)

    start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=object)

    accepting = np.array([
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [0],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1],
                [1]


    ], dtype=object)
    finalMatrix = start.dot(newMatrix).dot(accepting)
    return finalMatrix[0]

def Pop(queue):
    item = queue[0]
    del queue[0]
    return item

def Push(queue, item):

    queue.append(item)
    return queue

def bfs(state_transition_table, start_state, alphabet):

    #[print(a) for a in state_transition_table]
    #quit()
    edge_input = {i:letter for i, letter in enumerate(alphabet)}
    #[print(i, edge_input[i]) for i in edge_input.keys()]
    visited = [0] * len(state_transition_table)
    sequences_found_so_far = [(-1, -1)] * len(state_transition_table)
    queue = []
    #print(visited)
    visited[start_state] = 1
    queue = Push(queue, start_state)
    k = 0
    while (queue != []):
        current_remainder = Pop(queue)
        #print('current state', current_remainder)
        #print(state_transition_table[current_remainder])
        #print('next states')
        #print(state_transition_table[current_remainder])
        #print('tuple next states')
        #print([(i, next_remainder) for i, next_remainder in enumerate(state_transition_table[current_remainder]) if i > 0])
        next_remainders = [(edge_input[i], NextRemainder) for i, NextRemainder in enumerate(state_transition_table[current_remainder])]
        #print(next_remainders)

        # also need the edge input value
        for y in next_remainders:
            #print(y)
            # current state could be 0 and one of the next states could be 0
            #i = y[0]
            #next_remainder = y[1]
            #print(k)
            (letter, next_remainder) = y
            #print(k, next_remainder)

            # for catching input where there is no solution
            state_changed = False
            if visited[next_remainder] == 0:
                # they are all new so this happens for all neighbors
                #print(edge_input[i])

                visited[next_remainder] = 1

                sequences_found_so_far[next_remainder] = (current_remainder, letter)
                #print(next_remainder, current_remainder, sequences_found_so_far[next_remainder])

                queue = Push(queue, next_remainder)
            # 0 is an accepting state
            if next_remainder == 0:
                # what happens if current state = 0?
                #print(current_remainder)
                # need the last link so the recovery process can start on the last character found
                sequences_found_so_far[next_remainder] = (current_remainder, letter)
                #print(next_remainder, current_remainder, sequences_found_so_far[next_remainder])

                #print('done')
                #print(sequences_found_so_far, current_remainder, next_remainder)
                #exit()
                print()
                # traverse sequences_found_so_far backwards to recover the string

                return recover(sequences_found_so_far, next_remainder)
            #print(sequences_found_so_far)
            k += 1
            '''
            if k == 100:
                print()
                filtered = [(i ,j) for i, j in sequences_found_so_far if i != -1 and j != -1]
                [print('current_remainder', i, 'letter', j) for i, j in filtered]

                exit()
            '''
        #print()


def recover(sequences_found_so_far, next_remainder):
    # 31333
    # reversed = 33313
    # 33313 % 7 = 0
    # tested on alphabet = {1, 3, 5}
    # gives back 553
    # 553 % 7 = 0
    sequence = []
    # this sets prev_state as the current_remainder > 0
    (prev_state, input_index) = sequences_found_so_far[next_remainder]

    #print((prev_state, input_index))
    sequence.insert(0, str(input_index))
    while prev_state != 0:
        (prev_state, input_index) = sequences_found_so_far[prev_state]
        #print((prev_state, input_index))

        sequence.insert(0, str(input_index))
        #print(sequence)

    return ''.join(sequence)





# 2
def createArray(alphabet, n):

  # next states are remainders
  # can't visit enough of graph if the remainders never reach 26147
  # can use 10 with 7 because
  # remainder for order
  # make remainder using the remainders from k, each letter in the alphabet
  # why does it travel down the wrong path?
  return [ [ ( remainder * 10 + letter ) % n for letter in alphabet ] for remainder in range(n) ]

#print(bfs(createArray([1, 3], 26147), 0))
# gives an infinite loop
# maybe the test cases have no solutions
# case 2 : Input: k = 198217, Digits permitted: 1
#alphabet = [1]
#print(bfs(createArray(alphabet, 198217), 0, alphabet))
# works: eactly 10962 1's
#alphabet = [1,3]
#print(bfs(createArray(alphabet, 26147), 0, alphabet))


#node = {'input_digit': 0, 'prev_digit': }
# find shortest path
'''
def manyBFS(graph, start_vertex, verticies):

  # make a multiway tree in with reverse edges only
  # this allows backward traversal to the root to collect the input digits
  # makes all paths at the same time

  root = {'input_digit': 'null', 'prev_digit': 'null'}

  tree = [root]
'''
'''
>>> for i, letter in enumerate(['a', 'b', 'c']):
...    print(i, letter)
...
0 a
1 b
2 c
>>>
'''
'''
  next_remainders = [i for i in enumerate(verticies)]
  roots = [root]
  current_level = []
  i = 0
  current_vertex = 0
  new_set_of_next_remainders = []
    next_set_of_roots = []
    while i < len(roots):
      for current_vertex in current_level:
        next_remainders = []
        for j, next_remainder in enumerate(verticies[current_vertex]):
          # if next_remainder == 0
            # stop loops and return the dict representing the next item to add to the path
          tree.append({'input_digit': j, 'prev_digit' : roots[i]})
          next_set_of_roots.append({'input_digit': j, 'prev_digit' : roots[i]})
          next_remainders.append(next_remainder)
        # reset roots with new_set_of_roots for connecting to next level of items
        current_level.append(next_remainder)
        #new_set_of_next_remainders.append((verticies[next_remainders[i]]), )
      i += 1


'''
# another function
# start at last path
# traverse using the reference to the next dict
# collect the input digits in reverse using a list
# ''.join(list_name) = answer to problem

# small example
#table = createArray([1, 3], 7)
#[print(i, row) for i, row in enumerate(table)]
#manyBFS(table, 0, table)
#print(1113 % 7)


if __name__ == '__main__':
    main()
