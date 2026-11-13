# PageRank Algorithm Implementation

I built this custom implementation of the Google PageRank algorithm for my Linear Algebra course. It calculates the importance of different nodes in a directed graph by treating links as votes of confidence.

## The Math Behind It
At its core, this project applies a few key linear algebra concepts to solve the ranking problem:
* **Transition Matrices:** It builds a column-stochastic matrix to represent the probability of moving from one node to another.
* **The Random Surfer Model:** To prevent the algorithm from getting stuck in dead-ends, it includes a damping factor (usually 0.85). This simulates a user randomly jumping to a completely new page.
* **Power Iteration:** The script repeatedly multiplies the matrix to find its principal eigenvector, stopping once the rankings converge and stabilize.

## Project Structure
* `pagerank.py` - The main script that runs the algorithmic logic and the power iteration loop.
* `matrix_utils.py` - Handles the underlying matrix math, normalization, and stochastic transitions.
* `visualize.py` - Outputs the final graph and shows the resulting rank distribution.

## How to Run

```bash
cd src
python3 pagerank.py