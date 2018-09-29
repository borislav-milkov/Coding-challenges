import java.util.Random;

/*Given a stream of elements too large to store in memory, 
 * pick a random element from the stream with uniform probability.
 * */

public class RandomStream {
	static int result = 0;
	static int count = 0;
	
	static int pickRandom(int index) {
		count += 1;
		
		if(count == 1) {
			result = index;
		}
		
		else {
			Random r = new Random();
			int i = r.nextInt(count);
			
			if(i == count-1) {
				return index;
			}
		}
		
		return result;
	} 
	
	public static void main(String[] args) { 
        int stream[] = {1, 2, 3, 4}; 
        int n = stream.length; 
        for(int i = 0; i < n; i++) 
            System.out.println("Random number from first " + (i+1) + 
                               " numbers is " + pickRandom(stream[i])); 
    } 
}