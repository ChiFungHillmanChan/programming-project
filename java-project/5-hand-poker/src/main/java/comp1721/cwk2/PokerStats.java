package comp1721.cwk2;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

import static java.lang.System.out;

/**
 * Program to estimate probabilities of different five-card poker hands.
 *
 * <p>Provided for COMP1721 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class PokerStats {

  private static final int DEFAULT_TRIALS = 1000;
  private static final int HANDS_PER_TRIAL = 10;

  private final String logFilename;
  private final int numTrials;

  private int pair = 0;
  private int twoPairs = 0;
  private int threeOfAKind = 0;
  private int fourOfAKind = 0;
  private int fullHouse = 0;
  private int flush = 0;
  private int straight = 0;

  public PokerStats(String filename) {
    this(filename, DEFAULT_TRIALS);
  }

  public PokerStats(String filename, int trials) {
    logFilename = filename;
    numTrials = trials;
  }

  public void runTrials() throws FileNotFoundException {
    try (PrintWriter log = new PrintWriter(new File(logFilename))) {
      resetCounters();
      for (int i = 0; i < numTrials; ++i) {
        Deck deck = new Deck();
        deck.shuffle();
        for (int j = 0; j < HANDS_PER_TRIAL; ++j) {
          PokerHand hand = createHand(deck);
          checkForScoringHand(hand, log);
        }
      }
    }
  }

  private void resetCounters() {
    pair = 0;
    twoPairs = 0;
    threeOfAKind = 0;
    fourOfAKind = 0;
    fullHouse = 0;
    flush = 0;
    straight = 0;
  }

  private PokerHand createHand(Deck deck) {
    PokerHand hand = new PokerHand();
    for (int k = 0; k < PokerHand.FULL_SIZE; ++k) {
      hand.add(deck.deal());
    }
    return hand;
  }

  private void checkForScoringHand(PokerHand hand, PrintWriter log) {
    log.print(hand);
    if (hand.isPair()) {
      log.println("   Pair");
      ++pair;
    }
    else if (hand.isTwoPairs()) {
      log.println("   2 Pairs");
      ++twoPairs;
    }
    else if (hand.isThreeOfAKind()) {
      log.println("   3 of a Kind");
      ++threeOfAKind;
    }
    else if (hand.isFourOfAKind()) {
      log.println("   4 of a Kind");
      ++fourOfAKind;
    }
    else if (hand.isFullHouse()) {
      log.println("   Full House");
      ++fullHouse;
    }
    else if (hand.isFlush()) {
      log.println("   Flush");
      ++flush;
    }
    else if (hand.isStraight()) {
      log.println("   Straight");
      ++straight;
    }
    else {
      log.println();
    }
  }

  public void showResults() {
    int hands = HANDS_PER_TRIAL * numTrials;
    out.printf("\n%,d hands dealt\n\n", hands);

    out.printf("P(Pair)            = %6.3f%%\n", 100.0*pair/hands);
    out.printf("P(Two Pair)        = %6.3f%%\n", 100.0*twoPairs/hands);
    out.printf("P(Three of a Kind) = %6.3f%%\n", 100.0*threeOfAKind/hands);
    out.printf("P(Straight)        = %6.3f%%\n", 100.0*straight/hands);
    out.printf("P(Flush)           = %6.3f%%\n", 100.0*flush/hands);
    out.printf("P(Full House)      = %6.3f%%\n", 100.0*fullHouse/hands);
    out.printf("P(Four of a Kind)  = %6.3f%%\n", 100.0*fourOfAKind/hands);
  }

  public static void main(String[] args) {

    PokerStats stats = null;

    if (args.length == 1) {
      stats = new PokerStats(args[0]);
    }
    else if (args.length == 2) {
      int trials = Integer.parseInt(args[1]);
      stats = new PokerStats(args[0], trials);
    }
    else {
      System.err.println("Error: invalid command line arguments");
      System.err.println("Filename required, optionally followed by number of trials");
      System.exit(1);
    }

    try {
      Card.useFancySymbols(true);
      stats.runTrials();
      stats.showResults();
    }
    catch (FileNotFoundException error) {
      System.err.printf("Error: %s\n", error.getMessage());
      System.exit(2);
    }
  }
}
