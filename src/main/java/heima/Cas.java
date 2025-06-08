package heima;

import java.util.concurrent.atomic.LongAdder;

public class Cas {

    LongAdder la = new LongAdder();

    private void func() {
        la.add(11);
    }


    public static void main(String[] args) {
        Cas c = new Cas();
        c.func();
    }

}
