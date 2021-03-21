import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class LeetCode648 {

    public String replaceWords(List<String> dictionary, String sentence) {
        Collections.sort(dictionary);

        List<String> words = Arrays.asList(sentence.split(" "));
        for (int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            boolean set = false;
            for (int j = 1; j < word.length(); j++) {
                String substring = word.substring(0, j);
                if (set) {
                    set = false;
                    break;
                }
                for (String s : dictionary) {
                    if (s.length() > substring.length() + 1){
                        break;
                    }
                    if (substring.equals(s)) {
                        words.set(i, s);
                        set = true;
                        break;
                    }
                }
            }
        }
        return String.join(" ", words);
    }

    public static void main(String[] args) {
        List<String> dictionary = Arrays.asList("a", "aa", "aaa", "aaaa");
        String sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa";
        LeetCode648 leetCode648 = new LeetCode648();
        System.out.println(leetCode648.replaceWords(dictionary, sentence));
    }
}
