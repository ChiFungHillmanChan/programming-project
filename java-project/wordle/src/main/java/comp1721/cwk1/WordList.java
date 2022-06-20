package comp1721.cwk1;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class WordList {
  private List<String> words;

  // TODO: Implement constructor with a String parameter
  public WordList(String filename)throws IOException
  {
    this.words = new ArrayList<>();
    //read file
    Path path = Paths.get(filename);
    BufferedReader input = Files.newBufferedReader(path);

    String line = input.readLine();

    //store to words arrayList
    while (line != null){
      words.add(line);
      line = input.readLine();
    }
    input.close();
  }

  // TODO: Implement size() method, returning an int
  public int size()
  {
    return words.size(); 
  }
  
  // TODO: Implement getWord() with an int parameter, returning a String
  public String getWord(int num)
  {
    //remind: word size array start from 0
    if(num > words.size() - 1|| num < 0){
      throw new GameException("Game Number out of range.");
    }
    return words.get(num);
  }
}
