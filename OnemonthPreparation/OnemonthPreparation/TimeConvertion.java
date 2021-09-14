package OnemonthPreparation;
import  java.util.*;
import java.text.*;


public class TimeConvertion {

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        DateFormat inFormat = new SimpleDateFormat("hh:mm:ssaa");
        DateFormat outFormat = new SimpleDateFormat("HH:mm:ss");
        sc.close();
        
        Date date = null;
        try{
            date = inFormat.parse(s);
        }
        catch(ParseException e)
        {
            e.printStackTrace();
        }
        if(date!= null)
        {
            String myDate = outFormat.format(date);
            System.out.println(myDate);
        }
    }
    



}
