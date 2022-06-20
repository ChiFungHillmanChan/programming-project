// Correctness testing for COMP1721 Coursework 2 (Full Solution)

package comp1721.cwk2;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.hamcrest.Matchers.is;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.junit.jupiter.api.Assertions.assertAll;

public class Full {

  private PokerHand hand;
  private PokerHand oneCard;
  private PokerHand twoCards;
  private PokerHand fiveCards;
  private PokerHand pair;
  private PokerHand twoPairs;
  private PokerHand threeOfAKind;
  private PokerHand fourOfAKind;
  private PokerHand fullHouse;

  @BeforeAll
  public static void perClassSetup() {
    Card.useFancySymbols(true);
  }

  @BeforeEach
  public void perTestSetup() {
    hand = new PokerHand();
    oneCard = new PokerHand("AC");
    twoCards = new PokerHand("AC 3D");
    fiveCards = new PokerHand("AC 3D 5H 7S 9C");
    pair = new PokerHand("AC AD 3H 5S 7C");
    twoPairs = new PokerHand("AC AD 3H 3S 5C");
    threeOfAKind = new PokerHand("AC AD AH 3S 5C");
    fourOfAKind = new PokerHand("AC AD AH AS 3C");
    fullHouse = new PokerHand("AC AD AH 3S 3C");
  }

  @Test
  @DisplayName("Fancy suit symbols used correctly")
  public void handAsStringFancySuits() {
    Card.useFancySymbols(true);
    assertAll(
      () -> assertThat(hand.toString(), is("")),
      () -> assertThat(oneCard.toString(), is("A\u2663")),
      () -> assertThat(twoCards.toString(), is("A\u2663 3\u2666")),
      () -> assertThat(fiveCards.toString(), is("A\u2663 3\u2666 5\u2665 7\u2660 9\u2663"))
    );
  }

  @Test
  @DisplayName("Pair detected correctly")
  public void handIsPair() {
    PokerHand fourCards = new PokerHand("AC AD 3H 5S");
    assertAll(
      () -> assertThat(hand.isPair(), is(false)),
      () -> assertThat(fourCards.isPair(), is(false)),
      () -> assertThat(fiveCards.isPair(), is(false)),
      () -> assertThat(pair.isPair(), is(true)),
      () -> assertThat(twoPairs.isPair(), is(false))
    );
  }

  @Test
  @DisplayName("Two Pairs detected correctly")
  public void handIsTwoPairs() {
    PokerHand fourCards = new PokerHand("AC AD 3H 3S");
    assertAll(
      () -> assertThat(hand.isPair(), is(false)),
      () -> assertThat(fourCards.isTwoPairs(), is(false)),
      () -> assertThat(fiveCards.isTwoPairs(), is(false)),
      () -> assertThat(pair.isTwoPairs(), is(false)),
      () -> assertThat(twoPairs.isTwoPairs(), is(true))
    );
  }

  @Test
  @DisplayName("Three of a Kind detected correctly")
  public void handIsThreeOfAKind() {
    PokerHand fourCards = new PokerHand("AC AD AH 3S");
    assertAll(
      () -> assertThat(hand.isThreeOfAKind(), is(false)),
      () -> assertThat(fourCards.isThreeOfAKind(), is(false)),
      () -> assertThat(pair.isThreeOfAKind(), is(false)),
      () -> assertThat(threeOfAKind.isThreeOfAKind(), is(true)),
      () -> assertThat(fourOfAKind.isThreeOfAKind(), is(false)),
      () -> assertThat(fullHouse.isThreeOfAKind(), is(false))
    );
  }

  @Test
  @DisplayName("Four of a Kind detected correctly")
  public void handIsFourOfAKind() {
    PokerHand fourCards = new PokerHand("AC AD AH AS");
    assertAll(
      () -> assertThat(hand.isFourOfAKind(), is(false)),
      () -> assertThat(fourCards.isFourOfAKind(), is(false)),
      () -> assertThat(threeOfAKind.isFourOfAKind(), is(false)),
      () -> assertThat(fourOfAKind.isFourOfAKind(), is(true))
    );
  }

  @Test
  @DisplayName("Full House detected correctly")
  public void handIsFullHouse() {
    assertAll(
      () -> assertThat(hand.isFullHouse(), is(false)),
      () -> assertThat(pair.isFullHouse(), is(false)),
      () -> assertThat(threeOfAKind.isFullHouse(), is(false)),
      () -> assertThat(fourOfAKind.isFullHouse(), is(false)),
      () -> assertThat(fullHouse.isFullHouse(), is(true))
    );
  }

  @Test
  @DisplayName("Flush detected correctly")
  public void handIsFlush() {
    PokerHand fourCards = new PokerHand("AC 3C 5C 7C");
    PokerHand flushClubs = new PokerHand("AC 3C 5C 7C 9C");
    PokerHand flushSpades = new PokerHand("AS 3S 5S 7S 9S");
    PokerHand notFlush = new PokerHand("AC 3C 5C 7C 9D");
    assertAll(
      () -> assertThat(hand.isFlush(), is(false)),
      () -> assertThat(fourCards.isFlush(), is(false)),
      () -> assertThat(flushClubs.isFlush(), is(true)),
      () -> assertThat(flushSpades.isFlush(), is(true)),
      () -> assertThat(notFlush.isFlush(), is(false))
    );
  }

  @Test
  @DisplayName("Straight detected correctly")
  public void handIsStraight() {
    PokerHand fourCards = new PokerHand("2C 3D 4H 5S");
    PokerHand straight = new PokerHand("2C 3D 4H 5S 6C");
    PokerHand lowAceStraight = new PokerHand("AC 2D 3H 4S 5C");
    PokerHand notStraight = new PokerHand("2C 3D 4H 5S 7C");
    assertAll(
      () -> assertThat(hand.isStraight(), is(false)),
      () -> assertThat(fourCards.isStraight(), is(false)),
      () -> assertThat(straight.isStraight(), is(true)),
      () -> assertThat(lowAceStraight.isStraight(), is(true)),
      () -> assertThat(notStraight.isStraight(), is(false))
    );
  }

  @Test
  @DisplayName("Straight with high ace detected correctly")
  public void straightAllowsHighAce() {
    PokerHand highAceStraight = new PokerHand("TC JD QH KS AC");
    assertThat(highAceStraight.isStraight(), is(true));
  }
}
