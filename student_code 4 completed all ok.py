import math
from collections import defaultdict
import heapq

def shortest_path(M, start, goal):
    explored_id = list()
    explored_id.append(start)
    explored_distance = 0

    current_id = start
    previous_id = start
    terminate_id = start
    next_id = start
    itera = 0

    if start == goal:
        print([start])

    established = {}

    test = defaultdict()

    #############
    explored_set = list()
    explored_set.append(start)
    ############
    
    choice_distance_priority_queue = list()
    
    while current_id != goal:




        ################
        if current_id in explored_set:
            explored_set.remove(current_id)
        ###############    

        if len(explored_id) == 1:
            previous_id = start
        else:
            previous_id = explored_id[-2]

        #print("\n\n======itera", itera, "begin,", "explored", explored_id)

        # get neighbour id for current id    
        all_neighbour_id = M.roads[current_id]

        #frontier_id = [x for x in all_neighbour_id if x not in explored_id]


        frontier_id = set()
        for x in all_neighbour_id:
            if x not in explored_id:
                frontier_id.add(x)

        # record of total distance of current id:
        #choice_distance = {}
        
        
        #print("itera", itera, "middle",", frontier_id:", frontier_id)
        #print("previous_id,current_id",previous_id, current_id)
        explored_distance += distance(M, previous_id, current_id)
        #print("explored_distance", explored_distance)



        for node_id in frontier_id:
            # use A* algorithm, distance = greedy distance + heuristic distance
            greedy_distance = []
            greedy_distance.append(node_id)
            greedy_distance += explored_id

            #print("\n  --------exploring frontier node_id ", node_id)
            #print("  greedy_distance_id", greedy_distance, ",\n  explored_id:", greedy_distance[1:])


            #test.append([current_id, node_id])
            #print("test0: ", test)

            #print("explored_set: ", opeexplored_setnset)
            #if node_id not in explored_set or (len(explored_set) == 1 and node_id in explored_set):
            if node_id not in explored_set or len(explored_set) == 1:
                #print("test1: ", test)
                #print("++++++++++++++++++   current_id" , current_id)
                test[node_id] = current_id
                #print("New, current",node_id,current_id ,"added !!!!!!!!!!!!!!")
                explored_set.append(node_id)


            g_distance = explored_distance + distance(M, current_id, node_id)
            #g_distance = distance(M, current_id, node_id)
            h_distance = distance(M, node_id, goal)
            #print ("  pre h_distance: ",h_distance)


            if h_distance > distance(M, current_id, goal):
                h_distance = distance(M, current_id, goal)
            else:
                h_distance = distance(M, node_id, goal)


            #print("  after h_distance: ", h_distance)

            total_distance = 1 * g_distance + h_distance

            #choice_distance[node_id] = total_distance
            heapq.heappush(choice_distance_priority_queue, (total_distance, node_id))
            
            established[node_id] = total_distance
            
            '''
            print("\n  explored_distance:",round(explored_distance,3),\
                  "\n  candidate_greedy_distance between ",current_id, "and", node_id,"is", round(distance(M, current_id, node_id),3),\
                  "\n  g_distance: ", round(g_distance,3),\
                 "\n  final h_distance between ",node_id, "and", goal,"is", round(h_distance,3),\
                 "\n  total_distance:", round(total_distance,3))
                      
            '''
            

        # return min value (total distance) of choice_distance:
        #next_id = min(choice_distance, key=choice_distance.get)
        if len(choice_distance_priority_queue) == 0:
            print("Path not found ! Return retrived path: ")
            break
        else:
            (_, next_id) = heapq.heappop(choice_distance_priority_queue)
        
        #print("\n  choice_distance dictionary:\n", choice_distance)
        #print("  established: \n", established)

        #print("gallery: ", gallery)

        #print("\n  current_id:", current_id, ", frontier_id:", frontier_id)
        #print("\n----------exploring completed, choose id: ", next_id)
        explored_id.append(next_id)

        #print("\nitera", itera, "end, explored_id:", explored_id,"\n============")
        current_id = next_id
        itera += 1

    #print("goal achieved!")
    #print(explored_id)
    #print("test: ",test)
    return path_retrieve(test, current_id)

# distance between two points on the map M   
def distance(M, a, b):
    '''
    Input: two id a, b in integer
    Output: distance between a and b
    '''
    # distance = sqrt((delta_x)^2 + (delta_y)^2)
    return math.sqrt((M.intersections[a][0] - M.intersections[b][0])**2 + (M.intersections[a][1] - M.intersections[b][1])**2)

def path_retrieve(test, current_id):
    path = [current_id]
    while current_id in test.keys():
        current_id = test[current_id]
        path.append(current_id)
    return path[::-1]