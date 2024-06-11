from pyeda.inter import bddvar, expr2bdd
import graphviz

# Define BDD variables
A = bddvar('A')
B = bddvar('B')
C = bddvar('C')
D = bddvar('D')

# Not A = ~A
# Implication A => B = (~A | B)
# A ^ B
# Construct the BDD for A XOR B
f = (A ^ B) & (B ^ C) ^ (C ^ D)

# Convert expression to a BDD
f_bdd = expr2bdd(f)

# Function to visualize the BDD
def visualize_bdd(bdd, filename='bdd_graph'):
    # Generate dot format for BDD
    dot_format = bdd.to_dot()
    # Create a Graphviz graph from the dot format
    src = graphviz.Source(dot_format)
    # Render the graph to a file (default format: PDF)
    src.render(filename, format='png', cleanup=True)
    print(f"Graph is rendered as {filename}.png")

# Visualize the BDD
visualize_bdd(f_bdd)
