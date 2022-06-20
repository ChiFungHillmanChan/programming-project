package comp1721.cwk2;

import java.util.ArrayList;

import comp1721.cwk2.Card.Rank;

// Implement PokerHand class here

/**
 * Program to creates a PokerHand
 *
 * <p> This is the function to create Poker Hand in card Game<p>
 *
 * @author Chi Fung Hillman Chan
 */


public class PokerHand{
    /**
     * private arratList for Poker Hand
     */
    private ArrayList<Card> hand;
    /**
     * Static value for the full hand size 5
     */
    public static final int FULL_SIZE = 5;

    /**
     * Created an empty Poker Hand
     */
    public PokerHand(){
        hand = new ArrayList<Card>();
    }

    /**
     * Created a Poker Hand with cards added in
     *
     * @param getCard the card added
     */
    public PokerHand(String getCard){
        hand = new ArrayList<Card>();
        String[] cards = getCard.split(" ");
        if(cards.length > FULL_SIZE){
            throw new CardException("Only five cards in Hand");
        }
        for (String str : cards) {
            Card card = new Card(str);
            hand.add(card);
        }
    }
    @Override
    public String toString(){
        String str = "";
        if(hand.size() > 0){
            str +=  String.format("%s", hand.get(0));
        }
        for (int i = 1; i < hand.size(); i++) {
            str += String.format(" %s", hand.get(i));
        }
        return str;
    }

    /**
     * Give the number of the cards inside the Poker Hand
     *
     * @return Number of cards in deck
     */
    public int size(){
        return hand.size();
    }

    /**
    * Remove all the card inside Poker Hand
    *
    * @throws CardException if Poker Hand is already emptied
    */
    public void discard(){
        if(hand.isEmpty()){
            throw new CardException("Hand is already empty.");
        }
        else{
            hand.clear();
        }
    }
    /**
    * Remove all the card inside Poker Hand and add back to the deck
    *
    * @param deck return the removed card to it
    * @throws CardException if Poker Hand is already emptied
    */
    public void discardTo(Deck deck){
        if(hand.isEmpty()){
            throw new CardException("Hand is already empty.");
        }
        else{
            for (Card card : hand) {
                deck.add(card);
            }
            hand.clear();
        }
    }
    /**
    * Add the given card to the deck
    *
    * @param card Card we want to add
    * @throws CardException if there is already 5 cards in Hand
    * @throws CardException if the card already exist
    */
    public void add(Card card) {
        if(hand.size() == FULL_SIZE){
            throw new CardException("Only 5 cards in hand");
        }
        else if(hand.contains(card)){
            throw new CardException("Card already exist");
        }
        else{
            hand.add(card);
        }
    }
    /**
    * Function to check if the poker hand has a pair
    *
    * @return true is it has a pair, otherwise false;
    */
    public boolean isPair(){
        if(hand.size() != FULL_SIZE){ return false; }

        for ( int i = 0; i < hand.size(); i++ ) {
            for ( int j = 0; j < hand.size(); j++ ) {
                if( hand.get(i).getRank() == hand.get(j).getRank() 
                && i!=j && !isTwoPairs() 
                && !isFullHouse() 
                && !isFourOfAKind() 
                && !isThreeOfAKind() ) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
    * Function to check if the poker hand has two pair
    *
    * @return true is it has two pair, otherwise false;
    */
    public boolean isTwoPairs(){
        if(hand.size() != FULL_SIZE){ return false; }
        int countsame1 = -1;
        int countsame2 = -1;
        for (int i = 0; i < hand.size(); i++) {
            for (int j = 0; j < hand.size(); j++) {
                if(hand.get(i).getRank() == hand.get(j).getRank() && i != j){
                    countsame1 = i;
                    break;
                }
            }
        }
        if(countsame1 == -1){ return false; }
        for (int i = 0; i < hand.size(); i++) {
            for (int j = 0; j < hand.size(); j++) {
                if(hand.get(i).getRank() == hand.get(j).getRank() 
                && hand.get(i).getRank() != hand.get(countsame1).getRank() 
                && i != j){
                    countsame2 = i;
                    break;
                }
            }
        }
        if(countsame1 >= 0 && countsame2 >= 0 && !isFullHouse()){ return true; }
        return false;
    }

    /**
    * Function to check if the poker hand has three of same kind
    *
    * @return true is it has three of same kind, otherwise false;
    */
    public boolean isThreeOfAKind(){
        if(hand.size() != FULL_SIZE){ return false; }

        int countthree = 0;
        for (int i = 0; i < hand.size(); i++) {
            for (int j = 0; j < hand.size(); j++) {
                if( hand.get(i).getRank().compareTo(hand.get(j).getRank()) == 0 ){
                    countthree += 1;
                }
                if(countthree == 3 && !isFourOfAKind() && !isFullHouse() ){ return true; }
            }
            countthree = 0;
        }
        return false;
    }

    /**
    * Function to check if the poker hand has four of same kind
    *
    * @return true is it has four of same kind, otherwise false;
    */
    public boolean isFourOfAKind(){
        if(hand.size() != FULL_SIZE){ return false; }

        int countfour = 0;
        for (int i = 0; i < hand.size(); i++) {
            for (int j = 0; j < hand.size(); j++) {
                if(hand.get(i).getRank() == hand.get(j).getRank()){
                    countfour += 1;
                    if(countfour == 4){ return true; }
                }
            }
            countfour = 0;
        }
        return false;
    }

    /**
    * Function to check if the poker hand has a full house
    *
    * @return true is it has a full house, otherwise false;
    */
    public boolean isFullHouse(){
        int countsame1 = 0;
        int countsame2 = 0;

        if(hand.size() != FULL_SIZE){ return false; }

        Rank rank1 = hand.get(0).getRank();
        Rank rank2 = null;

        for (int i = 0; i < hand.size(); i++) {
            if(hand.get(i).getRank() != rank1 ){
                rank2 = hand.get(i).getRank();
                break;
            }
        }
        if(rank2 == null){ return false; }
        
        for (int i = 0; i < hand.size(); i++) {
            if(rank1 == hand.get(i).getRank()){
                countsame1 += 1;
            }
            else if( rank2 == hand.get(i).getRank()){
                countsame2 += 1;
            }
        }
        if( countsame1 == 3 && countsame2 == 2 ){ return true; }
        if( countsame1 == 2 && countsame2 == 3 ){ return true; }
        return false;
    }

    /**
    * Function to check if the poker hand has a flush
    *
    * @return true is it has a flush, otherwise false;
    */
    public boolean isFlush(){
        if(hand.size() != FULL_SIZE){ return false; }
        for (int i = 0; i < FULL_SIZE - 1; i++) {
            if(hand.get(i).getSuit() != hand.get(i+1).getSuit()){ return false; }
        }
        return true;
    }

    /**
    * Function to check if the poker hand has a straight
    *
    * @return true is it has a straight, otherwise false;
    */
    public boolean isStraight(){
        /* Value to calculate straight */
        int calculatelarge = 0;
        int calculatesmall = -1;
        int count = 0;
        int counthand = 0;
        if(hand.size() != FULL_SIZE){ return false; }
        /* if have same rank, directly return false */
        for (int i = 0; i < hand.size(); i++) {
            for (int j = 0; j < hand.size(); j++) {
                if(hand.get(i).getRank() == hand.get(j).getRank() && i!= j){ return false; }
            }
        }
        /* Check if there is straight with high Ace*/
        for (int i = 0; i < hand.size(); i++) {
            if(hand.get(i).getRank()== Rank.ACE){ count+=1; }
            else if(hand.get(i).getRank()== Rank.TEN){ count+=1; }
            else if(hand.get(i).getRank()== Rank.JACK){ count+=1; }
            else if(hand.get(i).getRank()== Rank.QUEEN){ count+=1; }
            else if(hand.get(i).getRank()== Rank.KING){ count+=1; }

            if(count == 5){ return true; }
        }
        /* check normal straight */
        for ( Rank rk : Rank.values() ) {
            for (int i = 0; i < hand.size(); i++) {
                if(hand.get(i).getRank() == rk){
                    if(calculatesmall == -1){ calculatesmall = counthand; }
                    else if(counthand < calculatelarge){ calculatesmall = counthand; }
                    else if(counthand > calculatelarge){ calculatelarge = counthand; }
                }
            }
            counthand++;
        }
        if(calculatelarge - calculatesmall == 4) { return true; }
        return false;
    }
}
