package csc301;

import algs4.*;
import algs4.Graph;
import myalgs4.*;
import java.util.Arrays;


public class BaconNumbers {
	
	public static void main(String[] args) {
		System.out.println("SAAD KHAN***");
		System.out.printf("%-18s", "Actor Name");
		System.out.printf("--- Bacon Number " + "%2s", "");
		System.out.printf("  --- Bacon Path " + "%s%n", "");
		System.out.println("-------------------------------------------------------------------");
		BSTEssential<Integer, String> BST1 = new BSTEssential<>();
		BSTEssential<String, Integer> BST2 = new BSTEssential<>();
		StdIn.fromFile("data/KBgraphActors.txt");
		String[] words = StdIn.readAllStrings();
        String sorted[] = new String[words.length];
        for (int i = 0; i < words.length; i++)
            sorted[i] = words[i];
        Arrays.sort(sorted);
		for (int w = 0; w< sorted.length; w++) {
			String word = sorted[w];
			BST1.put(w, word);
			}
		for (int e = 0; e< words.length; e++) {
			String word2 = words[e];
			BST2.put(word2, e);
			}
		Graph g = new Graph(new In("data/KBgraph.txt"));
		BreadthFirstPaths breadth = new BreadthFirstPaths(g, 0);
		for (int v = 0; v < g.V(); v++) {
			//int kevin = BST2.get("Kevin_Bacon");
			String vectorvalue = BST1.get(v);
			int vector = BST2.get(vectorvalue);
			int KBnum = breadth.distTo(vector);
			Iterable<Integer> pathlist = breadth.pathTo(vector);
			String path = "";
			for (int w : pathlist) {
				//StdOut.println(w);
				path = path + words[w] + "->";
			}
			
			System.out.printf("%-18s", vectorvalue);
			System.out.printf("---" + "%10s", KBnum);
			System.out.printf("        --- " + "%s%n",path);
		}
        
        }
	
}
	
