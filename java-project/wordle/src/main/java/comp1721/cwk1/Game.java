package comp1721.cwk1;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

public class Game {
  private int gameNumber;
  private String target; 
  private String CommandLine; 


  public String getCommand(String a)
  {
    CommandLine  = a; 
    return CommandLine; 
  }

  // TODO: Implement constructor with String parameter
  public Game(String filename)throws IOException
  {
    //check today game
    LocalDate localDay = LocalDate.now();
    LocalDate firstDay =  LocalDate.of(2021, 06, 19); 
    long diff = ChronoUnit.DAYS.between(firstDay, localDay); 

    WordList wordlist = new WordList(filename);

    wordlist.size();
    gameNumber = (int)diff; 
    target = wordlist.getWord((int)diff); 
  }

  // TODO: Implement constructor with int and String parameters
  public Game(int num, String filename)throws IOException
  {
    WordList wordlist = new WordList(filename); 

    wordlist.size();
    gameNumber = num; 
    target = wordlist.getWord(num); 
  }

  // TODO: Implement play() method
  public void play()throws IOException
  {
  // Init everything
    int GameRange = 1; //only 6 time guess

    BufferedWriter writer = new BufferedWriter(new FileWriter("build/lastgame.txt"));
    Guess guess;

    System.out.printf("WORDLE %d\n\n", gameNumber);
    //loop guess until all match or Guessing time end 
    do
    {
      guess = new Guess(GameRange); 
      
      guess.readFromPlayer();

      if(CommandLine == null)
      {
        System.out.println(guess.compareWith(target));
        writer.append(guess.compareWith(target));
        writer.append("\n");
      }
      else if (CommandLine.equals("-a"))
      {
        guess.compareWithNoneColorMode(target); 
        writer.append("----------------------------------------\n"); 
        System.out.println(guess.compareWithNoneColorMode(target));
        writer.append(guess.compareWithNoneColorMode(target));
      }
      GameRange++; 

    }while(guess.matches(target) == false); 
      if(GameRange == 1)
      {
        System.out.printf("Superb - Got it in one!\n\n");
      }
      else if (GameRange < 7 && GameRange > 1)
      {
        System.out.printf("Well done!\n\n"); 
      }
      else
      {
        System.out.printf("That was a close call\n\n");
      }

      //remind: close file writer
      writer.close();
}

  // TODO: Implement save() method, with a String parameter
  public void save(String filename)throws IOException
  {
    
    BufferedReader br = new BufferedReader(new FileReader(filename));
    String line;
    while ((line = br.readLine()) != null) {
      System.out.println(line);
    }
    br.close();
  }
}
