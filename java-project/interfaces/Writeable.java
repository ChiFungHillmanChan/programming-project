import java.io.IOException;
import java.io.Writer;

public interface Writeable {
    void writeTo(Writer destination)throws IOException; 
}
