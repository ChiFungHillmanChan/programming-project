// Correctness testing for COMP1721 Coursework 2 (Basic Solution)

package comp1721.cwk2;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertThrows;

public class Basic {

  private Deck deck;
  private PokerHand hand;
  private PokerHand oneCard;
  private PokerHand twoCards;
  private PokerHand full;

  @BeforeAll
  public static void perClassSetup() {
    Card.useFancySymbols(false);
  }

  @BeforeEach
  public void perTestSetup() {
    deck = new Deck();
    hand = new PokerHand();
    oneCard = new PokerHand("AC");
    twoCards = new PokerHand("AC 3D");
    full = new PokerHand("AC 3D 5H 7S 9C");
  }

  // Deck class

  @Test
  @DisplayName("size() works correctly for full and empty decks")
  public void sizeOfDeck() {
    int sizeBefore = deck.size();
    deck.discard();
    int sizeAfter = deck.size();
    assertAll(
      () -> assertThat(sizeBefore, is(52)),
      () -> assertThat(sizeAfter, is(0))
    );
  }

  @Test
  @DisplayName("isEmpty() works correctly for full and empty decks")
  public void deckIsEmpty() {
    boolean emptyBefore = deck.isEmpty();
    deck.discard();
    boolean emptyAfter = deck.isEmpty();
    assertAll(
      () -> assertThat(emptyBefore, is(false)),
      () -> assertThat(emptyAfter, is(true))
    );
  }

  @Test
  @DisplayName("contains() works correctly for a deck")
  public void deckContainsCard() {
    Card aceClubs = new Card(Card.Rank.ACE, Card.Suit.CLUBS);
    boolean containsBefore = deck.contains(aceClubs);
    deck.deal();
    boolean containsAfter = deck.contains(aceClubs);
    assertAll(
      () -> assertThat(containsBefore, is(true)),
      () -> assertThat(containsAfter, is(false))
    );
  }

  @Test
  @DisplayName("Correct cards dealt from deck")
  public void dealFromDeck() {
    Card first = deck.deal();
    Card second = deck.deal();
    assertAll(
      () -> assertThat(deck.size(), is(50)),
      () -> assertThat(first.getRank(), is(Card.Rank.ACE)),
      () -> assertThat(first.getSuit(), is(Card.Suit.CLUBS)),
      () -> assertThat(second.getRank(), is(Card.Rank.TWO)),
      () -> assertThat(second.getSuit(), is(Card.Suit.CLUBS))
    );
  }

  @Test
  @DisplayName("CardException when dealing from an empty deck")
  public void emptyDeckException() {
    deck.discard();
    assertThrows(CardException.class, () -> deck.deal());
  }

  @Test
  @DisplayName("Cards can be added to a deck")
  public void addCardToDeck() {
    Card card = deck.deal();
    deck.add(card);
    assertThat(deck.size(), is(52));
  }

  @Test
  @DisplayName("Deck can be shuffled")
  public void shuffleDeck() {
    deck.shuffle();
    String cards = String.format("%s%s%s%s",
      deck.deal(), deck.deal(), deck.deal(), deck.deal());
    assertThat(cards, is(not("AC2C3C4C")));
  }

  // PokerHand class

  @Test
  @DisplayName("Hands created with correct numbers of cards")
  public void handCreation() {
    assertAll(
      () -> assertThat(hand.size(), is(0)),
      () -> assertThat(oneCard.size(), is(1)),
      () -> assertThat(twoCards.size(), is(2))
    );
  }

  @Test
  @DisplayName("Hand creation fails if too many cards")
  public void tooManyCardsForHand() {
    assertThrows(CardException.class, () -> new PokerHand("AC 3D 5H 7S 9C JD"));
  }

  @Test
  @DisplayName("Cards can be added to a hand")
  public void addCardToHand() {
    hand.add(new Card("AC"));
    assertThat(hand.size(), is(1));
  }

  @Test
  @DisplayName("CardException when adding to a full hand")
  public void addToFullHand() {
    assertThrows(CardException.class, () -> full.add(new Card("JD")));
  }

  @Test
  @DisplayName("CardException when adding a duplicate card to a hand")
  public void addDuplicateCard() {
    assertThrows(CardException.class, () -> oneCard.add(new Card("AC")));
  }

  @Test
  @DisplayName("discard() empties a hand")
  public void canDiscardHand() {
    full.discard();
    assertThat(full.size(), is(0));
  }

  @Test
  @DisplayName("discardTo() returns cards to a deck")
  public void discardToDeck() {
    hand.add(deck.deal());
    hand.add(deck.deal());
    int handSizeBefore = hand.size();
    int deckSizeBefore = deck.size();
    hand.discardTo(deck);
    int handSizeAfter = hand.size();
    int deckSizeAfter = deck.size();
    assertAll(
      () -> assertThat(handSizeBefore, is(2)),
      () -> assertThat(deckSizeBefore, is(50)),
      () -> assertThat(handSizeAfter, is(0)),
      () -> assertThat(deckSizeAfter, is(52))
    );
  }

  @Test
  @DisplayName("CardException when discarding from an empty hand")
  public void cannotDiscardEmptyHand() {
    assertAll(
      () -> assertThrows(CardException.class, () -> hand.discard()),
      () -> assertThrows(CardException.class, () -> hand.discardTo(deck))
    );
  }

  @Test
  @DisplayName("Correct string representation of a hand")
  public void handAsString() {
    assertAll(
      () -> assertThat(hand.toString(), is("")),
      () -> assertThat(oneCard.toString(), is("AC")),
      () -> assertThat(twoCards.toString(), is("AC 3D")),
      () -> assertThat(full.toString(), is("AC 3D 5H 7S 9C"))
    );
  }
}
