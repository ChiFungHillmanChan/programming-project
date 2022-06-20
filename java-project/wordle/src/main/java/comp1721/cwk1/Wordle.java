// Main program for COMP1721 Coursework 1
// DO NOT CHANGE THIS!

package comp1721.cwk1;

import java.io.IOException;


public class Wordle {
  public static void main(String[] args) throws IOException {
    Game game;

    if (args.length > 0) 
    {
      // Player wants to specify the game
      if(args[0].equals("-a"))
      {
        // Player wants to specify the game with accessible Wordle
        if(args.length > 1)
        {
          game = new Game(Integer.parseInt(args[1]), "data/words.txt");
          game.getCommand(args[0]); 
        }
        else
        {
          game = new Game("data/words.txt");
          game.getCommand(args[0]); 
        }
      }
      else
      {
        // Player wants today's accessible wordle
        game = new Game(Integer.parseInt(args[0]),"data/words.txt");
      }
    }
    else {
      // Play today's game
      game = new Game("data/words.txt");
    }

    game.play();
    game.save("build/lastgame.txt");
  }
}
