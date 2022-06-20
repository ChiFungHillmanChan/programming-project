package comp1721.cwk2;

/**
 * Class representing exceptions relating to card games.
 *
 * <p>Provided for use in COMP1721 Coursework 2.</p>
 *
 * @author Nick Efford
 */
public class CardException extends RuntimeException {
  /**
   * Create a CardException with the given message.
   *
   * @param message Error message associated with this exception
   */
  public CardException(String message) {
    super(message);
  }
}
