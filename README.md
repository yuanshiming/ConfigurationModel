# ConfigurationModel

Definition 1.2.5 (Configuration model graph (CM)). Let p=(p_k,k∈Z_+ ) be a probability distribution on Z_+. The Bollosbas-Molloy-Reed or Configuration random graph with vertices V is constructed as follows. We associate with each vertex u∈V an independent random variable X_u drawn from the distribution p, that corresponds to the number of half edges attached to u. Conditionally on {∑_(u∈V)▒〖X_u even〗}, the Configuration model random graph is a multigraph (a graph with possibly self-loops and multiple edges) obtained by pairing the half-edges uniformly at random.
A possible algorithm for pairing the half edges (also called stubs) is the following:
-Associate with each half edge an independent uniform random variable on [0,1] and sort the half-edges by decreasing values.
-Pair each odd stub with the following even stub. Note that if the number of stubs ∑_(u∈V)▒X_u  is odd, it is possible to add or remove one stub arbitrarily.
Note that this linkage procedure does not exclude self-loops or multiple edges. When the size of graph N→+∞ with a fixed degree distribution, self-loops and multiple edges become less and less apparent in the global picture.
