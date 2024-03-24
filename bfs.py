import time
from sokobanGame import es_estado_final, generate_next_states, reconstruct_path

class BFS:
    def search(game):
        # Inicia el cronometro
        start = time.time()
        
        # Implementa el algoritmo BFS
        total_steps = 0
        nodes_expanded = 0
        frontier_nodes = 0
        
        # Initialize the frontier with the initial state
        frontier = [game.board]
        # Initialize an empty set to keep track of visited states
        visited = set()
        # Initialize a dictionary to keep track of the path to each state
        parent = {str(game.board): None}
        expanded_nodes = 0  # Counter for expanded nodes
        frontier_nodes = 1  # Counter for nodes in the frontier (initial state is in the frontier)

        # Continue searching until the frontier is empty
        while frontier:
            # Pop the first state from the frontier
            current_state = frontier.pop(0)
            # Increment the count of expanded nodes
            expanded_nodes += 1

            # Check if the current state is the goal state
            if es_estado_final(current_state):
                # Return the path to the goal state along with statistics
                return reconstruct_path(parent, current_state), expanded_nodes, frontier_nodes
            
            # Mark the current state as visited
            visited.add(str(current_state))

            # Generate all possible next states
            for next_state in generate_next_states(current_state):
                # Check if the next state has not been visited
                if str(next_state) not in visited:
                    # Add the next state to the frontier
                    frontier.append(next_state)
                    # Increment the count of frontier nodes
                    frontier_nodes += 1
                    # Record the path to the next state
                    parent[str(next_state)] = current_state
                    
                          
        # Finaliza e imprime el cronometro
        end = time.time()
        total_time = end - start
        
        print("BFS: Tiempo de ejecución", total_time, "segundos") 
        print("BFS: Numero de pasos:", total_steps)
        print("BFS: Numero de nodos expandidos:", nodes_expanded) 
        print("BFS: Numero de nodos frontera:", frontier_nodes) 
        
        # If no solution is found, return None along with statistics
        return None, expanded_nodes, frontier_nodes
