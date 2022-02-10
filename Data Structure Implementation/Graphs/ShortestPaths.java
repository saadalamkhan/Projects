package csc301;

import algs4.*;

public class ShortestPaths {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		StdOut.println("*** Saad Khan ***");
		Graph g = new Graph(new In("data/KBgraph.txt"));
		BreadthFirstPaths breadth = new BreadthFirstPaths(g, 0);
		for (int v = 0; v < g.V(); v++) {
			Iterable<Integer> pathlist = breadth.pathTo(v);
			int distance = breadth.distTo(v);
			StdOut.print("Vertex number: " + v+" - distance from 0:  " + distance + " - Path to 0: " + pathlist);
			StdOut.println();
			}
	}
}
	
		
