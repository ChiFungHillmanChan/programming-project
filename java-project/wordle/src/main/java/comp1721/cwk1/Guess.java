package comp1721.cwk1;

import java.util.Arrays;
import java.util.Scanner;


public class Guess {
  // Use this to get player input in readFromPlayer()
  private static final Scanner INPUT = new Scanner(System.in);
  private int guessNumber; 
  private String ChosenWord; 

  // TODO: Implement constructor with int parameter
  public Guess(int number)
  {
    if(number < 1 )
    {
      throw new GameException("Guess number must be start from 1"); 
    }
    else if (number > 6)
    {
      throw new GameException("Sorry! You can only guess 6 times. "); 
    }
    guessNumber = number; 
  }

  // TODO: Implement constructor with int and String parameters
  public Guess(int number, String word)
  { 
    //check guessing time 
    if(number < 1 )
    {
      throw new GameException("Guess number must be start from 1"); 
    }
    else if (number > 6)
    {
      throw new GameException("Sorry! You can only guess 6 times. "); 
    }
    //Invalid length
    if( word.length() != 5)
    {
      throw new GameException("Invalid word length! word length must be 5"); 
    }
    //Invalid type of word
    for (int i = 0; i < word.length(); i++) {
      if ( !Character.isLetter( word.toUpperCase().charAt(i) ))
      {
        throw new GameException("Guess words must be character only!"); 
      }
    }
    guessNumber = number;
    ChosenWord = word.toUpperCase(); 
  }

  // TODO: Implement getGuessNumber(), returning an int
  public int getGuessNumber()
  {
    return guessNumber; 
  }  

  // TODO: Implement getChosenWord(), returning a String
  public String getChosenWord()
  {
    return ChosenWord.toUpperCase(); 
  }  

  // TODO: Implement readFromPlayer()
  public void readFromPlayer()
  {
    //for player to input guessing word

    System.out.printf("Enter guess (%d/6): ", guessNumber);
    ChosenWord = INPUT.nextLine().toUpperCase();
    new Guess(guessNumber, ChosenWord); 
  }

  // TODO: Implement compareWith(), giving it a String parameter and String return type
  public String compareWith(String target)
  {
    String [] saveIndex = new String [target.length()]; 
    StringBuffer SaveWord = new StringBuffer();
    int [] intArray = {0,1,2,3,4};  
    int checkwrong;  

    for (int i = 0; i < target.length(); i++) 
    {
      //check correct place and word
      if(ChosenWord.charAt(i) == target.charAt(i))
      {
        saveIndex[i] = "\033[30;102m " + ChosenWord.charAt(i)+" \033[0m";
        intArray[i] = -1;
      }
    }
    for (int i = 0; i < target.length(); i++) 
    {
      // variable for checking if index changes to yellow
      checkwrong = 0; 
      for(int j = 0; j < target.length(); j++)
      {
        // check if matched but wrong place
        if(ChosenWord.charAt(i) == target.charAt(j) && contains(intArray, j) && i != j)
        {
          saveIndex[i] = "\033[30;103m "+ChosenWord.charAt(i)+ " \033[0m";
          //remove index if matched, prevent check again if other letter is the same
          intArray[j] = -1;
          break; 
        } 
        else
        {
          //check all wrong 
          checkwrong++;
          // if checkwrong is 5 and saveIndex is not green, then wrong it is. 
          if(checkwrong == target.length() && saveIndex[i] == null)
          {
            saveIndex[i] = "\033[30;107m "+ ChosenWord.charAt(i)+ " \033[0m";
          }

        }
      }
    }
    
    
    //convert every output to string and return
    for (int i = 0; i < target.length(); i++)
    {
      SaveWord.append(saveIndex[i]); 
    }
    String str = SaveWord.toString(); 
    return str; 
  }

  // TODO: Implement matches(), giving it a String parameter and boolean return type
  public Boolean matches(String target)
  {
    if(target.toUpperCase().equals(ChosenWord))
    {
      return true; 
    }
    else
    {    
      return false;
    }
  }

  public String compareWithNoneColorMode(String target)
  {
    String [] saveIndex = new String [target.length()]; 
    StringBuffer SaveWord = new StringBuffer();
    int [] intArray = {0,1,2,3,4};  
    int checkwrong;  

    for (int i = 0; i < target.length(); i++) 
    {
      //check correct place and word
      if(ChosenWord.charAt(i) == target.charAt(i))
      {
        saveIndex[i] = "Letter '" + ChosenWord.charAt(i) + "' perfect \n"; 
        intArray[i] = -1;
      }
    }
    for (int i = 0; i < target.length(); i++) 
    {
      // variable for checking if index changes to yellow
      checkwrong = 0; 
      for(int j = 0; j < target.length(); j++)
      {
        // check if matched but wrong place
        if(ChosenWord.charAt(i) == target.charAt(j) && contains(intArray, j) && i != j)
        {
          saveIndex[i] ="Letter '" + ChosenWord.charAt(i)  + "' is correct but in wrong place \n"; 
          //remove index if matched, prevent check again if other letter is the same
          intArray[j] = -1;
          break; 
        } 
        else
        {
          //check all wrong 
          checkwrong++;
          // if checkwrong is 5 and saveIndex is not green, then wrong it is. 
          if(checkwrong == target.length() && saveIndex[i] == null)
          {
            saveIndex[i] ="Letter '" + ChosenWord.charAt(i)  + "' is not correct \n"; 
          }

        }
      }
    }
    //convert every output to string and return
    for (int i = 0; i < target.length(); i++)
    {
      SaveWord.append(saveIndex[i]); 
    }
    String str = SaveWord.toString(); 
    return str; 
  }
  //function for matching array
  public boolean contains(final int[] intarray, final int index) 
  {
    return Arrays.stream(intarray).anyMatch(i -> i == index);
  }
}
