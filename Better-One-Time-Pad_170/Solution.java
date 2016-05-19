import java.util.Random;

public class Solution {

    // http://stackoverflow.com/a/20183412
    public static long getSeed(int i1, int i2) {
        final long multiplier = 0x5DEECE66DL;
        final long inv_mult = 0xDFE05BCB1365L;
        final long increment = 0xBL;
        final long mask = ((1L << 48) - 1);

        long suffix = 0L;
        long lastSeed;
        long currSeed;
        int lastInt;

        for (long i=0; i < (1<<16); i++) {
            suffix = i;
            currSeed = ((long)i2 << 16) | suffix;
            lastSeed = ((currSeed - increment) * inv_mult) & mask;
            lastInt = (int)(lastSeed >>> 16);

            if (lastInt == i1) {
                /* We've found the current seed, need to roll back 2 seeds */
                currSeed = lastSeed;
                lastSeed = ((currSeed - increment) * inv_mult) & mask;
                return lastSeed ^ multiplier;
            }
        }

        /* Error, current seed not found */
        System.err.println("current seed not found");
        return 0;
    }

    public static void main(String[] args) {
        long seed = getSeed(-1837086, -834601712);
        System.out.println("The seed is " + seed);

        Random r = new Random(seed);
        int[] encrypted = {105, 69, 70, 88, 7, 94, 0, 64, 0, 57, 3, 117, 93, 108, 50, 15, 18, 79, 39, 98, 39, 108, 34, 21, 71, 118, 121, 26, 112};
        String flag = "";
        String alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_0123456789";

        int[] rand = new int[encrypted.length];
        // Get rng to desired state
        for (int i = 0; i < 256; i++) {
            r.nextInt();
        }

        // Store the rng's
        for (int i = 0; i < encrypted.length; i++) {
            rand[i] = r.nextInt();
        }

        for (int i = 0; i < encrypted.length; i++) {
            // Brute force the characters of the flag
            for (int j = 0; j < alphabet.length(); j++) {
                int candidate = Math.abs((alphabet.charAt(j) ^ rand[i]) % 128);
                if (candidate == encrypted[i]) {
                    flag += alphabet.charAt(j);
                }
            }
        }
        if (flag.length() != encrypted.length) {
            System.out.println("Could not find flag.");
            return;
        }
        System.out.println(flag);
    }
}

// flag{prngs_arent_very_secure}
