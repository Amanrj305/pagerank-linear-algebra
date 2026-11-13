import numpy as np
import sys
import os

# Add current directory to Python path (so we can import local files)
sys.path.append(os.path.dirname(__file__))

# Import helper functions
from matrix_utils import build_adjacency_matrix, normalize_matrix
from visualize import draw_graph



# Function: load_graph
# Purpose: Reads graph data from file and converts to edge list

def load_graph(file_path):
    edges = []

    # Open the file and read line by line
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()

            # Only consider valid lines with two nodes
            if len(parts) == 2:
                u, v = parts
                edges.append((u, v))  # store edge (u -> v)

    return edges



# Purpose: Compute PageRank using iterative method

def pagerank(M, d=0.85, max_iter=100, tol=1e-6):
    n = M.shape[0]

    # Initialize rank vector with equal probability
    x = np.ones(n) / n

    # Iterative computation (Power Method)
    for _ in range(max_iter):
        # PageRank formula
        x_new = (1 - d) / n + d * M @ x

        # Check convergence (L1 norm)
        if np.linalg.norm(x_new - x, 1) < tol:
            break

        x = x_new  # update vector

    return x




# Purpose: Controls overall flow of program

def main():

    # Step 1: Load graph from file
    edges = load_graph("../data/graph.txt")

    # Step 2: Visualize graph (for understanding)
    draw_graph(edges)

    # Step 3: Build adjacency matrix
    A, nodes = build_adjacency_matrix(edges)

    # Step 4: Normalize matrix (convert to transition matrix)
    M = normalize_matrix(A)

    # Step 5: Compute PageRank
    ranks = pagerank(M)

    # Step 6: Print results
    print("\nPageRank Results:\n")
    for node, rank in zip(nodes, ranks):
        print(f"{node}: {rank:.4f}")

    # Step 7: Save results to file
    with open("../output/results.txt", "w") as f:
        for node, rank in zip(nodes, ranks):
            f.write(f"{node}: {rank:.4f}\n")


# Entry point of program
if __name__ == "__main__":
    main()