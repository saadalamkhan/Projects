package csc301;

import algs4.*;
import java.util.Arrays;

public class DNASequences {
	private AVLTreeST<String, String> AVL;
	
	public DNASequences() {
		AVL = new AVLTreeST<String, String>();
		
	}
	
	public void addSpecies(String species, String sequence) {
		AVL.put(species, sequence);
	}
	
	public void removeSpecies(String species) {
		AVL.delete(species);
	}
	public String[] speciesList(String[] spList){
		String[] list1 = new String[spList.length];
		list1 = spList;
		Arrays.sort(list1);
		return list1;
	}
	public String sequence(String species) {
		String sequence = null;
		sequence = AVL.get(species);
		if (sequence == null) {
			return null;
		}
		else{
			return sequence;
		}
	}
	public int size() {
		return AVL.size();
	}

	
	
}
