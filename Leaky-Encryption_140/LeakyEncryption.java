import java.math.BigInteger;
import java.nio.charset.Charset;
import java.security.SecureRandom;
import java.util.Random;

public class LeakyEncryption {
    private static String flag = "{{REDACTED}}";

    private static Random r = new SecureRandom();
    private static BigInteger TWO = BigInteger.valueOf(2);
    private static BigInteger THREE = BigInteger.valueOf(3);
    private static BigInteger FOUR = BigInteger.valueOf(4);

    public static void main(String[] args) {
        BigInteger[] key = genKey(1024);
        BigInteger N = key[0];
        System.out.println("N="+N);
        BigInteger p = key[1];
        //System.out.println("p="+p);
        BigInteger q = key[2];
        //System.out.println("q="+q);

        String testMessage = "Hello World!";
        BigInteger testEnc = encrypt(intFromString(testMessage), N);
        BigInteger[] testDec = decrypt(testEnc, p, q);

        //test to make sure our implementation was correct
        boolean successful = false;
        for(BigInteger dec:testDec) {
            System.out.println("dec="+dec);
            if(stringFromInt(dec).equals(testMessage)) {
                successful = true;
            }
        }
        System.out.println("Success = "+successful);

        //if it works, encrypt our flag.
        if(successful) {
            BigInteger flagEnc = new BigInteger("39590922396654916086628650019888739576498733522051085794871782506305512496992920507954186593534372168795535544484431901327020054086517722889640267634647695915443094275580169");
            BigInteger[] flagDec = decrypt(flagEnc, p, q);
            for (BigInteger dec:flagDec) {
                System.out.println(stringFromInt(dec));
            }
            //there's no way they can crack 2048 bit encryption!
            System.out.println("encrypted flag="+flagEnc);
        }
    }

    public static BigInteger intFromString(String m) {
        return new BigInteger(m.getBytes(Charset.forName("ascii")));
    }

    public static String stringFromInt(BigInteger m) {
        return new String(m.toByteArray(), Charset.forName("ascii"));
    }

    public static BigInteger[] genKey(int bitLength) {
        BigInteger p = blumPrime(bitLength/2);
        BigInteger q = blumPrime(bitLength/2);
        BigInteger N = p.multiply(q);
        return new BigInteger[]{N,p,q};
    }

    public static BigInteger encrypt(BigInteger m, BigInteger N) {
        return m.modPow(TWO, N);
    }

    public static BigInteger[] decrypt(BigInteger c, BigInteger p , BigInteger q) {
        BigInteger N = p.multiply(q);
        BigInteger m_p1 = c.modPow(p.add(BigInteger.ONE).divide(FOUR), p);
        BigInteger m_p2 = p.subtract(m_p1);
        BigInteger m_q1 = c.modPow(q.add(BigInteger.ONE).divide(FOUR), q);
        BigInteger m_q2 = q.subtract(m_q1);

        BigInteger[] ext = ext_gcd(p,q);
        BigInteger y_p = ext[1];
        BigInteger y_q = ext[2];

        BigInteger d1 = y_p.multiply(p).multiply(m_q1).add(y_q.multiply(q).multiply(m_p1)).mod(N);
        BigInteger d2 = y_p.multiply(p).multiply(m_q2).add(y_q.multiply(q).multiply(m_p1)).mod(N);
        BigInteger d3 = y_p.multiply(p).multiply(m_q1).add(y_q.multiply(q).multiply(m_p2)).mod(N);
        BigInteger d4 = y_p.multiply(p).multiply(m_q2).add(y_q.multiply(q).multiply(m_p2)).mod(N);

        return new BigInteger[]{d1,d2,d3,d4};
    }

    public static BigInteger[] ext_gcd(BigInteger a, BigInteger b) {
        BigInteger s = BigInteger.ZERO;
        BigInteger old_s = BigInteger.ONE;
        BigInteger t = BigInteger.ONE;
        BigInteger old_t = BigInteger.ZERO;
        BigInteger r = b;
        BigInteger old_r = a;
        while(!r.equals(BigInteger.ZERO)) {
            BigInteger q = old_r.divide(r);
            BigInteger tr = r;
            r = old_r.subtract(q.multiply(r));
            old_r=tr;

            BigInteger ts = s;
            s = old_s.subtract(q.multiply(s));
            old_s=ts;

            BigInteger tt = t;
            t = old_t.subtract(q.multiply(t));
            old_t=tt;
        }
        return new BigInteger[]{old_r, old_s, old_t};
    }

    public static BigInteger blumPrime(int bitLength) {
        BigInteger p = BigInteger.probablePrime(bitLength, r);
        while(!p.mod(FOUR).equals(THREE)) {
            p=BigInteger.probablePrime(bitLength,r);
        }
        return p;
    }
}
