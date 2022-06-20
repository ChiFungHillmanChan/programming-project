package comp1721.cwk2;

import java.util.Collections;
import java.util.LinkedList;
import java.util.List;

/**
 * A class to represent a collection of playing cards.
 *
 * <p>The intent is that this should form the basis for new classes
 * useful in card games.  It isn't meant to be instantiated itself and
 * is therefore declared as abstract.</p>
 *
 * <p>Provided for use in COMP1721 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public abstract class CardCollection {

  protected List<Card> cards;

  /**
   * Creates an empty CardCollection.
   */
  public CardCollection() {
    cards = new LinkedList<>();
  }

  /**
   * Provides the number of cards in this collection.
   *
   * @return Number of cards
   */
  public int size() {
    return cards.size();
  }

  /**
   * Returns the numerical value of this collection.
   *
   * <p>This is simply the sum of the values of its cards.</p>
   *
   * @return Value
   */
  public int value() {
    int sum = 0;
    for (Card card: cards) {
      sum += card.value();
    }
    return sum;
  }

  /**
   * Indicates whether this collection is empty or not.
   *
   * @return true if collection is empty, false otherwise
   */
  public boolean isEmpty() {
    return cards.isEmpty();
  }

  /**
   * Indicates whether a particular card is present in this collection.
   *
   * @param card Card we are looking for
   * @return true if the card is present, false otherwise
   */
  public boolean contains(Card card) {
    return cards.contains(card);
  }

  /**
   * Adds the given card to this collection.
   *
   * @param card Card to be added
   */
  public void add(Card card) {
    cards.add(card);
  }

  /**
   * Discards all the cards from this collection.
   */
  public void discard() {
    cards.clear();
  }

  /**
   * Sorts this collection's cards into their natural order.
   */
  public void sort() {
    Collections.sort(cards);
  }
}
