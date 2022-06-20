package comp1721.cwk2;

import java.util.ArrayList;
import java.util.Collections;

import comp1721.cwk2.Card.Rank;
import comp1721.cwk2.Card.Suit;
// Implement Deck class here

/**
 * Program to creates a deck containing 52 cards.
 *
 * @author Chi Fung Hillman Chan
 */
public class Deck{
    /**
     * private arratList for deck
     */
    private ArrayList<Card> deck;
    /**
     * Creates a Deck object
     *
     */
    public Deck() {
        deck = new ArrayList<Card>();
        for(Suit suit : Suit.values()){
            for(Rank rank : Rank.values()){
                deck.add(new Card(rank, suit));
            }
        }
    }

    /**
     * Give the number of the cards inside the deck
     *
     * @return Number of cards in deck
     */
    public int size() {
        return deck.size();
    }

    /**
    * Indicates whether the deck is empty or not
    *
    * @return true if the deck is empty, othersize false
    */
    public boolean isEmpty() {
        return deck.isEmpty();
    }

    /**
    * Indicates whether the card is inside the deck
    *
    * @param card Card we are looking for
    * @return true if the deck contains the card, otherwise false
    */
    public boolean contains(Card card) {
        return deck.contains(card);
    }

    /**
    * Remove all the card inside the deck
    */
    public void discard() {
        deck.clear();
    }

    /**
    * Remove the first card in the deck
    *
    * @throws CardException if the deck is already emptied.
    * @return the card tha removed from deck to Card
    */
    public Card deal() {
        if(deck.isEmpty()){
            throw new CardException("The deck is empty.");
        }
        return deck.remove(0);
    }

    /**
    * Shuffle the card inside this deck
    *
    */
    public void shuffle() {
        Collections.shuffle(deck);
    }

    /**
    * Add the given card to the deck
    *
    * @param card Card we want to add
    */
    public void add(Card card) {
        deck.add(card);
    }
}
