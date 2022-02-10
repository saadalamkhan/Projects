package csc301;

import algs4.*;
import java.util.Arrays;

public class TestDNASequences extends DNASequences{

	public static void main(String[] args) {
		StdOut.println("Saad Khan ***");
		DNASequences DNA = new DNASequences();
		StdIn.fromFile("data/mammals.txt");
		String[] lines = StdIn.readAllLines();
		String [] spList = new String[lines.length];
		for (int i = 0; i<lines.length; i++) {
			String line = lines[i];
			String[] entry = line.split("	");
			String species = entry[0];
			String sequence = entry[1];
			spList[i] = species;
			DNA.addSpecies(species, sequence);
	}
		int size = DNA.size();
		StdOut.println("Size of collection: " + size);
		Arrays.sort(spList);
		StdOut.println("Species - - - Sequence:  ");
		for (int s = 0; s < spList.length; s++) {
			String spec = spList[s];
			String seq = DNA.sequence(spec);
			String trimmedseq = seq.substring(0, 20);
			StdOut.println(spec + " - - - " + trimmedseq);
		}
		for (int l = 0; l<spList.length; l++) {
			String spRemove = spList[l];
			DNA.removeSpecies(spRemove);
		}
		size = DNA.size();
		StdOut.println("Size of collection: " + size);
	}
}
