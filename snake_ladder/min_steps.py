'''
Assuming N * N board
Dice 6 faced dice
User has the ability to control the dice to
  get required value

Input:

The value N is provided in the first line
The number of snakes is provided in second line
The snakes positions in provided in subsequent lines
The number of ladders is provided in next line
followed by each ladder position in subsequent line

Output:

Minimum number of steps to win the game.
-1 if not possible


Sample Input:
6
2
35 11
21 6
2
3 22
18 29

Sample Output:

'''

test_data = '''6
2
35 11
21 6
2
3 22
18 29
'''

class QueueEntry:

    def __init__(self, vertex=0, dist=0):
        self.vertex = vertex
        self.dist = dist

    def __repr__(self):
        return "({},{})".format(self.vertex, self.dist)

def find_min_steps(snakes, ladders, N):

    board_size = N * N
    dice = 6
    board = [-1] * board_size
    for snake in snakes:
        board[snake[0]-1] = snake[1]-1
    for ladder in ladders:
        board[ladder[0]-1] = ladder[1]-1

    #print board
    visited = [False] * board_size

    # Mark first vertex as visited
    visited[0] = True
    queue = []

    queue.append(QueueEntry(0,0))
    qe = QueueEntry()
    while queue:

        #print queue
        #print visited
        qe = queue.pop(0)

        if qe.vertex == board_size-1:
            return qe.dist

        j = qe.vertex
        while j <= qe.vertex+dice and j < board_size:

            if visited[j] == False:
                entry = QueueEntry()
                entry.dist = qe.dist + 1
                entry.vertex = j if board[j] == -1 else board[j]
                queue.append(entry)
                visited[j] = True
            j = j + 1

    return -1

def test_prog():

     data = test_data.strip().splitlines()
     N = int(data.pop(0))
     snake_count = int(data.pop(0))
     snakes = [ map(int, data.pop(0).strip().split()) for i in range(snake_count) ]
     ladder_count = int(data.pop(0))
     ladders = [ map(int, data.pop(0).strip().split()) for i in range(ladder_count) ]

     print N
     print snakes
     print ladders

     min_steps = find_min_steps(snakes, ladders, N)
     if min_steps != -1:
         print "Minimum steps to win the game: ", min_steps
     else:
         print "Solution not found"


def main():

    print "*" * 80
    print "Instructions for the input"
    print "Enter board dimention in the first line"
    print "Enter number of snakes in second line"
    print "Enter snake positions head and tail values in each line"
    print "Enter number of ladders"
    print "Enter ladder positions base and top values in each line"
    print "*" * 80

    N = int(raw_input())
    snake_count = int(raw_input())
    snakes = [map(int, raw_input().strip().split()) for i in range(snake_count)]
    ladder_count = int(raw_input())
    ladders = [map(int, raw_input().strip().split()) for i in range(ladder_count)]


    print N
    print snakes
    print ladders

    min_steps = find_min_steps(snakes, ladders, N)
    if min_steps != -1:
        print "Minimum steps to win the game: ", min_steps
    else:
        print "Solution not found"

if __name__ == '__main__':
    test_prog()
    #main()

