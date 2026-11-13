import numpy as np

# -----------------------------------------------------------
# Function: build_adjacency_matrix
# Purpose: Convert edge list into adjacency matrix
# -----------------------------------------------------------
def build_adjacency_matrix(edges):
    
    # Extract all unique nodes from edges
    # We take both source (u) and destination (v)
    nodes = sorted(set([u for u, v in edges] + [v for u, v in edges]))
    
    # Create mapping: node → index (for matrix positioning)
    index = {node: i for i, node in enumerate(nodes)}
    
    # Number of nodes
    n = len(nodes)
    
    # Initialize n x n matrix with zeros
    A = np.zeros((n, n))

    # Fill adjacency matrix
    for u, v in edges:
        # If there is a link from u → v
        # We store it as A[v][u] = 1
        # (column-wise representation for PageRank)
        A[index[v]][index[u]] = 1

    # Return matrix and node list
    return A, nodes


# -----------------------------------------------------------
# Function: normalize_matrix
# Purpose: Convert adjacency matrix into transition matrix
# -----------------------------------------------------------
def normalize_matrix(A):
    
    # Number of nodes (matrix size)
    n = A.shape[0]
    
    # Initialize matrix for normalized values
    M = np.zeros_like(A)

    # Normalize each column
    for j in range(n):
        
        # Sum of column j (total outgoing links from node j)
        col_sum = np.sum(A[:, j])
        
        if col_sum == 0:
            # Dangling node (no outgoing links)
            # Assign equal probability to all nodes
            M[:, j] = 1 / n
        else:
            # Normalize column → divide by total links
            M[:, j] = A[:, j] / col_sum

    # Return transition matrix
    return M