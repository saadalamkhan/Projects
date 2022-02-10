package csc301;

import algs4.*;
import java.util.Arrays;

public class TimeST {
	
	public static void original() {
		StdOut.println("=== Times with original ordering ===");
		BST<String, Integer> BST = new BST<>();
		AVLTreeST<String, Integer> AVLST = new AVLTreeST<>();
		SeparateChainingHashST<String, Integer> SCHST = new SeparateChainingHashST<>();
		StdIn.fromFile("data/tale.txt");
		String[] words = StdIn.readAllStrings();
		Stopwatch watch;
		//BST 
		watch = new Stopwatch();
		for (int w = 0; w< words.length; w++) {
			String word = words[w];
			Integer value = BST.get(word);
			if (value != null) {
				BST.put(word, value + 1);
			}
			else {
				BST.put(word, 1);
			}
		}
		double time = watch.elapsedTime();
		StdOut.println("BST Time: " + time);
		//AVLST
		watch = new Stopwatch();
		for (int w = 0; w< words.length; w++) {
			String word = words[w];
			Integer value = AVLST.get(word);
			if (value != null) {
				AVLST.put(word, value + 1);
			}
			else {
				AVLST.put(word, 1);
			}
		}
		double time2 = watch.elapsedTime();
		StdOut.println("AVLST Time: " + time2);
		//SCHST
		watch = new Stopwatch();
		for (int w = 0; w< words.length; w++) {
			String word = words[w];
			Integer value = SCHST.get(word);
			if (value != null) {
				SCHST.put(word, value + 1);
			}
			else {
				SCHST.put(word, 1);
			}
		}
		double time3 = watch.elapsedTime();
		StdOut.println("SCHST Time: " + time3);	
		//Sorted
		StdOut.println("=== Times with sorted ordering ===");
		BST = new BST<>();
		AVLST = new AVLTreeST<>();
		SCHST = new SeparateChainingHashST<>();
		Arrays.sort(words);
		//BST (Sorted)
		watch = new Stopwatch();
		for (int w = 0; w< words.length; w++) {
			String word = words[w];
			Integer value = BST.get(word);
			if (value != null) {
				BST.put(word, value + 1);
			}
			else {
				BST.put(word, 1);
			}
		}
		double time4 = watch.elapsedTime();
		StdOut.println("BST Time: " + time4);
		//AVLST (sorted)
		watch = new Stopwatch();
		for (int w = 0; w< words.length; w++) {
			String word = words[w];
			Integer value = AVLST.get(word);
			if (value != null) {
				AVLST.put(word, value + 1);
			}
			else {
				AVLST.put(word, 1);
			}
		}
		double time5 = watch.elapsedTime();
		StdOut.println("AVLST Time: " + time5);
		//SCHST (sorted)
		watch = new Stopwatch();
		for (int w = 0; w< words.length; w++) {
			String word = words[w];
			Integer value = SCHST.get(word);
			if (value != null) {
				SCHST.put(word, value + 1);
			}
			else {
				SCHST.put(word, 1);
			}
		}
		double time6 = watch.elapsedTime();
		StdOut.println("SCHST Time: " + time6);		
	}
	
	public static void main(String[] args) {
		StdOut.println("Saad Khan ***");
		original();
	}
}
