package comp1721.cwk2;

/**
 * Representation of a playing card.
 *
 * <p>Provided for use in COMP1721 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class Card implements Comparable<Card> {

  /*--------------------------- Enumerated types ---------------------------*/

  public enum Rank {
    ACE('A'), TWO('2'), THREE('3'), FOUR('4'), FIVE('5'),
    SIX('6'), SEVEN('7'), EIGHT('8'), NINE('9'), TEN('T'),
    JACK('J'), QUEEN('Q'), KING('K');

    private final char symbol;

    Rank(char s) { symbol = s; }

    public char getSymbol() { return symbol; }

    @Override
    public String toString()
    {
      String rankName = name();
      return rankName.substring(0, 1) + rankName.substring(1).toLowerCase();
    }
  }

  public enum Suit {
    CLUBS('C', '\u2663'), DIAMONDS('D', '\u2666'),
    HEARTS('H', '\u2665'), SPADES('S', '\u2660');
    
    private final char symbol;
    private final char fancySymbol;

    Suit(char s, char fs) {
      symbol = s;
      fancySymbol = fs;
    }

    public char getSymbol() { return symbol; }
    public char getFancySymbol() { return fancySymbol; }

    @Override
    public String toString()
    {
      String suitName = name();
      return suitName.substring(0, 1) + suitName.substring(1).toLowerCase();
    }
  }

  /*-------------------------- Class-level code ----------------------------*/

  private static boolean fancySymbols = false;

  /**
   * Enables or disables use of fancy Unicode symbols for suits.
   *
   * @param fancy True if fancy symbols are required, false otherwise
   */
  public static void useFancySymbols(boolean fancy) {
    fancySymbols = fancy;
  }

  /*------------------------- Instance-level code --------------------------*/

  private Rank rank;
  private Suit suit;

  /**
   * Creates a Card object.
   *
   * @param r Rank of the card
   * @param s Suit of the card
   */
  public Card(Rank r, Suit s) {
    rank = r;
    suit = s;
  }

  /**
   * Creates a Card object, given its name as a string.
   *
   * <p>Name can either be given in full - e.g., "Ace of Clubs" - or
   * be abbreviated to a two-character code - e.g., "AC".</p>
   *
   * @param name Name of card
   * @throws IllegalArgumentException if string is invalid
   */
  public Card(String name) {
    if (name.length() > 2) {
      parseLongName(name);
    }
    else {
      parseRank(name);
      parseSuit(name);
    }
  }

  private void parseLongName(String name) {
    String[] parts = name.split("\\s+");
    if (parts.length == 3 && parts[1].toLowerCase().equals("of")) {
      rank = Rank.valueOf(parts[0].toUpperCase());
      suit = Suit.valueOf(parts[2].toUpperCase());
    }
    else {
      throw new IllegalArgumentException("Invalid card name format");
    }
  }

  private void parseRank(String name) {
    for (Rank r: Rank.values()) {
      if (r.getSymbol() == name.charAt(0)) {
        rank = r;
        break;
      }
    }

    if (rank == null) {
      throw new IllegalArgumentException("Unrecognised rank");
    }
  }

  private void parseSuit(String name) {
    for (Suit s: Suit.values()) {
      if (s.getSymbol() == name.charAt(1)) {
        suit = s;
        break;
      }
    }

    if (suit == null) {
      throw new IllegalArgumentException("Unrecognised suit");
    }
  }

  /**
   * Provides the rank of this card.
   *
   * @return The rank
   */
  public Rank getRank() {
    return rank;
  }

  /**
   * Provides the suit of this card.
   *
   * @return The suit
   */
  public Suit getSuit() {
    return suit;
  }

  /**
   * Computes the hash code for this card.
   *
   * @return Hash code
   */
  @Override
  public int hashCode() {
    return java.util.Objects.hash(rank, suit);
  }

  /**
   * Tests whether this card is equal to another object.
   *
   * @param thing Object with which this card is being compared
   * @return true if thing is equal to this card, false otherwise
   */
  @Override
  public boolean equals(Object thing) {
    boolean same = false;

    if (thing == this) {
      same = true;
    }
    else if (thing instanceof Card) {
      final Card card = (Card) thing;
      if (rank == card.rank && suit == card.suit) {
        same = true;
      }
    }

    return same;
  }

  /**
   * Creates a two-character string representation of this card.
   *
   * <p>The first character represents rank, the second represents suit.
   * Special Unicode symbols will be used for the latter if
   * <code>Card.fancySymbols</code> is set to <code>true</code>.</p>
   *
   * @return String representation of this card
   */
  @Override
  public String toString() {
    if (fancySymbols) {
      return String.format("%c%c", rank.getSymbol(), suit.getFancySymbol());
    }
    else {
      return String.format("%c%c", rank.getSymbol(), suit.getSymbol());
    }
  }

  /**
   * Generates this card's full name - e.g., "Ace of Spades".
   *
   * @return Full name of this card, as a string
   */
  public String fullName() {
    return String.format("%s of %s", rank, suit);
  }

  /**
   * Compares this card to another, using their natural ordering
   * (by suit, then by rank).
   *
   * @return A negative integer if this card comes before the other, 0 if
   *   they are the same, a positive integer if this card comes after
   */
  @Override
  public int compareTo(Card other) {
    int difference = suit.compareTo(other.suit);

    if (difference == 0) {
      difference = rank.compareTo(other.rank);
    }

    return difference;
  }

  /**
   * Computes the value of this card.
   *
   * <p>Value is based on rank and disregards suit. Aces score 1
   * and picture cards all score 10.</p>
   *
   * @return Card value
   */
  public int value() {
    return Math.min(rank.ordinal() + 1, 10);
  }
}
