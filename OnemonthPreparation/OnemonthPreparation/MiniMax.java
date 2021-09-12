package OnemonthPreparation;

import java.io.*;
import java.util.*;

public class MiniMax {
    
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        long[] m = new long[5];
        for (int i =0;i<5;i++)
        {
            m[i]=sc.nextLong();
        }
        Arrays.sort(m);
        long x=0;
        long y=0;
        for(int i=0;i<4;i++)
        {
            x=x+m[i];
        }
        for(int i=1;i<5;i++)
        {
            y=y+m[i];
        }
        System.out.println(x+" "+y);
    }


}
